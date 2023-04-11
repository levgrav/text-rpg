import os
from art import tprint

def theme(theme):
    pass

def get_command():
    try:
        return input("> ")
    except KeyboardInterrupt:
        print('exit')
        return 'exit'

def main_menu():    
    try:
        tprint("Main     Menu", font="big")
        
        i = input("new game | load game | exit \n> ")
        if i != 'new game' and i != 'load game' and i != 'exit':
            i = main_menu()

        return i
    
    except KeyboardInterrupt:
        print('exit')
        return 'exit'

def set_output_text(text: str):
    print(text)
    
def set_layout(*_):
    pass

def get_event_values(*_):
    pass