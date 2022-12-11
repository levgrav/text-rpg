from resources.world.world_class import World, create_world
import json

def world_setup(filename = None) -> World:
    if not filename:
        filename = 'default_world'
    fp = f'C:/Users/levgr/OneDrive/Documents/Coding Projects/python_projects/text_based_adventure_game/the new version/saves/worlds/{filename}.json'
    
    with open(fp) as f:
        world_dict = json.load(f)

    return create_world(world_dict)

    
