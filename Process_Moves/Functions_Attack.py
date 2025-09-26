import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Nodes/Class_Sub_Node"))
from Class_Sub_Node import Coastal_Node


def check_other_attacks(command_id, command, commands, destination_command_id):
    #print("check other attacks", command_id)
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
            #print("test 1", command_id, other_command.unit.id)
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

"""
def check_other_attacks(command_id, command, commands, destination_command_id):
    print("check other attacks", command_id)
    # get a dictionary without the command to check if there are other attacking commands
    dictionary_without_command = commands.copy()
    dictionary_without_command.pop(command_id)
    # remove the command for the unit on the destination
    if destination_command_id != False:
        dictionary_without_command.pop(destination_command_id)
        for other_command_id in dictionary_without_command:
            other_command = dictionary_without_command[other_command_id]
            if other_command.location == commands[destination_command_id].destination:
                outcome = True
                break
            else:
                if other_command.destination == command.destination:
                    if other_command.origin != command.origin:
                        if command.strength > other_command.strength:
                            outocme = True
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
    # check if another command attacks the same destination as the command in question
    else:
        for other_command_id in dictionary_without_command:
            other_command = dictionary_without_command[other_command_id]
            # another attack on destination => check other attacks
            if other_command.destination == command.destination:
                print("test 1", command_id, other_command.unit.id)
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
"""

"""
def check_other_attacks(command_id, command, commands, destination_command_id):
    #print(command_id)
    # get a dictionary without the command to check if there are other attacking commands
    dictionary_without_command = commands.copy()
    dictionary_without_command.pop(command_id)
    # remove the command for the unit on the destination
    if destination_command_id != False:
        dictionary_without_command.pop(destination_command_id)

        for other_command_id in dictionary_without_command:
            other_command = dictionary_without_command[other_command_id]
            if command_id == "FR06" or command_id == "GE01":
                print(1, command_id, other_command_id)
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
"""

def check_other_attacks(command_id, command, commands, destination_command_id):
    # get a dictionary without the command to check if there are other attacking commands
    dictionary_without_command = commands.copy()
    dictionary_without_command.pop(command_id)
    # remove the command for the unit on the destination
    if destination_command_id != False:
        dictionary_without_command.pop(destination_command_id)

        for other_command_id in dictionary_without_command:
            other_command = dictionary_without_command[other_command_id]
            if other_command.destination == commands[destination_command_id].destination and other_command.location == other_command.origin:
                #outcome = check_if_other_attack_is_on_destination(command_id, command, other_command)
                outcome = True
                break
            else:
                outcome = check_if_other_attack_is_on_destination(command_id, command, other_command)
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







def check_if_other_attack_is_on_destination(command_id, command, other_command):
    if other_command.destination == command.destination:
        if other_command.origin != command.origin:
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


"""
def get_attack_outcome(command_id, command, commands):
    if command.destination.is_occupied:
        # get the command for the unit on the destination
        destination_command_id, destination_command = get_destination(command, commands)
        # if the unit on the destination has a command
        if destination_command_id in commands:
            # if the unit on the destination is attacking 
            if destination_command.location == destination_command.origin and destination_command.destination != destination_command.origin:
                # if the command and unit on destination are trying to attack each other
                if command.location == destination_command.destination and command.destination == destination_command.location:
                    outcome = False
                    destination_command_outcome = False
                # if they're not attacking each other, get the outcome for the command on the destination
                else:
                    destination_command_outcome = get_attack_outcome (destination_command_id, destination_command, commands)
                # if destination's command is successful, check for other attacks on the destination
                if destination_command_outcome:
                    other_attacks_on_destination_outcome = check_other_attacks(command_id, command, commands, destination_command_id)
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
                        outcome = check_commanders(command, destination_command)
                    else:
                        outcome = False
            # if the unit on the destination is not attacking, check the strength to see if the unit is dislodged
            # ensure the commands have different commanders 
            else:
                if command.strength > destination_command.strength:
                    #outcome = True
                    outcome = check_commanders(command, destination_command)
                else:
                    outcome = False
        # if the unit on the destination does not have a command
        # is this still necessary? 
        # all units have valid commands now (illegal commands become holds) so this may not be necessary
        else:
            # if the command is stronger than the destination command's hold/support, check for other attacks
            if command in commands and command.strength > destination_command.strength:
                other_attacks_on_destination_outcome = check_other_attacks(command_id, command, commands, destination_command_id)
                if other_attacks_on_destination_outcome == True:
                    outcome = True
                else:
                    if command.strength > destination_command.strength:
                        outcome = True
                    else:
                        outcome = False
            else:
                outcome = True
    else:
        outcome = check_other_attacks(command_id, command, commands, False)
    command.success(outcome)
    return command.succeed
"""




def get_attack_outcome(command_id, command, commands, count = None):
    if command.destination.is_occupied:
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
                    destination_command_outcome = False
            # if destination's command is successful, check for other attacks on the destination
            if destination_command_outcome:
                other_attacks_on_destination_outcome = check_other_attacks(command_id, command, commands, destination_command_id)
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
                    outcome = check_commanders(command, destination_command)
                else:
                    outcome = False
        # if the unit on the destination is not attacking, check the strength to see if the unit is dislodged
        # ensure the commands have different commanders 
        else:
            if command.strength > destination_command.strength:
                #outcome = True
                outcome = check_commanders(command, destination_command)
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

def check_commanders(command, destination_command):
    # if the two commands have the same human then the outcome is false
    # a command cannot dislodge a unit of the same country
    if command.human == destination_command.human:
        outcome = False
    else:
        outcome = True
    return outcome

def get_destination(command, commands):
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
        destination_command_id = command.destination.is_occupied.id
    destination_command = commands[destination_command_id]
    return destination_command_id, destination_command

def get_success_attacks(commands):
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