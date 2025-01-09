import sys
import os

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Commander"))
from Class_Commander import Commander
from Hard_Data_Commanders import cmdrs_data_1 as cmdrs_data

from Class_Command import Command

def get_commander(cmd_unit):
    for indiv_cmdr in cmdrs_data:
        cmdr_info = cmdrs_data[indiv_cmdr]
        indiv_cmdr_obj = Commander(indiv_cmdr, cmdr_info)
        if cmd_unit.id in indiv_cmdr_obj.unit_members:                   # check if unit belongs to any country
            cmdr_obj = indiv_cmdr_obj
            break
        else:
            continue
    return cmdr_obj

def create_commands(commands_starting_data):   # function uses nested dictionary data
    cmds_dict = {}
    for each_cmd in commands_starting_data: 
        cmd_info = commands_starting_data[each_cmd]
        one_cmd = Command(each_cmd, cmd_info)
        command_unit = one_cmd.get_unit_obj()
        commander = get_commander(command_unit)
        one_cmd.get_loc_node()
        one_cmd.get_origin_node()
        one_cmd.get_dest_node()
        one_cmd.validate_human(commander)
        #one_cmd.print_statements()
        cmds_dict[one_cmd.unit.id] = one_cmd
    return cmds_dict
    
