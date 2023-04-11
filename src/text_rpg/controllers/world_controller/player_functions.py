"""
player_functions
~~~~~~~~~~~~~~~~

A file with a list of functions that the player can do"""


import processing.functions as pfun
import controllers.output_controller.output_controller as out

def move(player, world, direction):
    """Function that can be called by the user to move from area to area
    
    Parameters:

        `player (Player)`: player that will be affected 
        `world (World)`: world in which player moves
        `direction (str)`: string ( "north" | "south" | "east" | "west" ) that determines the direction of movement
        
    Returns:

        `world (World)`: updated world
        `msg (str)`: message that will be outputted to the GUI or console

    Precondition: 

        `player` object (class `Player`) needs attribute `"currentroom"` of type: `list[str]`. `world` object (class `World`) needs attribute `"areas"` of type: `list[Area]`. `area` object (class `Area`) in `world.areas` needs attributes `"name"` of type: `str` and `"pos"` of type: `list[int]` with length `2`
    
    Postcondition: 
        `player.currentroom` will change based on whichever room has the new `x` and `y` position of `player`
    """
        # if in room, unhappy
    if player.current_room.__len__() > 1:
        return world, "Player is currently inside a room, unable to use command 'move <direction>"

    # for message at the end
    old_area = player.current_room[0]

    # find area that matches player.current_room[0]
    area_name = player.current_room[0]
    (area,*_), msg = pfun.find_room(world, area_name)
    if isinstance(area, pfun.Class):
        return world, msg
    x, y = area.pos # type: ignore

    # find new position
    match direction:
        case 'north': y += 1
        case 'south': y -= 1
        case 'east':  x += 1
        case 'west':  x -= 1
        case _:       return world, "Invalid 'direction' argument for command 'move <direction>'"
    
    # find area that matches new position
    _, area = pfun.find_by_attr(world.areas, "pos", [x,y], case_sensitive = False)
    if isinstance(area, pfun.Class):
        return world, "Cannot go there"

    player.current_room = [area.name] # type: ignore

    return world, f"Moved {direction} from {old_area} to {player.current_room[0]}"

def equip(player, world, item_name, place = None):

    i, item = pfun.find_by_attr(player.inventory, "name", item_name, case_sensitive=False)
    
    # item not in inventory
    if i == -1: return world, f"Item {item_name} not in inventory"
    
    # put item in correct place
    if item.item_type not in ["Melee_Weapon", "Ranged_Weapon", "Armor"]: # type: ignore
        return world, f"Item '{item.name.lower()}' with type '{item.item_type}' is not a type you can equip" # type: ignore
    
    if 'place' not in item.__dict__.keys(): # if item does not have attribute 'place'
        p_places = ['primary', 'secondary'] # possible places
    else: p_places = [item.place] # type: ignore

    if place != None and place not in p_places:
        return world, f"Cannot equip item '{item.name.lower()}' in place {place}" # type: ignore
    
    if place == None: place = p_places[0]

    player.equipped.__setattr__(place, item) # type: ignore
    player.inventory.remove(item) # type: ignore
    
    return world, f"Equipped '{item.name.lower()}' in place: '{place}'" # type: ignore

def unequip(player, world, item_name, place = None):

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
    
    # find area, room that matches current area
    (area, room), msg = pfun.find_room(world, *player.current_room)
    
    # if in room, unhappy
    if room:
        return world, "Player is currently inside a room, unable to use command 'enter <room>'"
    
    if area == None:
        return world, f"Player attribute: 'current_room' with value: {player.current_room} does not match any area"
    
    for a_room in area.rooms:
        if a_room.name.lower() == room_name.lower():
            player.current_room.append(a_room.name)
            return world, f'Entered room: {a_room.name}'

    return world, f"Could not find a match for room: {room_name} in area: {area.name}"

def leave(player, world, room_name = None):
    # find area matches current area
    # needs current_room attr
    
    current_room = player.current_room
    
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
    (*_, room), msg = pfun.find_room(world, *player.current_room)

    if "Found room: '" not in msg:
        return world, msg

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

    for contianer in room.containers: # type: ignore
        if contianer.name.lower() == entity_name:
            return world, pfun.disp_obj(contianer, 'name')

    for npc in world.npcs:
        if npc.name.lower() == entity_name.lower() and npc.current_room == player.current_room:
            return world, pfun.disp_obj(npc, 'name')

    for item in room.inventory: # type: ignore
        if item.name.lower() == entity_name:
            return world, pfun.disp_obj(item, 'name')
                

    return world, f"Could not find entity: '{entity_name}' in room: {player.current_room}"

def pick_up(player, world, item_name):
    (area, room), msg = pfun.find_room(world, *player.current_room)

    if "Found room: '" not in msg:
        return world, msg

    if room == None: room = area

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

    for container in room.containers: # type: ignore
        if container.name.lower() == container_name:
            break
    else:
        return world, f"Could not find container: '{container_name}' in room"

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

    for container in room.containers: # type: ignore
        if container.name.lower() == container_name:
            break
    else:
        return world, f"Could not find container: '{container_name}' in room"
    
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

def talk(player, world, npc_name):
    return world, f'talk {npc_name}'

def fight(player, world, npc_name):
    done = False
    turn = player
    while not done:
        # decide action
        if turn == player:
        # player action
            player_action = {
                "action": "slash",
                "object": "shield",
                "direction": "right"
            }
            npc_response = {
                "action": "dodge",
                "direction": "left"
            }

            turn = npc_name

        # npc action
        else:
            npc_action = {
                "action": "stab",
                "object": "dagger",
                "direction": "up-left"
            }
    return world, f'fight {npc_name}'

def output_player(player, world, *_):

    return world, pfun.disp_obj(player, 'name')
