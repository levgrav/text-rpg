import processing.functions as pfun
import controllers.output_controller.output_controller as out

def move(player, world, direction):
    # needs current_room attr
    need_attr = pfun.need_attrs(player, 'current_room')
    if need_attr:
        return world, f"Player needs attribute '{need_attr}' to use 'move' command"
    
    current_room = player.__getattribute__("current_room")
    
    # current room needs to be list
    if type(current_room) != list:
        return world, "Attribute 'current_room' needs to be type: 'list'"

    # if in room, unhappy
    if current_room.__len__() > 1:
        return world, "Player is currently inside a room, unable to use command 'move <direction>"

    # for message at the end
    old_area = player.current_room[0]

    # find current position
    # if player has position attr, use that
    class_type = None
    attr = pfun.get_attr(player, 'pos', [tuple, list, dict], length = 2, keys = ['x', 'y'])
    if attr:
        (x, y), class_type = attr

    elif 'x' in player.__dict__.keys() and 'y' in player.__dict__.keys():
        x = player.__getattribute__('x'); y = player.__getattribute__('y')
        class_type = 'raw'

    else:
        # find area that matches player.current_room [0]
        area_name = current_room[0]
        x = y = None
        for area in world.areas:
            if area.name.lower() == area_name.lower():
                x,y = area.pos

        # if no area matches, unhappy
        if x == y == None:
            return world, "Could not find area that matched given area"
    
    # find new position
    match direction:
        case 'north':
            y += 1 # type: ignore
        case 'south':
            y -= 1 # type: ignore
        case 'east': 
            x += 1 # type: ignore
        case 'west':
            x -= 1 # type: ignore
        case _:
            return world, "Invalid 'direction' argument for command 'move <direction>'"
    
    # find area that matches new position
    for area in world.areas:
        if area.pos[0] == x and area.pos[1] == y:
            player.current_room = [area.name]
            if class_type == 'raw':
                player.x = x; player.y = y
            elif class_type != None:
                pass

    return world, f"Moved {direction} from {old_area} to {player.current_room[0]}"

def equip(player, world, item_name, place = None):
    # needs inventory, equipped attrs
    need_attr = pfun.need_attrs(player, 'inventory', 'equipped')
    if need_attr:
        return world, f"Player needs attribute '{need_attr}' to use 'equip' command"

    # find item in inventory
    item = None

    # checks for the first item in inventory that matches
    for item in player.inventory: #type: ignore
        if item.name.lower() == item_name:
            break
    
    # if item still == None, item must not be in inventory
    if item == None:
        return world, f"Item {item_name} not in inventory"

    # put item in correct place
    if item.item_type != "Melee_Weapon" and item.item_type != "Ranged_Weapon" and item.item_type != "Armor":
        return world, f"Item '{item.name.lower()}' with type '{item.item_type}' is not a type you can equip"
    
    if pfun.need_attrs(item, 'place') == 'place': # if item does not have attribute 'place'
        p_places = ['primary', 'secondary'] # possible places
    else: p_places = [item.place]

    if place != None and place not in p_places:
        return world, f"Cannot equip item '{item.name.lower()}' in place {place}"
    
    if place == None: place = p_places[0]

    player.equipped.__setattr__(place, item) # type: ignore
    player.inventory.remove(item) # type: ignore
    
    return world, f"Equipped '{item.name.lower()}' in place: '{place}'"

def unequip(player, world, item_name, place = None):
    
    # needs inventory, equipped attrs
    need_attr = pfun.need_attrs(player, 'inventory', 'equipped')
    if need_attr:
        return world, f"Player needs attribute '{need_attr}' to use 'equip' command"

    # find item in equipped
    item = None

    # if place is specified, check only there
    if place:
        item = player.equipped.__getattribute__(place) #type: ignore
        if item == None or item.name.lower() != item_name:
            return world, f"Item: '{item_name}' not in place: '{place}'"

    # checks for the first item in equipped that matches
    for place, item in player.equipped.__dict__.items(): #type: ignore
        if item != None and item.name.lower() == item_name:
            break

    # if item still == None, item must not be equipped
    if item == None:
        return world, f"Item {item_name} not equipped"
    
    # add item to inventory and remove it from equipped
    player.inventory.append(item) # type: ignore
    player.equipped.__setattr__(place, None) # type: ignore
    
    return world, f'Unequipped item: {item_name} from place: {place}'

