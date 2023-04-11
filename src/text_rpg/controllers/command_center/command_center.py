import os
import controllers.command_center.terminal as t
set_layout = t.set_layout
get_event_values = t.get_event_values
get_command = t.get_command
set_output_text = t.set_output_text



def set_io_outlet(io_outlet):
    global io
    if io_outlet == 'terminal':
        import controllers.command_center.terminal as io
    elif io_outlet == 'gui':
        import controllers.command_center.gui as io
    else:
        raise NotImplementedError(f'io_outlet: {io_outlet}') 


    global set_layout
    set_layout = io.set_layout    
    global get_event_values
    get_event_values = io.get_event_values  
    global get_command
    get_command = io.get_command
    global set_output_text
    set_output_text = io.set_output_text