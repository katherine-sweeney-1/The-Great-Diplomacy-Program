import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Class_Sub_Node import Coastal_Node

"""
def retrieve_command_destination_dictionary(commands):
    destination_commands_dictionary = {}
    for id in commands:
        destination_commands_dictionary[id] = commands[id].destination
    return destination_commands_dictionary
"""
def check_other_attacks(command_id, command, commands, destination_command_id):
    # get a dictionary without the command to check if there are other attacking commands
    dictionary_without_command = commands.copy()
    dictionary_without_command.pop(command_id)
    # remove the command for the unit on the destination
    if destination_command_id != False:
        dictionary_without_command.pop(destination_command_id)
    # check if another command attacks the same destination as the command in question
    for id in dictionary_without_command:
        other_cmd = dictionary_without_command[id]
        # another attack on destination => check other attacks
        if other_cmd.destination == command.destination:
            if other_cmd.origin != command.origin:
                if command.strength > other_cmd.strength:
                    outcome = True
                else:
                    if command.strength > other_cmd.strength:
                        outcome = True
                    elif command.strength == other_cmd.strength and command.location == command.destination:
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

def get_attack_outcome(command_id, command, commands):
    if command.destination.is_occupied:
        # get the command for the unit on the destination
        destination_command_id, destination_command = get_dest_obj(command, commands)
        # if the unit on the destination has a command
        if destination_command_id in commands:
            # if the unit on the destination is attacking 
            if destination_command.location == destination_command.origin and destination_command.destination != destination_command.origin:
                # if the command and unit on destination are trying to attack each other
                if command.location == destination_command.destination and command.destination == destination_command.location:
                    outcome = False
                    unit_on_dest_outcome = False
                # if they're not attacking each other, get the outcome for the command on the destination
                else:
                    unit_on_dest_outcome = get_attack_outcome (destination_command_id, destination_command, commands)
                # if destination's command is successful, check for other attacks on the destination
                if unit_on_dest_outcome:
                    other_outcome = check_other_attacks(command_id, command, commands, destination_command_id)
                    if other_outcome == True:
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
                other_outcome = check_other_attacks(command_id, command, commands, destination_command_id)
                if other_outcome == True:
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
        """
        print(cmd.unit.id, unit_dest_id, "test")
        other_outcome = check_other_attacks(unit_id, cmd, all_cmds, unit_dest_id)
        if other_outcome == True:
            outcome = True
        else:
            if cmd.strength > unit_dest_obj.strength:
                outcome = True
            else:
                outcome = False
        """
    command.success(outcome)
    return command.succeed

def get_hold_outcome(command_id, command, commands):
    # check for other attacks that affect the hold
    other_attack_outcome = check_other_attacks(command_id, command, commands, False)
    # if there are no other attacks then the hold is valid
    if other_attack_outcome:
        outcome = True
    # if there are other attacks check the strengths of the attack(s) and the hold
    else:
        attacking_unit_id, attacking_unit_obj = get_dest_obj(command, commands)
        if command.strength > attacking_unit_obj.strength:
            outcome = True
        else:
            outcome = False
    command.success(outcome)
    return command

def get_success_attacks(commands):
    for id in commands:
        cmd = commands[id]
        # if hold, run hold outcome function
        if cmd.location == cmd.destination:
            get_hold_outcome(id, commands[id], commands)
        # if attack, run attack outcome function
        elif cmd.location == cmd.origin and cmd.origin != cmd.destination:
            get_attack_outcome(id, commands[id], commands)
        # if not an attack or hold then continue to next command
        else:
            continue
    return commands

def check_commanders(command, destination_command):
    # if the two commands have the same human then the outcome is false
    # a command cannot dislodge a unit of the same country
    if command.human == destination_command.human:
        outcome = False
    else:
        outcome = True
    return outcome

def get_dest_obj(command, commands):
    if command.destination.is_occupied == 1:
        destination_node = command.destination
        # nest 8 lines of code replaced the commented out section below 
        destination_parent = destination_node.name[:3]
        for id in commands:
            if commands[id].destination == destination_parent:
                destination_command_id = id
                break
            elif destination_parent in commands[id].location.name:
                destination_command_id = id
                break
        # get destination node for coastal cases
        """
        if isinstance(destination_node, Coastal_Node):
            destination_parent = destination_node.name[:3]
            for id in commands:
                if commands[id].destination == destination_parent:
                    destination_command_id = id
                    break
                elif destination_parent in commands[id].loc.name:
                    destination_command_id = id
                    break
        """
        # not sure is this is necessary
        # get destination node for non-coastal cases
        """
        else:
            for id in commands:
                if command.destination.name in commands[id].loc.name:
                    destination_command_id = id
        """
    # get destination node for non-coastal cases
    else:
        destination_command_id = command.destination.is_occupied.id
    destination_command = commands[destination_command_id]
    return destination_command_id, destination_command