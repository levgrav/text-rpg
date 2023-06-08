import controllers.world_controller.player_functions as player_functions

def update_world(player, world, command, args):
    if command == 'quit':
        return world, "quit", True
    elif command == None or command == 'invalid_prompt':
        return world, 'Invalid Command', False
    elif command == 'error':
        return world, 'Error', False
    else:
        try: 
            return *player_functions.__dict__[command](player, world, *args), False
        except TypeError:
            return world, 'Invalid Command', False
