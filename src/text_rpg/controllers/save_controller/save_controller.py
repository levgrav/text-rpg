import shelve
import os

def save(world, player):
    player_name = player.name
    
    try:
        os.mkdir(f"files/game_data/saves/{player_name}")
    except FileExistsError:
        pass
    
    with shelve.open(f"files/game_data/saves/{player_name}/{player_name}") as f:
        f["player"] = player
        f["world"] = world
        f.close()

def load(player_name):
    with shelve.open(f"files/game_data/saves/{player_name}/{player_name}") as f:
        player = f["player"]
        world = f["world"]
        f.close()
    
    return world, player