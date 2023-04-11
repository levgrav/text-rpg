from controllers.setup.player_setup import player_setup
from controllers.setup.world_setup import world_setup
import controllers.command_center.command_center as cc

def setup():
    cc.set_layout("Main Menu")
    while True:
        event, values = cc.get_event_values()
        if event in ['New Game', 'Load Game', 'Main Menu']:
            cc.set_layout(event)
        elif event == 'Quit':
            return (None, None), True
        elif event == 'Load':
            world, player = load(values['-SAVED_GAMES-'][0])
            return (world, player), False
        elif event == 'New':
            world, player = new(values['Name'])  # type: ignore
            return (world, player), False
        

def load(savename):
    return player_setup(savename), world_setup(savename)

def new(playername):
    w, p = world_setup(), player_setup() 
    p.name = playername
    return w, p

