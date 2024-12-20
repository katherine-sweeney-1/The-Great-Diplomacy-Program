
from Class_Command import Command

def run_commands(commands_starting_data):   #nested dictionary
    for each_cmd in commands_starting_data:
        cmd_info = commands_starting_data[each_cmd]
        print(each_cmd, cmd_info)
        one_cmd = Command(cmd_info)
        one_cmd.print_statements