def enter(player, world, room_name):
    # find area matches current area
    # needs current_room attr
    need_attr = pfun.need_attrs(player, 'current_room')
    if need_attr:
        return world, f"Player needs attribute '{need_attr}' to use 'move' command"
    
    current_room = player.__getattribute__("current_room")
    
    # current room needs to be list
    if type(current_room) != list:
        return world, "Attribute 'current_room' needs to be type: 'list'"

    # if in room, unhappy
    if current_room.__len__() > 1:
        return world, "Player is currently inside a room, unable to use command 'enter <room>'"

    # find room in area that matches area
    area = None
    area_name = current_room[0]
    for w_area in world.areas:
        if w_area.name.lower() == area_name.lower():
            area = w_area
    
    if area == None:
        return world, f"Player attribute: 'current_room' with value: {current_room} does not match any area"
    
    for a_room in area.rooms:
        if a_room.name.lower() == room_name.lower():
            player.current_room.append(a_room.name)
            return world, f'Entered room: {a_room.name}'

    return world, f"Could not find a match for room: {room_name} in area: {area_name}"

def leave(player, world, room_name = None):
    # find area matches current area
    # needs current_room attr
    need_attr = pfun.need_attrs(player, 'current_room')
    if need_attr:
        return world, f"Player needs attribute '{need_attr}' to use 'leave' command"
    
    current_room = player.__getattribute__("current_room")
    
    # current room needs to be list
    if type(current_room) != list:
        return world, "Attribute 'current_room' needs to be type: 'list'"

    # if in room, unhappy
    if current_room.__len__() < 2:
        return world, "Player is not currently inside a room, unable to use command 'leave <room?>'"

    if room_name and current_room[1] != room_name:
        return world, f"Player not in room: {room_name}, player is in room: {current_room[1]}"
    
    lr = current_room[1]
    current_room.pop()

    return world, f'Left room: {lr}'

def look_around(player, world):
    (area, room), msg = pfun.find_room(world, *player.current_room)

    if "Found room: '" not in msg:
        return world, msg

    if room == None: room = area

    msg += "\n" + pfun.disp_obj(room, 'name')
    msg += "\n  npcs: ["
    for npc in world.npcs:
        if npc.current_room == player.current_room:
            msg += f"\"{npc.name}\", "
    msg += "]"

    return world, msg

def look_at(player, world, entity_name):
    (area, room), msg = pfun.find_room(world, *player.current_room)

    if "Found room: '" not in msg:
        return world, msg

    if room == None: room = area

    if not pfun.need_attrs(room, "containers"):
        for contianer in room.containers: # type: ignore
            if contianer.name.lower() == entity_name:
                return world, pfun.disp_obj(contianer, 'name')
    
    if not pfun.need_attrs(world, "npcs"):
        for npc in world.npcs:
            if npc.name.lower() == entity_name.lower() and npc.current_room == player.current_room:
                return world, pfun.disp_obj(npc, 'name')
    
    if not pfun.need_attrs(room, "inventory"):
        for item in room.inventory: # type: ignore
            if item.name.lower() == entity_name:
                return world, pfun.disp_obj(item, 'name')
                

    return world, f"Could not find entity: '{entity_name}' in room: {player.current_room}"

