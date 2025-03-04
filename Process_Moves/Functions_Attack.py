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
                    outcome = False
                    break
            else:
                outcome = "fuck"
        else:
            outcome = True
    cmd.success(outcome)
    return cmd.succeed

def det_attack_outcome(unit_id, cmd, all_cmds):
    if cmd.destination.is_occ:
        # special case node occupied => get id for unit on special case node
        if cmd.destination.is_occ == 1:
            destination_node = cmd.destination
            if isinstance(destination_node, Coastal_Node):
                destination_parent = destination_node.name[:3]
                for each_cmd in all_cmds:
                    if all_cmds[each_cmd].destination == destination_parent:
                        unit_dest_id = each_cmd
                        break
                    elif destination_parent in all_cmds[each_cmd].loc.name:
                        unit_dest_id = each_cmd
                        break
            else:
                for indiv_cmd in all_cmds:
                    if cmd.destination.name in all_cmds[indiv_cmd].loc.name:
                        unit_dest_id = indiv_cmd
        # regular case node occupied => get id for unit on node
        else:
            unit_dest_id = cmd.destination.is_occ.id
        unit_dest_obj = all_cmds[unit_dest_id]
        if unit_dest_id in all_cmds :
            if unit_dest_obj.loc == unit_dest_obj.origin and unit_dest_obj.destination != unit_dest_obj.origin:
                unit_on_dest_outcome = det_attack_outcome (unit_dest_id, unit_dest_obj, all_cmds)
                if unit_on_dest_outcome:
                    outcome = check_other_attacks(unit_id, cmd, all_cmds, unit_dest_id)
                else:
                
                    outcome = False
            else:
                if cmd.strength > unit_dest_obj.strength:
                    outcome = True
                else:
                    outcome = False
        else:
            if cmd in all_cmds and cmd.strength > unit_dest_obj.strength:
                outcome = check_other_attacks(unit_id, cmd, all_cmds, False)
            else:
                outcome = True
    else:
        outcome = check_other_attacks(unit_id, cmd, all_cmds, False)
    cmd.success(outcome)
    return cmd.succeed

def det_hold_outcome(unit_id, cmd, all_cmds):
    other_attack_outcome = check_other_attacks(unit_id, cmd, all_cmds, False)
    if other_attack_outcome:
        outcome = True
    else:
        outcome = False
    cmd.success(outcome)
    return cmd

def det_success_attacks(commands):
    for unit_id in commands:
        cmd = commands[unit_id]
        if cmd.loc == cmd.destination:
            det_hold_outcome(unit_id, commands[unit_id], commands)
        elif cmd.loc == cmd.origin and cmd.origin != cmd.destination:
            det_attack_outcome(unit_id, commands[unit_id], commands)
        else:
            continue
    return commands