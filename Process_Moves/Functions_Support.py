
def get_valid_support(commands, id = None, recur_bool = None):
    for command_id in commands:
        # if a unit is attacking
        if commands[command_id].location == commands[command_id].origin:
            continue
        command = commands[command_id]
        # if a unit is supporting
        if command.location != command.origin:
            for cut_attempt in commands:
                # use parent nodes for processing supports
                if "-" in commands[cut_attempt].destination.name:
                    commands[cut_attempt].destination = commands[cut_attempt].destination.parent
                command_success = True
                # check if unit supports an attack on support's brethren units
                if command.destination.is_occupied:
                    if command.destination.is_occupied.id in command.human.unit_members.keys():
                        if command.origin != command.destination:
                            command_success = False
                            break
                # check if support is for an attack on support's brethern units
                            #if commands[cut_attempt]
                # check if there is an attempt to cut support
                #print(command_id, command.location.name, commands[cut_attempt].destination.name)
                #print(command_id, cut_attempt, commands[cut_attempt].location.name, commands[cut_attempt].origin.name)
                if command.location == commands[cut_attempt].destination and commands[cut_attempt].location == commands[cut_attempt].origin:
                    # check if cut attempt has its own support
                    command_success = check_cut_attempt_on_support(commands, command_id, cut_attempt)
                if command_success == False:
                    break
        # if the support affects another command (ie if there is a unit on the origin), get the supported command
        if command_success and command.origin.is_occupied != False:
            # get supported command for coastal territory
            if command.origin.is_occupied == 1:
                origin = command.origin
                for potential_supported_id in commands:
                    if commands[potential_supported_id] == origin:
                        supported_command_id = commands[potential_supported_id].origin.is_occupied.id
                        break
            # get supported command for non-coastal territory
            else:
                supported_command_id = command.origin.is_occupied.id
            supported_command = commands[supported_command_id]
            # assign strength to the supported command
            if supported_command_id in commands:
                if supported_command.location != command.location:
                    if command.origin and supported_command.origin and supported_command.destination == command.destination:
                        command_strength = 1
                        supported_command.cmd_strength(command_strength)
                    elif supported_command.origin != supported_command.destination and supported_command.location != supported_command.origin:
                        command_strength = 1
                        supported_command.cmd_strength(command_strength)
                    elif supported_command.origin == supported_command.destination and supported_command.location != supported_command.origin:
                        command_strength = 1
                        supported_command.cmd_strength(command_strength)
                    
                    else:
                        command_strength = 0
                else:
                    command_strength = 0
            else:
                command_strength = 0
        # strength of zero if the supporting command does not affect another command
        else:
            command_strength = 0
        command.success(command_success)
    return commands



"""

def get_valid_support(commands, id = None, recur_bool = None):
    for command_id in commands:
        # if a unit is attacking
        if commands[command_id].location == commands[command_id].origin:
            continue
        command = commands[command_id]
        print(command_id)
        # if a unit is supporting
        if command.location != command.origin:
            print("test 1", command_id)
            cut_count = 1
            for cut_attempt in commands:
                cut_count += 1
                command_success = True
                if command.destination.is_occupied:
                    print("test 2", command_id)
                    if command.destination.is_occupied.id in command.human.unit_members.keys():
                        print("test 2.5", command_id)
                        if command.origin != command.destination:
                            command_success = False
                            break
                # check if support is for an attack on support's brethern units
                            #if commands[cut_attempt]
                # check if there is an attempt to cut support
                if command.location == commands[cut_attempt].destination and commands[cut_attempt].location == commands[cut_attempt].origin:
                    # check if cut attempt has its own support
                    command_success = check_cut_attempt_on_support(commands, command_id, cut_attempt)
                if command_success == False:
                    break
        # if the support affects another command (ie if there is a unit on the origin), get the supported command
        if command_success and command.origin.is_occupied != False:
            # get supported command for coastal territory
            if command.origin.is_occupied == 1:
                origin = command.origin
                for potential_supported_id in commands:
                    if commands[potential_supported_id] == origin:
                        supported_command_id = commands[potential_supported_id].origin.is_occupied.id
                        break
            # get supported command for non-coastal territory
            else:
                supported_command_id = command.origin.is_occupied.id
            supported_command = commands[supported_command_id]
            # assign strength to the supported command
            if supported_command_id in commands:
                if supported_command.location != command.location:
                    if command.origin and supported_command.origin and supported_command.destination == command.destination:
                        command_strength = 1
                        supported_command.cmd_strength(command_strength)
                    elif supported_command.origin != supported_command.destination and supported_command.location != supported_command.origin:
                        command_strength = 1
                        supported_command.cmd_strength(command_strength)
                    elif supported_command.origin == supported_command.destination and supported_command.location != supported_command.origin:
                        command_strength = 1
                        supported_command.cmd_strength(command_strength)
                    
                    else:
                        command_strength = 0
                else:
                    command_strength = 0
            else:
                command_strength = 0
        # strength of zero if the supporting command does not affect another command
        else:
            command_strength = 0
        command.success(command_success)
    return commands
"""






