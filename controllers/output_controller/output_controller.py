import processing.functions as pfun

def output_all(world, msg):
    print(msg)

def output_player(player):
    print("\n---------------------------")
    print(pfun.disp_obj(player, "name"))
    print("---------------------------\n")