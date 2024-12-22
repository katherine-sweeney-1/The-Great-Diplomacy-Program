

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
check that the unit is in the commander's members

make sure 
- no one makes moves for a different person
- no one makes moves for a non-owning country
- no one makes moves for a non-owning unit

"""
def get_cmdr (cmd_unit):
    for each_cmdr in cmdrs:
        cmdr_obj = cmdrs[each_cmdr]
        if cmd_unit in cmdr_obj.unit_members:                   # check if unit belongs to any country
            cmdr_person = each_cmdr
            break
        else:
            continue
    return cmdr_person, cmdr_obj

def validate_cmdr (cmd_obj, person, cmdr_obj):
    if cmd_obj.human == person:                         # if the person giving the cmd is the correct cmdr
        valid_person = True
    else:
        valid_person = False
    if cmd_obj.country == cmdr_obj.country:             # if command's affected unit is in the cmdr's country
        valid_country = True
    else:
        valid_country = False
    if valid_person == True and valid_country == True:
        valid_cmdr = True
    else:
        valid_cmdr = False
    return valid_cmdr



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
    for each_cmd_unit in all_cmds:
        command_obj = all_cmds[each_cmd_unit]
        #cmdr = get_cmdr(each_cmd_unit)
        cmdr_person, cmdr_obj = get_cmdr(each_cmd_unit)
        is_commander_valid = validate_cmdr(command_obj, cmdr_person, cmdr_obj)
        print("unit {} has commander {}".format(each_cmd_unit, cmdr_person))
        print("info", command_obj, is_commander_valid)
    