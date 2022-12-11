from resources.entities.player.player_class import Player, create_player
import json

def player_setup(filename = None) -> Player:
    if not filename:
        filename = 'default_player'
    fp = f'C:/Users/levgr/OneDrive/Documents/Coding Projects/python_projects/text_based_adventure_game/the new version/saves/players/{filename}.json'
    
    with open(fp) as f:
        player_dict = json.load(f)        

    return create_player(player_dict)