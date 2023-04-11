from resources.entities.player.player_class import Player, create_player
import json
import os
game_data_path = os.getcwd() + '\\game_data'

def player_setup(filename = None) -> Player:
    
    if not filename:
        fp = 'default_player.json'
    else:
        fp = f'saves\\players\\{filename}.json'
    fp = f'{game_data_path}\\{fp}'
    
    with open(fp) as f:
        player_dict = json.load(f)        

    return create_player(player_dict)