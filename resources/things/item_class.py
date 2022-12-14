from dataclasses import dataclass
import json
import os
game_data_path = os.getcwd() + '\\game_data'

@dataclass
class Item:
    name: str = ''
    item_type: str = '' 
    description: str = ''

class ItemNotFoundError(BaseException):
    pass

def create_item(name: str) -> Item:
    with open(f'{game_data_path}\\item_settings.json', 'r') as f:
        all_data: dict = json.load(f)
        for item_type, items in all_data.items():
            for item_name, item_data in items.items():
                if item_name == name:
                    i = Item(name=name, item_type=item_type, description=item_data['description'])
                    for attr, val in item_data.items():
                        i.__setattr__(attr, val)
                    return i
    
    raise ItemNotFoundError(name)

if __name__ == "__main__":
    i = create_item('sword')
    print('')
