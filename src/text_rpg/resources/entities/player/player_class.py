"""player_class
~~~~~~~~~~~~
Factory file for `Player` objects"""

# --- Imports --- #
from dataclasses import dataclass
from resources.things.item_class import create_item
from processing.classes import Class
import processing.functions as pfun
# --- Class Definition --- #
@dataclass
class Player:
    name: str = ''

# --- Functions --- #
def create_player(player_dict: dict):
    """Factory function for `Player` objects. Data should be taken from `game_data/default_player.json`

    Args:
        player_dict (dict): Dictionary from json that contains information for the player

    Returns:
        p (Player): Finished `Player` object containing all info
    """
    p = Player()
    for attr, val in player_dict.items():
        if type(val) == dict:
            val = Class(**val)
        elif attr == 'inventory':
            for i, item in enumerate(val):     
                val[i] = create_item(item)
            
        p.__setattr__(attr, val)
    return p

