import sys
import os
sys.path.append(os.path.join("/The-Great-Diplomacy-Program/Nodes/Class_Sub_Node"))
from Class_Sub_Node import Coastal_Node

def check_other_attacks(command_id, command, commands, destination_command_id, count = None):
    #print(command_id, destination_command_id)
    # get a dictionary without the command to check if there are other attacking commands
    relevant_attacking_commands = {}
    #print("check other attacks", command_id, destination_command_id)
    # remove the command for the unit on the destination
    if destination_command_id != False:
        relevant_attacking_commands[command_id] = command
        destination_command = commands[destination_command_id]
        relevant_attacking_commands[destination_command_id] = destination_command
        #print("command", command_id)
        #print("destination command 1", destination_command_id)
        """
        for other_command_id in commands:
            if command_id != other_command_id and destination_command_id != other_command_id:
                other_command = commands[other_command_id]
                if other_command.destination == commands[destination_command_id].location and other_command.location == other_command.origin:
                    relevant_attacking_commands[other_command_id] = commands[other_command_id]
                elif other_command.location == commands[destination_command_id].destination and other_command.location == other_command.origin:
                    relevant_attacking_commands[other_command_id] = commands[other_command_id]
                #if other_command.destination == command.location and other_command.location == other_command.origin:
                    #relevant_attacking_commands[other_command_id] = commands[other_command_id]
        """
        relevant_attacking_commands = get_relevant_attacks(command_id, destination_command_id, commands, relevant_attacking_commands)
        last_relevant_attack = retrieve_last_relevant_attack(relevant_attacking_commands)
        #last_relevant_attack_outcome = get_attack_outcome (last_relevant_attack.unit.id, last_relevant_attack, commands)
        #print("LST RELEVANT ATTACK OUTCOME", last_relevant_attack_outcome)
        #print("last relevant attack", last_relevant_attack)
        """
        print(command_id)
        print("relative attacking commands")
        print(relevant_attacking_commands)
        print(" ")
        """
        # determine if command has a higher strength than other attacks
        if len(relevant_attacking_commands) > 2:
            print(relevant_attacking_commands)
            print(command_id)
            for relevant_attack_id in relevant_attacking_commands:
                one_attacking_command = relevant_attacking_commands[relevant_attack_id]
                if len(relevant_attacking_commands) > 3 and one_attacking_command != command:
                    """
                    print(" ")
                    print("TESTING", command_id)
                    print(" ")
                    """
                    if command.strength > one_attacking_command.strength:
                        outcome = True
                    else:
                        # if the destination command attacks one attacking command and if destination command beats one attacking command, then command wins
                        destination_command = commands[destination_command_id]
                        if destination_command.location == destination_command.origin and destination_command.destination == one_attacking_command.location:
                            if destination_command.strength > one_attacking_command.strength:
                                outcome = True
                            else:
                                outcome = False
                                break
                        else:
                            relevant_attack_outcome = get_attack_outcome(relevant_attack_id, one_attacking_command, commands)
                            if relevant_attack_outcome == False:
                                outcome = False
                                break
                            else:
                                outcome = True
                            print("TESTING 2")
                            print(command_id)
                            print(" ")
                             
                else:
                    destination_command = commands[destination_command_id]
                    outcome = check_if_other_attack_is_on_destination(command_id, command, one_attacking_command, destination_command)
        else:
            #print("TESTING 3", command_id)
            if destination_command.location == command.destination and destination_command.destination == command.location:
                if command.strength > destination_command.strength:
                    outcome = True
                else:
                    outcome = False
            else:
                last_relevant_attack = retrieve_last_relevant_attack(relevant_attacking_commands)
                if last_relevant_attack == None:
                    #print("TEST", command_id, destination_command_id)
                    if command.strength > destination_command.strength:
                        outcome = True
                    else:
                        outcome = False
                #print(" ")
                #print("TESTING 4")
                #print(command_id, destination_command_id, last_relevant_attack.unit.id)
                #print(" ")
                
                #outcome = True
                #if command == last_relevant_attack:
                    #print("TRUE", command.unit.id)
                    #outcome = True
                else:
                    
                    last_relevant_attack_outcome = get_attack_outcome (last_relevant_attack.unit.id, last_relevant_attack, commands)
                    #print("LST RELEVANT ATTACK OUTCOME", last_relevant_attack_outcome)
                    #print("last relevant attack", last_relevant_attack)
                    """
                    if outcome is false
                        if there's only two relevant attacks
                            if command.strength > last relevant attack.strength:
                                outocme = true
                            else:
                                outcome = false
                        else:
                            if command.strength
                    
                    """
                    if last_relevant_attack_outcome == False:
                        if command.strength > last_relevant_attack.strength:
                            outcome = True
                        else:
                            outcome = False
                        #print(command_id, "outcome for if statement", outcome)
                    else:
                        outcome = True
                        #print(command_id, "outcome for else statement", outcome)
                    #outcome = last_relevant_attack_outcome
                    #print(command_id, "outcome", outcome)
            #destination_command = commands[destination_command_id]
            #outcome = check_if_other_attack_is_on_destination(command_id, command, other_command, destination_command)
    # check if another command attacks the same destination as the command in question
    else:
        for other_command_id in commands:
            other_command = commands[other_command_id]
            # another attack on destination => check other attacks
            if command.destination.is_occupied:
                destination_unit_id = command.destination.is_occupied.id
                destination_command = commands[destination_unit_id]
                outcome = check_if_other_attack_is_on_destination(command_id, command, other_command, destination_command)
            else:
                # error with check if other attack is on destination function
                outcome = check_if_other_attack_is_on_destination(command_id, command, other_command)
            if outcome == False:
                break
    command.success(outcome)
    command.checking_other_attacks(True)
    return command.succeed