def pick_up(player, world, item_name):
    (area, room), msg = pfun.find_room(world, *player.current_room)

    if "Found room: '" not in msg:
        return world, msg

    if room == None: room = area
    
    if pfun.need_attrs(room, "inventory"):
        return world, f"Room needs attribute: 'inventory' to use function: 'pick_up'"
    
    if pfun.need_attrs(player, "inventory"):
        return world, f"Player needs attribute: 'inventory' to use function: 'pick_up'"

    for item in room.inventory: # type: ignore
        if item.name.lower() == item_name:
            break
    else:
        return world, f"Could not find item: '{item_name}' in room inventory"
    
    room.inventory.remove(item) # type: ignore
    player.inventory.append(item) # type: ignore

    return world, f"Picked up item: '{item.name}' from room: '{room.name}'" # type: ignore        

def take(player, world, item_name, container_name):

    (area, room), msg = pfun.find_room(world, *player.current_room)

    if "Found room: '" not in msg:
        return world, msg

    if room == None: room = area
    
    if pfun.need_attrs(room, "containers"):
        return world, f"Room needs attribute: 'containers' to use function: 'take'"
    
    if pfun.need_attrs(player, "inventory"):
        return world, f"Player needs attribute: 'inventory' to use function: 'take'"

    for container in room.containers: # type: ignore
        if container.name.lower() == container_name:
            break
    else:
        return world, f"Could not find container: '{container_name}' in room"
    
    if pfun.need_attrs(container, "inventory"):
        return world, f"Container needs attribute: 'inventory' to use function: 'take'"

    for item in container.inventory: # type: ignore
        if item.name.lower() == item_name:
            break
    else:
        return world, f"Could not find item: '{item_name}' in inventory of container: {container.name}"
    
    container.inventory.remove(item) # type: ignore
    player.inventory.append(item) # type: ignore

    return world, f"Took item: '{item_name}' from container: '{container.name}'" # type: ignore 

def drop(player, world, item_name):
    (area, room), msg = pfun.find_room(world, *player.current_room)

    if "Found room: '" not in msg:
        return world, msg

    if room == None: room = area
    
    if pfun.need_attrs(room, "inventory"):
        return world, f"Room needs attribute: 'inventory' to use function: 'drop'"
    
    if pfun.need_attrs(player, "inventory"):
        return world, f"Player needs attribute: 'inventory' to use function: 'drop'"

    for item in player.inventory: # type: ignore
        if item.name.lower() == item_name:
            break
    else:
        return world, f"Could not find item: '{item_name}' in player inventory"
    
    room.inventory.append(item) # type: ignore
    player.inventory.remove(item) # type: ignore

    return world, f"Dropped item: '{item.name}' into room: '{room.name}'" # type: ignore  

def put(player, world, item_name, container_name):

    (area, room), msg = pfun.find_room(world, *player.current_room)

    if "Found room: '" not in msg:
        return world, msg

    if room == None: room = area
    
    if pfun.need_attrs(room, "containers"):
        return world, f"Room needs attribute: 'containers' to use function: 'put'"
    
    if pfun.need_attrs(player, "inventory"):
        return world, f"Player needs attribute: 'inventory' to use function: 'put'"

    for container in room.containers: # type: ignore
        if container.name.lower() == container_name:
            break
    else:
        return world, f"Could not find container: '{container_name}' in room"
    
    if pfun.need_attrs(container, "inventory"):
        return world, f"Container needs attribute: 'inventory' to use function: 'put'"

    for item in player.inventory: # type: ignore
        if item.name.lower() == item_name:
            break
    else:
        return world, f"Could not find item: '{item_name}' in inventory of player"
    
    container.inventory.append(item) # type: ignore
    player.inventory.remove(item) # type: ignore

    return world, f"Put item: '{item_name}' into container: '{container.name}'" # type: ignore 

def eat(player, world, item):
    return world, f'eat {item}'

def use(player, world, item):
    return world, f'eat {item}'

def talk(player, world, npc):
    return world, f'talk {npc}'

def fight(player, world, npc):
    return world, f'fight {npc}'

def output_player(player, world):

    out.output_player(player)

    return world, "" 
