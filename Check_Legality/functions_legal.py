

"""

det_move is useful for later

need to write down everything to check first and decide functions/formatting

"""

import sys
import os 

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Commander"))
from Functions_Commander import create_commanders
from Hard_Data_Commanders import cmdrs_data_1

cmdrs = create_commanders(cmdrs_data_1)

"""

Armies can only move to inland/coast
Fleets can only move to sea/coast

Territories must be adjacent
- attacks must be adjacent unless there is a convoy
- support must be adjacent to the destination

"""

def unit_dest_type(cmd):                                                # unit type and dest type determine if move is legal
    if cmd.unit.type == "army":
        if cmd.dest.node_type == "Coast" or cmd.dest.node_type == "Land":         # legal if army goes to coast/inland
            is_dest_valid = True
        else:
            is_dest_valid = False
    else:
        if cmd.dest.node_type == "Coast" or cmd.dest.node_type == "Sea":          # legal if fleet goes to coast/sea
            is_dest_valid = True
        else:
            is_dest_valid = False       
    return is_dest_valid


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
"""


def run_check_legal (all_cmds):
    for one_cmd in all_cmds:
        #move_type = det_move(each_cmd)
        cmd_obj = all_cmds[one_cmd]
        is_dest_type_valid = unit_dest_type(cmd_obj)
        print(cmd_obj.unit.id, cmd_obj.loc.name, is_dest_type_valid)
    