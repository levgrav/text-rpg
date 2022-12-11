import controllers.command_center.command_center as command_center
import controllers.output_controller.output_controller as output_controller
import controllers.parser.parser as parser
from controllers.setup.world_setup import world_setup
from controllers.setup.player_setup import player_setup
import controllers.world_controller.world_controller as world_controller

def main():
    mm = command_center.main_menu()
    world = world_setup()
    player = player_setup()
    while True:
        command = command_center.get_command()
        intent_pkg = parser.get_intent_command(command)
        world = world_controller.update_world(player, world, *intent_pkg)
        output_controller.output_all(world)

if __name__ == '__main__':
    main()