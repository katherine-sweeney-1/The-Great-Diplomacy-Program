import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Nodes/Class_Sub_Node"))
from Class_Sub_Node import Coastal_Node

"""
def check_other_attacks(command_id, command, commands, destination_command_id):
    # get a dictionary without the command to check if there are other attacking commands
    print(command_id, destination_command_id)
    dictionary_without_command = commands.copy()
    dictionary_without_command.pop(command_id)
    # remove the command for the unit on the destination
    if destination_command_id != False:
        dictionary_without_command.pop(destination_command_id)
        for other_command_id in dictionary_without_command:
            other_command = dictionary_without_command[other_command_id]
            if other_command.destination == commands[destination_command_id].destination and other_command.location == other_command.origin:
                print("yes")
                print(command_id)
                print(commands[command_id].location.name, commands[command_id].origin.name, commands[command_id].destination.name)
                print("destination command")
                print(destination_command.location.name, destination_command.origin.name, destination_command.destination.name)
                print("other command", other_command.unit.id)
                print(other_command.location.name, other_command.origin.name, other_command.destination.name)
                outcome = True
                break
            else:
                #print("no")
                destination_command = commands[destination_command_id]
                outcome = check_if_other_attack_is_on_destination(command_id, command, other_command, destination_command)
                if outcome == False:
                    break
    # check if another command attacks the same destination as the command in question
    else:
        for other_command_id in dictionary_without_command:
            other_command = dictionary_without_command[other_command_id]
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
    return command.succeed
"""

# need to loop through and find all relevant attacks for check other attacks
# check other attacks only considers the first attack that's relevant
def check_other_attacks(command_id, command, commands, destination_command_id, count = None):
    # get a dictionary without the command to check if there are other attacking commands
    #dictionary_without_command = commands.copy()
    #dictionary_without_command.pop(command_id)
    print("check", command_id)
    relevant_attacking_commands = {}
    # remove the command for the unit on the destination
    if destination_command_id != False:
        relevant_attacking_commands[command_id] = command
        #dictionary_without_command.pop(destination_command_id)
        for other_command_id in commands:
            if command_id != other_command_id:
                other_command = commands[other_command_id]
                """
                if command_id == "IT02":
                    print(command_id, other_command_id)
                    print(other_command.destination.name, commands[destination_command_id].destination.name)
                    print(other_command.location.name, other_command.origin.name)
                    print(" ")
                """
                if other_command.destination == commands[destination_command_id].location and other_command.location == other_command.origin:
                    if command_id == "TU02":
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
        print(command_id)
        print("test", len(relevant_attacking_commands))
        print(relevant_attacking_commands)
        print(" ")
        if len(relevant_attacking_commands) > 0:
            if command_id == "TU02":
                print("test")
                print(command_id)
                print(relevant_attacking_commands)
                print(" ")
            for relevant_attack_id in relevant_attacking_commands:
                one_attacking_command = relevant_attacking_commands[relevant_attack_id]
                #print(one_attacking_command)
                #if one_attacking_command.destination == relevant_attacking_commands[relevant_attack_id].destination and relevant_attack_id.location == relevant_attack_id.origin:
                    #other_attacking_commands[other_command_id] = other_command
                if len(relevant_attacking_commands) > 1:
                    
                    print("check")
                    print(command_id)
                    print(relevant_attacking_commands)
                    print(" ")
                    #relevant_attack_outcome = get_attack_outcome(relevant_attack_id, one_attacking_command, commands)
                    if count == None:
                        print("okkkkkkkk")
                        print(command_id, relevant_attack_id)
                        print(" ")
                        relevant_attack_outcome = check_other_attacks(relevant_attack_id, one_attacking_command, commands, destination_command_id, count = 1)
                    else:
                        #if one_attacking_command.location == command.destination and command.destination == one_attacking_command.location:
                        print("uhhhh", command_id)
                        relevant_attack_outcome = False
                        #else:
                            #print("yyyyyyyyyy")
                            #relevant_attack_outcome = check_other_attacks(relevant_attack_id, one_attacking_command, commands, destination_command_id, count = 2)



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
    return command.succeed




def check_if_other_attack_is_on_destination(command_id, command, other_command, destination_command = None):
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
    #print(command_id)
    if command.destination.is_occupied != False:
        # get the command for the unit on the destination
        destination_command_id, destination_command = get_destination(command, commands)
        # if the unit on the destination is attacking 
        if destination_command.location == destination_command.origin and destination_command.destination != destination_command.origin:
            # if the command and unit on destination are trying to attack each other
            if command.location == destination_command.destination and command.destination == destination_command.location:
                outcome = False
                destination_command_outcome = False
            # if they're not attacking each other, get the outcome for the command on the destination
            else:
                if count == None:
                    destination_command_outcome = get_attack_outcome(destination_command_id, destination_command, commands, count = 1)
                else:
                    if destination_command.location == command.destination and destination_command.destination == command.location:
                        destination_command_outcome = False
                    else:
                        destination_command_outcome = get_attack_outcome(destination_command_id, destination_command, commands, count = 2)
                        #print("uhh", command_id, destination_command_outcome)
            # if destination's command is successful, check for other attacks on the destination
            if destination_command_outcome:
                other_attacks_on_destination_outcome = check_other_attacks(command_id, command, commands, destination_command_id)
                #print("other attacks outocme", command_id, other_attacks_on_destination_outcome)
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
                #print("false outocme", command_id)
                if command.strength > destination_command.strength:
                    #print("check commanders", command_id, destination_command.unit.id)
                    outcome = check_commanders(command_id, command, commands, destination_command)
                else:
                    #print("check 2", command_id)
                    outcome = False
        # if the unit on the destination is not attacking, check the strength to see if the unit is dislodged
        # ensure the commands have different commanders 
        else:
            if command.strength > destination_command.strength:
                outcome = check_commanders(command_id, command, commands, destination_command)
            else:
                outcome = False
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