

"""

det_move is useful for later

need to write down everything to check first and decide functions/formatting

"""
def det_move(cmd_obj):
    print(" ")
    print("location {}, origin {}, destination {}".
          format(cmd_obj.loc.name, cmd_obj.origin.name, cmd_obj.dest.name))
    if cmd_obj.loc.name == cmd_obj.origin.name and cmd_obj.loc.name == cmd_obj.dest.name:       # if order is hold
         output = "hold"
    elif cmd_obj.loc.name == cmd_obj.origin.name and cmd_obj.loc.name != cmd_obj.dest.name:     # if order is attack
        output = "attack"
    elif cmd_obj.loc.name != cmd_obj.origin.name:                                     # if order is support
        if cmd_obj.origin.name == cmd_obj.dest.name:                                  # if order is support a hold
            output = "support hold"
        elif cmd_obj.origin.name != cmd_obj.dest.name:                                # if order is support an attack
            output = "support attack"
    else:
        output = "possible convoy"  
    return output

def run_check_legal (all_cmds):
    for each_cmd in all_cmds:
        is_legal = det_move(each_cmd)
        print(is_legal)
    