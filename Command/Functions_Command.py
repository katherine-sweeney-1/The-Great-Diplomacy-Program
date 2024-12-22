
from Class_Command import Command

def create_commands(commands_starting_data):   # function uses nested dictionary data
    cmds_dict = {}
    for each_cmd in commands_starting_data: 
        cmd_info = commands_starting_data[each_cmd]
        one_cmd = Command(each_cmd, cmd_info)
        one_cmd.get_unit_obj()
        one_cmd.get_loc_node()
        one_cmd.get_origin_node()
        one_cmd.get_dest_node()
        #one_cmd.print_statements()
        cmds_dict[one_cmd.unit.id] = one_cmd
    return cmds_dict
    

