from resources.world.world_class import World, create_world
import json
import os
game_data_path = os.getcwd() + '\\game_data'

def world_setup(filename = None) -> World:
    
    if not filename:
        fp = 'default_world.json'
    else:
        fp = f'saves\\worlds\\{filename}.json'
    fp = f'{game_data_path}\\{fp}'
    
    with open(fp) as f:
        world_dict = json.load(f)

    return create_world(world_dict)

    
