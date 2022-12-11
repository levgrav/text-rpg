
def update_world(player, world, intent, entities):
    if intent == 'exit':
        exit()
    elif intent == None:
        print('Invalid Command')
    else:
        player.__getattribute__(intent)(world, entities)

