"""npc_class
~~~~~~~~~
Factory file for `Npc` objects"""

from resources.things.item_class import create_item
from dataclasses import dataclass, field
from processing.classes import Class


@dataclass
class Npc:
    name: str = ''
    
def create_npc(npc_dict: dict):
    """Factory function for `Npc` objects. Data should be taken from `game_data/default_world.json`. Usually called in `World` object factory

    Args:
        npc_dict (dict): Dictionary from json that contains information for the Npc

    Returns:
        n (Npc): Finished `Npc` object containing all info"""
        
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
