"""
main
~~~~
Main file that is run when you want to run the game.
`> python (dir)/main.py`
Will also be the main one run when program is turned into executable"""

# --- Imports --- # 
import controllers.command_center.command_center as command_center
import controllers.output_controller.output_controller as output_controller
import controllers.parser.parser as parser
import controllers.world_controller.world_controller as world_controller
import controllers.gpttools.describe_gpt as describe_gpt
import json
import os
from controllers.setup.setup import setup
from controllers.save_controller.save_controller import save


# --- Main Function --- # 
def main():
    """Function that is called when the program runs. 
    Contains some setup and the main loop.
    Command Center -> Parser -> Command Controller -> World Updater -> Outputs
    """
    # --- Setup --- # 
    # Load settings
    with open('files/game_data/settings.json') as s:
        settings = json.load(s)
    
    # Use settings
    command_center.set_io_outlet(settings['io_outlet'])
    parser.enable_parse_gpt(settings['enable_parse_gpt'])
    command_center.io.theme(settings['theme'])
    
    # Main Menu -> world and player setup
    (world, player), done = setup()
    
    # makes the game page display
    command_center.set_layout("Game Page")
    
    # --- Main Loop --- # 
    while not done: # Loop is broken from within functions for now
        command = command_center.get_command()
        intent_pkg = parser.get_intent_command(command, player, world)
        world, msg, done = world_controller.update_world(player, world, *intent_pkg)
        print(msg)
        if settings['enable_describe_gpt']: msg = describe_gpt.describe(intent_pkg, msg)
        output_controller.output_all(world, msg)
    
    save(world, player)
    print("Saved")

# --- Run Program --- #
# if __name__ == '__main__':
main()

