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
                # if another unit affects the supporting unit
                if command.location == commands[other_id].destination:
                    # check if the affecting command is an attack
                    if commands[other_id].location == commands[other_id].origin:
                        # check if command supports an attack on the unit trying to cut support
                        if command.destination == commands[other_id].location:
                            print("check ", command_id, other_id)
                            # recursion attempt
                            
                            supported_attack_outcome = check_supported_attack_on_support(commands, command_id, other_id, True)
                            if supported_attack_outcome:
                                command_success = True
                                
                            else:
                                command_success = False
                                break
                                


                            #print("test 2", unit_id, other_unit)
                            #command_success = True
                        else:
                            command_success = False
                            break
                    else:
                        command_success = True
                else:
                    command_success = True
                
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
def check_supported_attack_on_support(commands, command_id, recursion_boolean):
    for pot_other_support in commands:
        if commands[pot_other_support].location != commands[pot_other_support].origin and commands[pot_other_support].origin != commands[pot_other_support].destination:
            if command_id == "FR03":
                    print("yes 0")
            if commands[command_id].location != commands[pot_other_support].destination:
                if command_id == "FR03":
                    print("yes 1")
                command_success = True
            if recursion_boolean:
                if command_id == "FR03":
                    print("yes 2", command_id, pot_other_support)
                    
                command_success = True
                break
            else:
                if command_id == "FR03":
                    print("yes 3")
                other_success = get_valid_support(commands, command_id, True)
                print(other_success)
                if other_success:
                    command_success = False
                    break
                else:
                    command_success = True
                    break
        else:
            command_success = False
            #print("check 4", command_success)
            #continue
    return command_success
"""



"""
def check_supported_attack_on_support(commands, command_id, recursion_boolean):
    for pot_other_support in commands:
        if commands[command_id].location == commands[pot_other_support].destination:
            print(command_id, pot_other_support)
            if commands[pot_other_support].location != commands[pot_other_support].origin and commands[pot_other_support].origin != commands[pot_other_support].destination:
                if commands[command_id].location != commands[pot_other_support].destination:
                    command_success = True
                if recursion_boolean:  
                    command_success = True
                    break
                else:
                    other_success = get_valid_support(commands, command_id, True)
                    if other_success:
                        command_success = False
                        break
                    else:
                        command_success = True
                        break
            else:
                print(command_id, pot_other_support)
                command_success = False
        else:
            continue
    return command_success
"""


def check_supported_attack_on_support(commands, command_id, other_id, recursion_boolean):
    for pot_other_support in commands:
        # if there is support on the 
        if other_id != pot_other_support:
            #print("yes")
            # if another command affects the supporting command
            if commands[command_id].location == commands[pot_other_support].destination:
                # if the other command is not a hold 
                if commands[pot_other_support].location != commands[pot_other_support].origin:
                    print(1, command_id, pot_other_support)
                    # if the other command is a support --> determine outcomes
                    if commands[pot_other_support].location != commands[pot_other_support].origin:
                        print(2, command_id, pot_other_support)
                        if commands[command_id].location != commands[pot_other_support].destination:
                            command_success = True
                        if recursion_boolean:  
                            command_success = True
                            break
                        else:
                            other_success = get_valid_support(commands, command_id, True)
                            if other_success:
                                command_success = False
                                break
                            else:
                                command_success = True
                                break
                    # if the other command is an attack
                    else:
                        command_success = True
                        break
                # if the other command is a hold
                else:
                    print(command_id, pot_other_support)
                    command_success = False
            else:
                continue
        else:
            command_success = True
    return command_success

"""
def check_supported_attack_on_support(commands, command_id, recursion_boolean):
    for pot_other_support in commands:
        # if another command affects the supporting command
        if commands[command_id].location == commands[pot_other_support].destination:
            # if the other command is not a hold 
            if commands[pot_other_support].location != commands[pot_other_support].origin:
                print(1, command_id, pot_other_support)
                # if the other command is a support --> determine outcomes
                if commands[pot_other_support].location != commands[pot_other_support].origin:
                    print(2, command_id, pot_other_support)
                    if commands[command_id].location != commands[pot_other_support].destination:
                        command_success = True
                    if recursion_boolean:  
                        command_success = True
                        break
                    else:
                        other_success = get_valid_support(commands, command_id, True)
                        if other_success:
                            command_success = False
                            break
                        else:
                            command_success = True
                            break
                # if the other command is an attack
                else:
                    command_success = True
                    break
            # if the other command is a hold
            else:
                print(command_id, pot_other_support)
                command_success = False
        else:
            continue
    return command_success
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
                #if command_id == "AU03":
                 #   print(command_id, commands[command_id].location.name, commands[command_id].origin.name, commands[command_id].destination.name)
                  #  print(other_id, commands[other_id].location.name, commands[other_id].origin.name, commands[other_id].destination.name)
                if command.location == commands[other_id].destination and commands[other_id].location == commands[other_id].origin:
                    # check if cut attempt has its own support
                    print(" oooooooooo")
                    command_success = check_cut_attempt_on_support(commands, command_id, other_id)
                    #break
                #else:
                    #print("uhhh", command_id)
                    #command_success = True
                    #if command_success_real == False:
                     #   command_success = False
                    #else:
                        #command_success = True
                    #if command_id == "AU03":
                     #   print("testing 2", command_id, command_success)
                if command_success == False:
                    break
        print(command_id, command_success, "bitch")
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


def is_support_for_attacking_cut(commands, command_id, other_id):
    for supported_attack in commands:
        #if command_id == "RU03":
        #if supported_attack != command_id and supported_attack.destination 
        print("command id", command_id, commands[command_id].origin.name, commands[command_id].destination.name)
        print("supported attack", supported_attack, commands[supported_attack].origin.name, commands[supported_attack].destination.name)
        if supported_attack != command_id and supported_attack != other_id:
            if commands[supported_attack].origin == commands[command_id].origin and commands[supported_attack].destination == commands[command_id].destination and commands[supported_attack].destination == commands[other_id].location:
                print("YEEESSSS")
                print(command_id, other_id, supported_attack)
                command_success = True
                break
            else:
                command_success = False
        else:
            command_success = False
            #break
        if command_id == "RU10":
            print("testing 1", command_id, command_success)
    return command_success

# check if the support is cut
def check_cut_attempt_on_support(commands, command_id, other_id):
    for cutting_support_id in commands:
        # if the cut attempt has its own support
        if commands[cutting_support_id] != (commands[command_id] and commands[other_id]) and commands[cutting_support_id].origin == commands[other_id].origin and commands[cutting_support_id].destination == commands[other_id].destination:
            print(" check test 2", command_id, other_id, cutting_support_id)
            for cut_on_supporting_cut in commands:
                if commands[cut_on_supporting_cut].location == commands[other_id].destination:
                    cutting_support_outcome = False
                    command_success = cutting_support_outcome
                    break
                else:
                    cutting_support_outcome = True
                    command_success = cutting_support_outcome
        # if the cut attempt does not have support
        else:
            #command_success = True
            #print("testing", command_success)
            print("  ")
            # if support is for an attack on cut attempt
            command_success = is_support_for_attacking_cut(commands, command_id, other_id)
            if command_success == False:
                print("testing", command_id, command_success)
                print("  1")
                break
            else:
                print("testing", command_success)
                print("  2")
                continue
    print(command_id, command_success, "shit")
    return command_success