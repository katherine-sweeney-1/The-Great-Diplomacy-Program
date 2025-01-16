
def filter_unit_type(commands):
    for each_cmd in commands:
        filter_value = 1
        #print("test", each_cmd)
        cmd = commands[each_cmd]
        # armies cannot have sea destinations
        #print("unit type", cmd.unit.type)
        #print("destination type")
        if cmd.unit.type == "army":
            if cmd.destination.node_type == "Sea":
                filter_value = 0
        # fleets cannot have inland destinations
        else:
            if cmd.destination.node_type == "Land":
                filter_value = 0
        print(each_cmd.id, filter_value)
        cmd.legal_command(filter_value)
    return commands
        