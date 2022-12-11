from resources.things.item_class import create_item
from dataclasses import dataclass, field
from processing.classes import Class


@dataclass
class Npc:
    name: str = ''
    
    def move(self, world, entities):
        pass

    def go(self, world, entities):
        pass

    def equip(self, world, entities):
        pass

    def unequip(self, world, entities):
        pass

    def enter(self, world, entities):
        pass

    def leave(self, world, entities):
        pass

    def look_around(self, world, entities):
        pass

    def look_at(self, world, entities):
        pass

    def pick_up(self, world, entities):
        pass

    def take(self, world, entities):
        pass

    def drop(self, world, entities):
        pass

    def eat(self, world, entities):
        pass

    def talk(self, world, entities):
        pass

    def fight(self, world, entities):
        pass
    
def create_npc(npc_dict: dict):

    n = Npc()
    for attr, val in npc_dict.items():
        if attr == 'stats':
            val = Class(**val)
        elif attr == 'equipped':
            val = Class(**val)
        elif attr == 'inventory':
            for i, item in enumerate(val):     
                val[i] = create_item(item)
            
        n.__setattr__(attr, val)
    return n