"""

def get_valid_support(commands, id = None, recur_bool = None):
    for command_id in commands:
        # if a unit is attacking
        if commands[command_id].location == commands[command_id].origin:
            continue
        command = commands[command_id]
        # if a unit is supporting
        if command.location != command.origin:
            for other_id in commands:
                command_success = True
                # check if there is an attempt to cut support
                if command.location == commands[other_id].destination and commands[other_id].location == commands[other_id].origin:
                    # check if cut attempt has its own support
                    command_success = check_cut_attempt_on_support(commands, command_id, other_id)
                if command_success == False:
                    break
        # if the support affects another command (ie if there is a unit on the origin), get the supported command
        if command_success and command.origin.is_occupied != False:
            # get supported command for coastal territory
            if command.origin.is_occupied == 1:
                origin = command.origin
                for potential_supported_id in commands:
                    if commands[potential_supported_id] == origin:
                        supported_command_id = commands[potential_supported_id].origin.is_occupied.id
                        break
            # get supported command for non-coastal territory
            else:
                supported_command_id = command.origin.is_occupied.id
            supported_command = commands[supported_command_id]
            # assign strength to the supported command
            if supported_command_id in commands:
                if supported_command.location != command.location:
                    if command.origin and supported_command.origin and supported_command.destination == command.destination:
                        command_strength = 1
                        supported_command.cmd_strength(command_strength)
                    elif supported_command.origin != supported_command.destination and supported_command.location != supported_command.origin:
                        command_strength = 1
                        supported_command.cmd_strength(command_strength)
                    elif supported_command.origin == supported_command.destination and supported_command.location != supported_command.origin:
                        command_strength = 1
                        supported_command.cmd_strength(command_strength)
                    
                    else:
                        command_strength = 0
                else:
                    command_strength = 0
            else:
                command_strength = 0
        # strength of zero if the supporting command does not affect another command
        else:
            command_strength = 0
        command.success(command_success)
    return commands
"""



def is_support_for_attacking_cut(commands, command_id, other_id):
    for supporting_attack in commands:
        if supporting_attack != command_id and supporting_attack != other_id and commands[supporting_attack].human == commands[command_id].human:
            # if the support is supporting an attack on the other_id's location
            if commands[supporting_attack].origin == commands[command_id].origin and commands[supporting_attack].destination == commands[command_id].destination and commands[supporting_attack].destination == commands[other_id].location:
                command_success = True
                break
            else:
                command_success = False
        else:
            command_success = False
    return command_success

# check if the support is cut
def check_cut_attempt_on_support(commands, command_id, other_id):
    for cutting_support_id in commands:
        # if the cut attempt (other_id) has its own support (cutting_support_id)
        if cutting_support_id != command_id and cutting_support_id != other_id and commands[cutting_support_id].origin:
            # check if the the support (cutting_support_id) supports the cut attempt's (other_id) attack
            if commands[other_id].origin == commands[cutting_support_id].origin and commands[cutting_support_id].destination == commands[other_id].destination:
                if commands[command_id].location == commands[cutting_support_id].destination:
                    command_success = False
                    break
                else:
                    command_success = True
        # if the cut attempt does not have support
        else:
            # if support is for an attack on cut attempt
            command_success = is_support_for_attacking_cut(commands, command_id, other_id)
            if command_success == False:
                break
            else:
                continue
    return command_success