def check_if_other_attack_is_on_destination(command_id, command, other_command, destination_command = None):
    #if command_id == "RU01" or command_id == "RU05":
     #   print(command_id, "check if other attack is on destination")
    if other_command.destination == command.destination:
        # if the other command is attacking
        if other_command.origin != command.origin:
            # if the other command is attacking on an occupied territory
            if destination_command != None:
                # if the destination command is being attacked by other command and is not attacking (i.e. hold or support)
                if destination_command.destination == other_command.origin and destination_command.origin == destination_command.location:
                    if other_command.strength >= destination_command.strength:
                        outcome = False
                    else:
                        outcome = True
                else:
                    if command.strength > other_command.strength:
                        outcome = True
                    else:
                        outcome = False
            else:
                """
                code might be redundant here
                """
                if command.strength > other_command.strength:
                    outcome = True
                else:
                    if command.strength > other_command.strength:
                        outcome = True
                    elif command.strength == other_command.strength and command.location == command.destination:
                        outcome = False
                    else:
                        outcome = False
        else:
            outcome = True
    else:
        outcome = True
    return outcome

def get_attack_outcome(command_id, command, commands, count = None):
    #print(command_id, command.strength)
    if command.destination.is_occupied != False:
        # get the command for the unit on the destination
        destination_command_id, destination_command = get_destination(command, commands)
        # if the unit on the destination is attacking 
        if destination_command.location == destination_command.origin and destination_command.destination != destination_command.origin:
            #print(command_id)
            # if the command and unit on destination are trying to attack each other
            if command.location == destination_command.destination and command.destination == destination_command.location:
                outcome = False
                destination_command_outcome = False
            # if they're not attacking each other, get the outcome for the command on the destination
            else:
                #print(command_id, destination_command_id)
                if count == None:
                    destination_command_outcome = get_attack_outcome(destination_command_id, destination_command, commands, count = 1)
                else:
                    if destination_command.location == command.destination and destination_command.destination == command.location:
                        destination_command_outcome = False
                    elif destination_command.destination != command.location:
                        destination_command_outcome = True
                    else:
                        destination_command_outcome = get_attack_outcome(destination_command_id, destination_command, commands, count = 2)
            # if destination's command is successful, check for other attacks on the destination
            if destination_command_outcome:
                #print(command_id)






                other_attacks_on_destination_outcome = check_other_attacks(command_id, command, commands, destination_command_id)
                #print(other_attacks_on_destination_outcome)
                if other_attacks_on_destination_outcome == True:
                    outcome = True
                else:
                    if command.strength > destination_command.strength:
                        outcome = True
                    else:
                        outcome = False
            # if the destination's command is not successful, check the strength of the command and destination command
            # ensure the commands have different commanders
            else:
                if command.strength > destination_command.strength:
                    outcome = check_commanders(command_id, command, commands, destination_command)
                else:
                    outcome = False
        # if the unit on the destination is not attacking, check the strength to see if the unit is dislodged
        # ensure the commands have different commanders 
        else:
            #print("check", command_id, destination_command.unit.id)
            if command.strength > destination_command.strength:
                outcome = check_commanders(command_id, command, commands, destination_command)
            else:
                """
                problem is in this area of code
                """
                
                #if command.strength > destination_command.strength:
                #    outcome = check_commanders(command_id, command, commands, destination_command)
                #else:
                """
                    print(command_id)
                    if count == None:
                        print("test 1", command_id)
                        destination_command_outcome = get_attack_outcome(destination_command_id, destination_command, commands, count = 1)
                        print("Destination command outcome", destination_command_outcome)
                    else:
                        print("Test 2", command_id)
                        if destination_command.location == command.destination and destination_command.destination == command.location:
                            destination_command_outcome = False
                        else:
                            destination_command_outcome = get_attack_outcome(destination_command_id, destination_command, commands, count = 2)
                        print("dest outcome", command_id, destination_command_outcome)
                    if destination_command_outcome:
                        print("test", command_id)
                        other_attacks_on_destination_outcome = check_other_attacks(command_id, command, commands, destination_command_id)
                        if other_attacks_on_destination_outcome == True:
                            outcome = True
                        else:
                            if command.strength > destination_command.strength:
                                outcome = True
                            else:
                                outcome = False
                    else:
                        if command.strength > destination_command.strength:
                            outcome = check_commanders(command_id, command, commands, destination_command)
                        else:
                            outcome = False
                    """
                outcome = False
                #print("YES", command_id)
    else:
        outcome = check_other_attacks(command_id, command, commands, False)
    command.success(outcome)
    return command.succeed

