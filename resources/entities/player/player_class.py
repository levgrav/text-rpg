from dataclasses import dataclass
from resources.things.item_class import create_item
from processing.classes import Class
import processing.functions as pfun
from controllers.output_controller.output_controller import output_player

@dataclass
class Player:
    name: str = ''

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

