from controllers.setup.player_setup import player_setup
from controllers.setup.world_setup import world_setup
from controllers.output_controller.output_controller import output_player 

def setup(mm):
    match mm:
        case 'new game':
            world = world_setup()
            player = player_setup()
            name = input("What is your character's name?\n> ")
            player.__setattr__("name", name)
            output_player(player)
            return world, player
        case 'load game':
            name = input("What is your character's name?\n> ")
            world = world_setup(name)
            player = player_setup(name)
            output_player(player)
            return world, player
        case 'exit':
            exit()
        case _:
            print('what?')
            exit()