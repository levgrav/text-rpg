"""item_class
~~~~~~~~~~
File that contains class definintion and factory for `Item` class"""
# --- Imports --- #
from dataclasses import dataclass
import json
import os

# --- Configuration --- #
game_data_path = os.getcwd() + '\\game_data'

# --- Class definitions --- #
@dataclass
class Item:
    name: str = ''
    item_type: str = '' 
    description: str = ''

# Special error class
class ItemNotFoundError(BaseException):
    pass

# --- Functions --- #
def create_item(name: str):
    """Factory function for `Item` class

    Args:
        name (str): the name of the item (is used to find all other information)

    Raises:
        ItemNotFoundError: if an item is not in `game_data/item_settings.json`

    Returns:
        item: Item class that matches the name given with the information from the json file
    """
    # Collects data from json file
    with open(f'{game_data_path}\\item_settings.json', 'r') as f:
        all_data: dict = json.load(f)

    # Loops though all posible items
    for item_type, items in all_data.items():
        for item_name, item_data in items.items():
            
            # Checks if name of item matches
            if item_name == name:
                
                # creates item, assigns it data, and raturns it
                item = Item(name=name, item_type=item_type, description=item_data['description'])
                for attr, val in item_data.items():
                    item.__setattr__(attr, val)
                return item
    
    # If no item was found that matches
    raise ItemNotFoundError(name)

# --- Test --- #
if __name__ == "__main__":
    i = create_item('sword')
    print(i.__dict__)
