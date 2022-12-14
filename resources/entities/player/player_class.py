from dataclasses import dataclass
from resources.things.item_class import create_item
from processing.classes import Class
from processing.functions import get_attr

@dataclass
class Player:
    name: str = ''
    
    def move(self, world, direction):
        # needs current_room attr
        if "current_room" not in self.__dict__.keys():
            return world, "Player needs attribute 'current_room' to use 'move' command"
        else:
            current_room = self.__getattribute__("current_room")
        
        # current room needs to be list
        if type(current_room) != list:
            return world, "Attribute 'current_room' needs to be type: 'list'"

        # if in room, unhappy
        if current_room.__len__() > 1:
            return world, "Player is currently inside a room, unable to use command 'move <direction>"

        print(self.current_room[0])

        # find current position
        # if player has position attr, use that
        class_type = None
        attr = get_attr(self, 'pos', [tuple, list, dict], length = 2, keys = ['x', 'y'])
        if attr:
            (x, y), class_type = attr

        elif 'x' in self.__dict__.keys() and 'y' in self.__dict__.keys():
            x = self.__getattribute__('x'); y = self.__getattribute__('y')
            class_type = 'raw'

        else:
            # find area that matches self.current_room [0]
            area_name = current_room[0]
            x = y = None
            for area in world.areas:
                if area.name == area_name:
                    x,y = area.pos

            # if no area matches, unhappy
            if x == y == None:
                return world, "Could not find area that matched given area"
        
        # find new position
        match direction[0]:
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
                self.current_room = [area.name]
                if class_type == 'raw':
                    self.x = x; self.y = y
                elif class_type != None:
                    pass
    
        print(self.current_room[0])
        return world, None

    def equip(self, world, item, place = None):
        # find item in inventory
        # put item in correct place
        print('equip', item)
        return world, None

    def unequip(self, world, entities):
        print('unequip', entities)
        return world, None

    def enter(self, world, entities):
        print('enter', entities)
        return world, None

    def leave(self, world, entities):
        print('leave', entities)
        return world, None

    def look_around(self, world, entities):
        print('look_around', entities)
        return world, None

    def look_at(self, world, entities):
        print('look_at', entities)
        return world, None

    def pick_up(self, world, entities):
        print('pick_up', entities)
        return world, None

    def take(self, world, entities):
        print('take', entities)
        return world, None

    def drop(self, world, entities):
        print('drop', entities)
        return world, None

    def eat(self, world, entities):
        print('eat', entities)
        return world, None

    def talk(self, world, entities):
        print('talk', entities)
        return world, None

    def fight(self, world, entities):
        print('fight', entities)
        return world, None

def create_player(player_dict) -> Player:

    p = Player()
    for attr, val in player_dict.items():
        if type(val) == dict:
            val = Class(**val)
        elif attr == 'inventory':
            for i, item in enumerate(val):     
                val[i] = create_item(item)
            
        p.__setattr__(attr, val)
    return p

