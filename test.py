import controllers.command_center.command_center as command_center
import controllers.output_controller.output_controller as output_controller
import controllers.parser.parser as parser
import controllers.setup.world_setup as world_setup
import controllers.setup.player_setup as player_setup
import controllers.world_controller.world_controller as world_controller
from processing.functions import explore
import json

def main():
    p = player_setup.player_setup()
    print(p.stats) # type: ignore
if __name__ == '__main__':
    main()