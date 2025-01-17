
from Class_Command import Command

def create_commands(commands_starting_data, commanders, units, nodes):   # function uses nested dictionary data
    cmds_dict = {}
    for each_cmd in commands_starting_data: 
        cmd_info = commands_starting_data[each_cmd]
        one_cmd = Command(commands_starting_data[each_cmd]["country"])
        one_cmd.assign_cmdr(commands_starting_data[each_cmd]["owner"], commanders)
        one_cmd.assign_unit(each_cmd, units)
        one_cmd.assign_loc(commands_starting_data[each_cmd]["location"], nodes)
        one_cmd.assign_origin(commands_starting_data[each_cmd]["origin"], nodes)
        one_cmd.assign_destination(commands_starting_data[each_cmd]["destination"], nodes)
        cmds_dict[one_cmd.unit] = one_cmd
    return cmds_dict
    
