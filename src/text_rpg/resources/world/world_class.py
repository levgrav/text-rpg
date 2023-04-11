"""
world_class
~~~~~~~~~~~
Factory file for class `World`
"""

# --- Imports --- #
from resources.things.area_class import Area, create_area
from resources.things.room_class import Room, create_room
from resources.things.container_class import Container, create_container
from resources.things.item_class import create_item
from resources.entities.npc.npc_class import Npc, create_npc
from dataclasses import dataclass

# --- Class Definition --- #
@dataclass
class World:
    name: str
    description: str
    areas: list[Area]
    npcs: list[Npc]

# --- Functions --- # 
def create_world(world_dict: dict):
    """Factory function for `World` class. Calls factory functions for `Area` and `Npc` classes.
    
    Args:
        world_dict (dict): dictionary with all relevant information on the `World` object. Data should be taken from `game_data/default_world.json`

    Returns:
        (World): object containing all information given
    """
    
    for i, area in enumerate(world_dict['areas']):  # creates Area objects in what will be `world.areas`
        world_dict['areas'][i] = create_area(area)
    
    for i, npc in enumerate(world_dict['npcs']):    # creates Npc  object in what will be `world.npcs`
        world_dict['npcs'][i] = create_npc(npc)
    
    return World(**world_dict) # creates world object