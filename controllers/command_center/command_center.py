import os

def set_io_outlet(io_outlet):
    global io
    if io_outlet == 'terminal':
        import controllers.command_center.terminal as io
    elif io_outlet == 'gui':
        import controllers.command_center.GUI as io
    else:
        raise NotImplementedError(f'io_outlet: {io_outlet}') 

def get_command():
    return io.get_command()  

def main_menu():
    return io.main_menu()