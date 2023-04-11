"""
test
~~~~
File used for testing different sparts of the program individualy"""

import controllers.command_center.command_center as command_center
import controllers.output_controller.output_controller as output_controller
import controllers.parser.parser as parser
import controllers.setup.world_setup as world_setup
import controllers.setup.player_setup as player_setup
import controllers.world_controller.world_controller as world_controller
import controllers.world_controller.player_functions as pfun
from processing.functions import explore, disp_obj
from processing.classes import Class
import json

def main():
    """Code to test goes here
    
    Parameters:
        whatever you want

    Returns: 
        Whatever you want"""
    
    p = player_setup.player_setup()
    
if __name__ == '__main__':
    main()