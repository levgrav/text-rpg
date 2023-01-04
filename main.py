import controllers.command_center.command_center as command_center
import controllers.output_controller.output_controller as output_controller
import controllers.parser.parser as parser
from controllers.setup.setup import setup
import controllers.world_controller.world_controller as world_controller
import json
import os

with open(os.getcwd() + '\\game_data\\settings.json') as s:
    settings = json.load(s)

def main():
    command_center.set_io_outlet(settings['io_outlet'])
    parser.set_parser(settings['parser_type'])
    mm = command_center.main_menu()
    world, player = setup(mm)
    while True:
        command = command_center.get_command()
        intent_pkg = parser.get_intent_command(command, player, world)
        world, msg = world_controller.update_world(player, world, *intent_pkg)
        output_controller.output_all(world, msg)

if __name__ == '__main__':
    main()