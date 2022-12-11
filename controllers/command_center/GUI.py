from controllers.command_center.GUI_class import GUI

gui = None

def get_command():
    global gui
    if gui == None:
        gui = GUI()
    gui.show_frame('InputPage')
    return gui.get_input()

def main_menu():
    global gui
    if gui == None:
        gui = GUI()
    gui.show_frame('MainMenu')
    return gui.get_input()
