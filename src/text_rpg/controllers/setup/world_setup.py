from resources.world.world_class import World, create_world
import json

def world_setup():
    with open("files/game_data/default_world.json") as f:
        world_dict = json.load(f)

    return create_world(world_dict)

    
