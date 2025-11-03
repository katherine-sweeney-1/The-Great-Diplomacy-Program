# need to loop through and find all relevant attacks for check other attacks
# check other attacks only considers the first attack that's relevant
def check_other_attacks(command_id, command, commands, destination_command_id, count = None):
    # get a dictionary without the command to check if there are other attacking commands
    #dictionary_without_command = commands.copy()
    #dictionary_without_command.pop(command_id)
    #print("check", command_id)

    relevant_attacking_commands = {}
    # remove the command for the unit on the destination
    if destination_command_id != False:
        relevant_attacking_commands[command_id] = command
        #dictionary_without_command.pop(destination_command_id)
        for other_command_id in commands:
            if command_id != other_command_id:
                other_command = commands[other_command_id]
                """
                if command_id == "AU01":
                    print(command_id, other_command_id)
                    print(other_command.destination.name, commands[destination_command_id].destination.name)
                    print(other_command.location.name, other_command.origin.name)
                    print(" ")
                """
                if other_command.destination == commands[destination_command_id].location and other_command.location == other_command.origin:
                    if command_id == "AU01":
                        
                        print("YES", command_id, other_command_id)
                        print("Destination command", destination_command_id)
                        print("destination loc", commands[destination_command_id].location.name)
                        print("destination cmd's origin", commands[destination_command_id].origin.name)
                        print("destination cmd's destination", commands[destination_command_id].destination.name)
                        print(" ")
                        
                #if command_id != other_command_id:
                    relevant_attacking_commands[other_command_id] = commands[other_command_id]
            #else:
                #continue
        """
        
        issue - need to include scenario of

        albania attacking trieste with vienna attacking trieste

        when ionian wants to go to albania and albania and vienna attack trieste
        
        
        """
        if len(relevant_attacking_commands) > 0:
            #if command_id == "AU01":
                #print("TRUE")

            """
            if command_id == "TU02":
                print("test")
                print(command_id)
                print(relevant_attacking_commands)
                print(" ")
            """
            if command_id == "AU01":
                print(relevant_attacking_commands)
            for relevant_attack_id in relevant_attacking_commands:
                one_attacking_command = relevant_attacking_commands[relevant_attack_id]
                #print(one_attacking_command)
                #if one_attacking_command.destination == relevant_attacking_commands[relevant_attack_id].destination and relevant_attack_id.location == relevant_attack_id.origin:
                    #other_attacking_commands[other_command_id] = other_command
                if len(relevant_attacking_commands) > 1:
                    """
                    print("check")
                    print(command_id)
                    print(relevant_attacking_commands)
                    print(" ")
                    """
                    #relevant_attack_outcome = get_attack_outcome(relevant_attack_id, one_attacking_command, commands)
                    if count == None:
                        relevant_attack_outcome = check_other_attacks(relevant_attack_id, one_attacking_command, commands, destination_command_id, count = 1)
                    else:
                        #if one_attacking_command.location == command.destination and command.destination == one_attacking_command.location:
                        if command_id == "AU01":    
                            print("uhhhh", command_id)
                    
                        #relevant_attack_outcome = False
                        """
                        if one_attacking_command.location == command.destination and one_attacking_command.destination == command.location:
                            if command_id == "AU01":
                                print("Test 1")
                            relevant_attack_outcome = False
                        else:
                            if command_id == "AU01":
                                print("test 2")
                            relevant_attack_outcome = check_other_attacks(relevant_attack_id, one_attacking_command, commands, destination_command_id, count = 2)
                        """
                        
                        #else:
                            #print("yyyyyyyyyy")
                            #relevant_attack_outcome = check_other_attacks(relevant_attack_id, one_attacking_command, commands, destination_command_id, count = 2







                    if destination_command_id == relevant_attack_id:
                        if relevant_attack_outcome == False:
                            outcome = False
                            #print("check 1", command_id)
                            break
                    else:
                        if relevant_attack_outcome == False:
                            #print("check 2", command_id)
                            outcome = True
                        else:
                            #print("check 3", command_id)
                            outcome = False
                else:
                    #print("check 4", command_id)
                    outcome = True
                #print("CHECKING")
                #print(outcome)
        else:
            destination_command = commands[destination_command_id]
            outcome = check_if_other_attack_is_on_destination(command_id, command, other_command, destination_command)


    # check if another command attacks the same destination as the command in question
    else:
        #for other_command_id in dictionary_without_command:
            #other_command = dictionary_without_command[other_command_id]
        for other_command_id in commands:
            other_command = commands[other_command_id]
            # another attack on destination => check other attacks
            if command.destination.is_occupied:
                destination_unit_id = command.destination.is_occupied.id
                destination_command = commands[destination_unit_id]
                outcome = check_if_other_attack_is_on_destination(command_id, command, other_command, destination_command)
            else:
                outcome = check_if_other_attack_is_on_destination(command_id, command, other_command)
            if outcome == False:
                break
    command.success(outcome)
    command.checking_other_attacks(True)
    return command.succeed
