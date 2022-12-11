from ascii_text11x7 import printBig
import os
import controllers.command_center.GUI as GUI

gui = None

def get_command(io_outlet = 'terminal'):
    if io_outlet == 'terminal':
        return get_command_terminal()

    elif io_outlet == 'gui': 
        return get_command_gui()

    else:
        raise NotImplementedError(f'io_outlet: {io_outlet}')    

def get_command_terminal():
    try:
        os.system('cls')
        return input("> ")
    except KeyboardInterrupt:
        print('exit')
        return 'exit'

def get_command_gui():
    global gui
    if gui == None:
        gui = GUI.GUI()
    gui.show_frame('InputPage')
    return gui.get_input()


def main_menu(io_outlet = 'terminal'):
    if io_outlet == 'terminal':
        main_menu_terminal()

    elif io_outlet == 'gui':
        main_menu_gui()

def main_menu_terminal():    
    try:
        os.system('cls')
        printBig("Main Menu")
        
        i = input("new game | load game | exit \n")
        if i != 'new game' and i != 'load game' and i != 'exit':
            i = main_menu_terminal()
            
        return i
    
    except KeyboardInterrupt:
        print('exit')
        return 'exit'

def main_menu_gui():
    global gui
    if gui == None:
        gui = GUI.GUI()
    gui.show_frame('MainMenu')
    return gui.get_input()

