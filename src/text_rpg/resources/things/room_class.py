"""
room_class
~~~~~~~~~~
Factory file for `Room` class"""

# --- Imports --- #
from resources.things.item_class import Item, create_item
from resources.things.container_class import Container, create_container
from dataclasses import dataclass, field

# --- Class definition --- #
@dataclass
class Room(Container):
    containers: list[Container] = field(default_factory=list)

# --- Room factory --- #
def create_room(room_dict: dict):
    """Factory function for `Room` class. Calls factory functions for `Item` and `Container`. Is genarally called via the `World` factory which calls the `Area` factory which, in turn, calls this factory with the information passed down through each

    Args:
        room_dict (dict): contains all information for `Room`. Information for each room should be in `game_data/default_world.json`

    Returns:
        (Room) : The completed room with all information stored in a object.
    """

    for i, item in enumerate(room_dict['inventory']): # creates `Item` objects in `Room.inventory` 
        room_dict['inventory'][i] = create_item(item)
    
    for i, container in enumerate(room_dict['containers']): # creates `Conttainer` objects int `Room.containers`
        room_dict['containers'][i] = create_container(container)
    
    return Room(**room_dict) # creates & returns `Room` object from `room_dict`