def get_hold_outcome(command_id, command, commands):
    # check for other attacks that affect the hold
    other_attacks_on_destination_outcome = check_other_attacks(command_id, command, commands, False)
    # if there are no other attacks then the hold is valid
    if other_attacks_on_destination_outcome:
        outcome = True
    # if there are other attacks check the strengths of the attack(s) and the hold
    else:
        dictionary_without_command = commands.copy()
        dictionary_without_command.pop(command_id)
        for attacking_command_id in dictionary_without_command:
            attacking_command = dictionary_without_command[attacking_command_id]
            if attacking_command.location == attacking_command.origin and attacking_command.destination == command.location:
                if command.strength >= attacking_command.strength:
                    outcome = True
                else:
                    outcome = False
                    break
            else:
                outcome = True
    command.success(outcome)
    return command.succeed

def check_commanders(command_id, command, commands, destination_command):
    # if the two commands have the same human then the outcome is false
    # a command cannot dislodge a unit of the same country
    if command.human == destination_command.human:
        outcome = False
    else:
        # might need to check for other attacks
        destination_command_id = destination_command.unit.id
        outcome = check_other_attacks(command_id, command, commands, destination_command_id)
        #outcome = True
    return outcome

def get_destination(command, commands):
    #code under this if statement may be obsolete now
    """
    if command.destination.is_occupied == 1:
        destination_node = command.destination
        destination_parent = destination_node.name[:3]
        for command_id in commands:
            if commands[command_id].destination == destination_parent:
                destination_command_id = command_id
                break
            elif destination_parent in commands[command_id].location.name:
                destination_command_id = command_id
                break
        # get destination node for coastal cases
        if isinstance(destination_node, Coastal_Node):
            destination_parent = destination_node.name[:3]
            for id in commands:
                if commands[id].destination == destination_parent:
                    destination_command_id = id
                    break
                elif destination_parent in commands[id].location.name:
                    destination_command_id = id
                    break
        # not sure if this is necessary
        # get destination node for non-coastal cases
        else:
            for id in commands:
                if command.destination.name in commands[id].location.name:
                    destination_command_id = id
    
    # get destination node for non-coastal cases
    else:
    """
    destination_command_id = command.destination.is_occupied.id
    destination_command = commands[destination_command_id]
    return destination_command_id, destination_command

