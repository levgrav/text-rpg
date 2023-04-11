"""container_class
~~~~~~~~~~~~~~~
Factory for `Container` objects
"""

# --- Imports --- #
from resources.things.item_class import Item, create_item
from dataclasses import dataclass, field

# --- Class definitions --- #
@dataclass
class Container:
    name: str = ''
    description: str = ''
    inventory: list[Item] = field(default_factory=list)

# --- Functions --- #
def create_container(container_dict: dict):
    """Factory function for `Container` objects. Is gennerally called within other factories such as `Room` and `Area` which, in turn are called by the `World` class factory

    Args:
        container_dict (dict): Dictionary if all infromation about the `Container`

    Returns:
        (Container): Finished object
    """
    # Creates `Item` objects in `Container.inventory`
    for i, item in enumerate(container_dict['inventory']):     
        container_dict['inventory'][i] = create_item(item)
    
    return Container(**container_dict)