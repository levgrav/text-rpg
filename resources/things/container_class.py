from resources.things.item_class import Item, create_item
from dataclasses import dataclass, field


@dataclass
class Container:
    name: str = ''
    description: str = ''
    inventory: list[Item] = field(default_factory=list)


def create_container(container_dict: dict):
    for i, item in enumerate(container_dict['inventory']):     
        container_dict['inventory'][i] = create_item(item)
    
    return Container(**container_dict)