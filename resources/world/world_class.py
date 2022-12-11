from resources.things.area_class import Area, create_area
from resources.things.room_class import Room, create_room
from resources.things.container_class import Container, create_container
from resources.things.item_class import create_item
from resources.entities.npc.npc_class import Npc, create_npc
from dataclasses import dataclass


@dataclass
class World:
    name: str
    description: str
    areas: list[Area]
    npcs: list[Npc]
    
def create_world(world_dict: dict):
    
    for i, area in enumerate(world_dict['areas']):     
        world_dict['areas'][i] = create_area(area)
    
    for i, npc in enumerate(world_dict['npcs']):     
        world_dict['npcs'][i] = create_npc(npc)
    
    return World(**world_dict)