import controllers.world_controller.player_functions as player_functions

def update_world(player, world, intent, entities):
    if intent == 'quit':
        return world, "quit", True
    elif intent == None or intent == 'invalid_prompt':
        return world, 'Invalid Command', False
    else:
        try: 
            return *player_functions.__dict__[intent](player, world, *entities), False
        except TypeError:
            return world, 'Invalid Command', False
