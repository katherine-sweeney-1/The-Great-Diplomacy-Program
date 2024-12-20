
from Class_Command import Command

def run_commands(commands_starting_data):   #nested dictionary
    cmds_list = []
    print(commands_starting_data)
    for each_cmd in commands_starting_data: 
        cmd_info = commands_starting_data[each_cmd]
        #print(each_cmd, cmd_info)
        one_cmd = Command(each_cmd, cmd_info)
        #print(one_cmd.loc)
        one_cmd.print_statements()
        cmds_list.append(one_cmd)
    return cmds_list
    

