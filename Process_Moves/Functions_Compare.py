def check_other_attacks(command_id, command, commands, destination_command_id):
    # get a dictionary without the command to check if there are other attacking commands
    dictionary_without_command = commands.copy()
    dictionary_without_command.pop(command_id)
    # remove the command for the unit on the destination
    if destination_command_id != False:
        dictionary_without_command.pop(destination_command_id)
    # check if another command attacks the same destination as the command in question
    for other_command_id in dictionary_without_command:
        other_command = dictionary_without_command[other_command_id]
        # another attack on destination => check other attacks

        if other_command.destination == command.destination:
            if other_command.origin != command.origin:
                if command.strength > other_command.strength:
                    outcome = True
                else:
                    if command.strength > other_command.strength:
                        outcome = True
                    elif command.strength == other_command.strength and command.location == command.destination:
                        outcome = True
                    else:
                        outcome = False
                        break
            else:
                outcome = True
        else:
            outcome = True
    command.success(outcome)
    return command.succeed



def check_other_attacks(command_id, command, commands, destination_command_id):
    # get a dictionary without the command to check if there are other attacking commands
    dictionary_without_command = commands.copy()
    dictionary_without_command.pop(command_id)
    # remove the command for the unit on the destination
    if destination_command_id != False:
        dictionary_without_command.pop(destination_command_id)
        for other_command_id in dictionary_without_command:
            other_command = dictionary_without_command[other_command_id]


            if other_command.location == commands[destination_command_id].destination:
                #print(command_id, other_command.unit.id)
                #outcome = check_if_other_attack_is_on_destination(command_id, command, other_command)
                #print("YES", command_id, outcome)
                outcome = True
                break
            else:
                #print(command_id, other_command_id)
                outcome = check_if_other_attack_is_on_destination(command_id, command, other_command)
                #print(command_id, outcome)
                if outcome == False:
                    break
    # check if another command attacks the same destination as the command in question
    else:
        for other_command_id in dictionary_without_command:
            other_command = dictionary_without_command[other_command_id]
            # another attack on destination => check other attacks
            outcome = check_if_other_attack_is_on_destination(command_id, command, other_command)
            if outcome == False:
                break
    command.success(outcome)
    return command.succeed