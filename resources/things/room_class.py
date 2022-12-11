from resources.things.item_class import Item, create_item
from resources.things.container_class import Container, create_container
from dataclasses import dataclass, field


@dataclass
class Room(Container):
    containers: list[Container] = field(default_factory=list)

def create_room(room_dict: dict):
    for i, item in enumerate(room_dict['inventory']):     
        room_dict['inventory'][i] = create_item(item)
    
    for i, container in enumerate(room_dict['containers']):     
        room_dict['containers'][i] = create_container(container)
    
    return Room(**room_dict)
