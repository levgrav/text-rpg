from resources.things.item_class import Item, create_item
from resources.things.container_class import Container, create_container
from resources.things.room_class import Room, create_room
from dataclasses import dataclass, field


@dataclass
class Area(Room):
    pos: list[int] = field(default_factory=list)
    rooms: list[Room] = field(default_factory=list)

def create_area(area_dict: dict):
    for i, item in enumerate(area_dict['inventory']):     
        area_dict['inventory'][i] = create_item(item)
    
    for i, container in enumerate(area_dict['containers']):     
        area_dict['containers'][i] = create_container(container)
    
    for i, room in enumerate(area_dict['rooms']):     
        area_dict['rooms'][i] = create_room(room)
    
    return Area(**area_dict)
