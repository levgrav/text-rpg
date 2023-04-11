import json
import os
from PySimpleGUI import (
    Text, Input, Combo, 
    OptionMenu, Multiline, 
    Output, Radio, Checkbox, 
    Spin, Button, Image, 
    Canvas, Column, Frame, 
    Tab, TabGroup, Pane, 
    Graph, Slider, Listbox, 
    Menu, MenubarCustom, 
    ButtonMenu, Titlebar, 
    ProgressBar, Table, 
    Tree, VerticalSeparator, 
    HorizontalSeparator, 
    StatusBar, Sizegrip, 
    Push, VPush, Sizer, 
    Window, theme, 
    WIN_CLOSED)

layouts_file_path = "game_data/gui_layouts.json"
SW, SH = Window.get_screen_size()
current_layout = ""
window = Window("")

class File_Listbox(Listbox):
    def __init__(self, folder_path, **kwargs):
        files = os.listdir(folder_path)
        values = [file.split(".")[0] for file in files]
        super().__init__(values, **kwargs)

def set_layout(layout):
    global window, current_layout
    current_layout = layout
    window = Window(layout, layout_from_json(layout), size=(SW, SH), no_titlebar=True)


def layout_from_json(layout_name: str):
    with open(layouts_file_path, "r") as l:
        layouts_dict = json.load(l)
    for _layout_name, layout_data in layouts_dict.items():
        if layout_name == _layout_name:
            break
    else:
        return []
    
    return objectify(layout_data)
            
def objectify(x):
    if isinstance(x, (list, tuple)):
        for i, e in enumerate(x):
            x[i] = objectify(e) # type: ignore
    if isinstance(x, dict):
        attrs = {}
        Class_Type = globals()[x["instanceof"]]
        for kw, arg in x['attrs'].items():
            attrs[kw] = objectify(arg)
            
        x = Class_Type(**attrs)
    return x

def get_event_values():
    event, values = window.read()  # type: ignore
    if event == WIN_CLOSED: event = 'Quit'
    return event, values

def set_output_text(text: str):
    if current_layout == 'Game Page':
        window['Output'].update(text) # type: ignore
    else:
        pass

def get_command():
    command = None
    while command == None:
        event, values = get_event_values()
        if event == 'Enter':
            command = values['Input']
            window['Input'].update("")  # type: ignore
        elif event == 'Quit':
            command = 'quit'
    
    return command

if __name__ == "__main__":
    theme('DarkAmber')
    set_layout("Main Menu")
    while True:
        event, values = window.read()  # type: ignore
        if event in ['New Game', 'Load Game', 'Main Menu']:
            set_layout(event)
        elif event == 'Quit' or event == WIN_CLOSED:
            # Exit the game
            break
        elif event in ['Load', 'New']:
            set_layout("Game Page")
        elif event == 'Enter':
            window['Output'].update("Player Name\n  name: Player Name\n  referrals: []\n  species: Human\n  description: \n  current_room: ['Village']\n  inventory: ['sword']\n  equipped: \n    head: None\n    chest: None\n    primary: None\n    secondary: None\n    boots: None\n  stats: \n    maxhp: 100\n    hp: 100\n    xp: 0\n    hunger: 100\n    max_cap: 20") # type: ignore
            window['Input'].update("") # type: ignore
        
        print([event, values])
            
    # Close the main menu window
    window.close()