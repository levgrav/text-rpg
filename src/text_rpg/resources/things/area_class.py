#  --- Imports --- #
from resources.things.item_class import Item, create_item
from resources.things.container_class import Container, create_container
from resources.things.room_class import Room, create_room
from dataclasses import dataclass, field

# --- Class definitions --- #
@dataclass
class Area(Room):
    pos: list[int] = field(default_factory=list)
    rooms: list[Room] = field(default_factory=list)

# --- Functions --- #
def create_area(area_dict: dict):
    """Factory function for `Area` objects. Useally called withing the factory for `World`.

    Args:
        area_dict (dict): Data taked from json file containing information for world

    Returns:
        (Area): Finished object with all dependent object also created
    """
    # Creates `Item` objects for `Area.inventory`
    for i, item in enumerate(area_dict['inventory']):     
        area_dict['inventory'][i] = create_item(item)
    
    # Creates `Container` objects for `Area.containers`
    for i, container in enumerate(area_dict['containers']):     
        area_dict['containers'][i] = create_container(container)
    
    # Creates `Room` objects for `Area.rooms`
    for i, room in enumerate(area_dict['rooms']):     
        area_dict['rooms'][i] = create_room(room)
    
    # Creates `Area`
    return Area(**area_dict)
