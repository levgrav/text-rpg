from dataclasses import dataclass
from resources.things.item_class import create_item
from processing.classes import Class

@dataclass
class Player:
    name: str = ''
    
    def move(self, world, entities):
        print('move', entities)

    def go(self, world, entities):
        print('go', entities)

    def equip(self, world, entities):
        print('equip', entities)

    def unequip(self, world, entities):
        print('unequip', entities)

    def enter(self, world, entities):
        print('enter', entities)

    def leave(self, world, entities):
        print('leave', entities)

    def look_around(self, world, entities):
        print('look_around', entities)

    def look_at(self, world, entities):
        print('look_at', entities)

    def pick_up(self, world, entities):
        print('pick_up', entities)

    def take(self, world, entities):
        print('take', entities)

    def drop(self, world, entities):
        print('drop', entities)

    def eat(self, world, entities):
        print('eat', entities)

    def talk(self, world, entities):
        print('talk', entities)

    def fight(self, world, entities):
        print('fight', entities)

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

