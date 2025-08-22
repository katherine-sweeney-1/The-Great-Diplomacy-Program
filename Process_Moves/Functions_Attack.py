import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Class_Sub_Node import Coastal_Node

def retrieve_cmd_dest_dict(cmds):
    cmd_dest_dict = {}
    for cmd in cmds:
        cmd_dest_dict[cmd] = cmds[cmd].destination
    return cmd_dest_dict

def check_other_attacks(unit_id, cmd, dict_wo_cmd, recur_unit_id):
    other_dict = dict_wo_cmd.copy()
    other_dict.pop(unit_id)
    if recur_unit_id != False:
        other_dict.pop(recur_unit_id)
    for id in other_dict:
        other_cmd = other_dict[id]
        # another attack on destination => check other attacks
        if other_cmd.destination == cmd.destination:
            if other_cmd.origin != cmd.origin:
                if cmd.strength > other_cmd.strength:
                    outcome = True
                else:
                    if cmd.strength > other_cmd.strength:
                        outcome = True
                    elif cmd.strength == other_cmd.strength and cmd.loc == cmd.destination:
                        outcome = True
                    else:
                        outcome = False
                        break
            else:
                outcome = True
        else:
            outcome = True
    cmd.success(outcome)
    return cmd.succeed

def get_attack_outcome(unit_id, cmd, all_cmds):
    if cmd.destination.is_occ:
        destination_command_id, destination_command = get_dest_obj(cmd, all_cmds)
        #unit_dest_obj = all_cmds[unit_on_destination_id]
        if destination_command_id in all_cmds :
            if destination_command.loc == destination_command.origin and destination_command.destination != destination_command.origin:
                if cmd.loc == destination_command.destination and cmd.destination == destination_command.loc:
                    outcome = False
                    unit_on_dest_outcome = False
                else:
                    unit_on_dest_outcome = get_attack_outcome (destination_command_id, destination_command, all_cmds)
                if unit_on_dest_outcome:
                    other_outcome = check_other_attacks(unit_id, cmd, all_cmds, destination_command_id)
                    if other_outcome == True:
                        outcome = True
                    else:
                        if cmd.strength > destination_command.strength:
                            outcome = True
                        else:
                            outcome = False
                else:
                    if cmd.strength > destination_command.strength:
                        outcome = check_commanders(cmd, destination_command)
                    else:
                        outcome = False
            else:
                if cmd.strength > destination_command.strength:
                    #outcome = True
                    outcome = check_commanders(cmd, destination_command)
                else:
                    outcome = False
        else:
            
            if cmd in all_cmds and cmd.strength > destination_command.strength:
                other_outcome = check_other_attacks(unit_id, cmd, all_cmds, destination_command_id)
                if other_outcome == True:
                    outcome = True
                else:
                    if cmd.strength > destination_command.strength:
                        outcome = True
                    else:
                        outcome = False
            else:
                outcome = True
    else:
        outcome = check_other_attacks(unit_id, cmd, all_cmds, False)
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
    cmd.success(outcome)
    return cmd.succeed

def get_hold_outcome(unit_id, cmd, all_cmds):
    other_attack_outcome = check_other_attacks(unit_id, cmd, all_cmds, False)
    if other_attack_outcome:
        outcome = True
    else:
        attacking_unit_id, attacking_unit_obj = get_dest_obj(cmd, all_cmds)
        if cmd.strength > attacking_unit_obj.strength:
            outcome = True
        else:
            outcome = False
    cmd.success(outcome)
    return cmd

def get_success_attacks(commands):
    for id in commands:
        cmd = commands[id]
        if cmd.loc == cmd.destination:
            get_hold_outcome(id, commands[id], commands)
        elif cmd.loc == cmd.origin and cmd.origin != cmd.destination:
            get_attack_outcome(id, commands[id], commands)
        else:
            continue
    return commands

def check_commanders(cmd, destination_command):
    if cmd.human == destination_command.human:
        outcome = False
    else:
        outcome = True
    return outcome

def get_dest_obj(cmd, commands):
    if cmd.destination.is_occ == 1:
        destination_node = cmd.destination
        if isinstance(destination_node, Coastal_Node):
            destination_parent = destination_node.name[:3]
            for id in commands:
                if commands[id].destination == destination_parent:
                    destination_command_id = id
                    break
                elif destination_parent in commands[id].loc.name:
                    destination_command_id = id
                    break
        else:
            for id in commands:
                if cmd.destination.name in commands[id].loc.name:
                    destination_command_id = id
    else:
        destination_command_id = cmd.destination.is_occ.id
    destination_command = commands[destination_command_id]
    return destination_command_id, destination_command