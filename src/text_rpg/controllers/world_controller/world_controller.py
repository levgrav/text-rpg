import controllers.world_controller.player_functions as player_functions

def update_world(player, world, intent, entities):
    if intent == 'quit':
        quit()
    elif intent == None or intent == 'invalid_prompt':
        return world, 'Invalid Command'
    else:
        try: 
            return player_functions.__dict__[intent](player, world, *entities)
        except TypeError:
            return world, 'Invalid Command'

