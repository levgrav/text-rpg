
def update_world(player, world, intent, entities):
    if intent == 'exit':
        exit()
    elif intent == None:
        return world, 'Invalid Command'
    else:
        return player.__getattribute__(intent)(world, *entities)

