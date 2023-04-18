from resources.entities.player.player_class import Player, create_player
from controllers.save_controller.save_controller import load
import json
import os

def player_setup():
    with open('files/game_data/default_player.json') as f:
        player_dict = json.load(f)
    return create_player(player_dict)