def get_success_attacks(commands):
    for command_id in commands:
        command = commands[command_id]
    for command_id in commands:
        command = commands[command_id]
        # run attack and hold functions for coastal nodes
        if isinstance (command.location, Coastal_Node):
            if command.location.parent == command.destination:
                get_hold_outcome (command_id, commands[command_id], commands)
            elif command.location.parent == command.origin and command.origin != command.destination:
                get_attack_outcome (command_id, commands[command_id], commands)
        # run attack and hold functions for non coastal nodes
        else:
            if command.location == command.destination:
                get_hold_outcome(command_id, commands[command_id], commands)
            elif command.location == command.origin and command.origin != command.destination:
                get_attack_outcome(command_id, commands[command_id], commands)
            # if not an attack or hold then continue to next command
            else:
                continue
    return commands


def get_relevant_attacks(command_id, destination_command_id, commands, relevant_attacking_commands, last_relevant_attack = None):
    #print("destination command id", destination_command_id)
    command = commands[command_id]
    destination_command = commands[destination_command_id]
    relevant_attack_destination_dict = {}
    # get relevant_attacks
    for other_command_id in commands:
        if command_id != other_command_id and destination_command_id != other_command_id and other_command_id not in relevant_attacking_commands.keys():
            other_command = commands[other_command_id]
            if other_command.destination == destination_command.location and other_command.location == other_command.origin:
                relevant_attacking_commands[other_command_id] = commands[other_command_id]
                boolean_value = True
                relevant_other_command_id = other_command_id
                break
            elif other_command.location == commands[destination_command_id].destination and other_command.location == other_command.origin:
                relevant_attacking_commands[other_command_id] = commands[other_command_id]
                relevant_other_command_id = other_command_id
                boolean_value = True
                break
            else:
                boolean_value = False
    if boolean_value == True:
        relevant_attacking_commands = get_relevant_attacks(destination_command_id, relevant_other_command_id, commands, relevant_attacking_commands)
    return relevant_attacking_commands





def retrieve_last_relevant_attack(relevant_attacking_commands):
    relevant_attack_destination_dict = {}
    # get dictionary of commands and their destinations
    for relevant_attack_id in relevant_attacking_commands:
        relevant_attacking_command = relevant_attacking_commands[relevant_attack_id]
        relevant_attack_destination_dict[relevant_attacking_command] = relevant_attacking_command.destination
    # retrieve last relevant attack from destinations 
        #print("check", relevant_attacking_command.unit.id, relevant_attacking_command.destination.name)
    count = 0
    #print(relevant_attacking_commands)
    for relevant_attack_id in relevant_attacking_commands:
        relevant_attacking_command = relevant_attacking_commands[relevant_attack_id]
        #print(relevant_attacking_command.unit.id, relevant_attacking_command.location.name, relevant_attacking_command.destination.name)
        if relevant_attacking_command.location in relevant_attack_destination_dict.values():# and relevant_attacking_command.destination not in relevant_attack_destination_dict.values():
            #print("true")
            #print(relevant_attack_id)
            count +=1 
            last_relevant_attack = relevant_attacking_command
            break
        else:
            #print(relevant_attack_id)
            last_relevant_attack = None
            #continue
        """
        else:
            print("false")
            print(relevant_attack_id)
            last_relevant_attack = relevant_attacking_command
            break
        """
    return last_relevant_attack