import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Nodes"))
from Functions_Node import create_nodes
from Functions_Node import create_special_nodes
from Functions_Node import retrieve_node_strings
from Class_Sub_Node import Coastal_Node
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Commanders"))
from Functions_Commander import create_commanders
from Functions_Commander import retrieve_cmdr_strings
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Commands"))
from Functions_Command import create_commands
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Units"))
from Class_Unit import Unit
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Process_Moves"))
from Functions_Filter import filter_owner
from Functions_Filter import filter_unit_type
from Functions_Filter import filter_neighbors
from Functions_Support import det_valid_support
from Functions_Attack import det_success_attacks
from Functions_Post_Outcome import det_outcome_locs
from Functions_Post_Outcome import det_retreats

def run_create_nodes(data_nodes_main, data_nodes_coastal):
    nodes = create_nodes(data_nodes_main)
    nodes_coastal = create_special_nodes(nodes, data_nodes_coastal)
    for each_coastal in nodes_coastal:
        nodes_coastal[each_coastal].assign_sibling(nodes_coastal)
    all_nodes = {**nodes, **nodes_coastal}
    for each_node in all_nodes:
        nbrs_string, dots_string, hsc_string = retrieve_node_strings(each_node, data_nodes_main, data_nodes_coastal)
        all_nodes[each_node].assign_nbrs(all_nodes, nbrs_string)
        all_nodes[each_node].assign_dot(dots_string)
        all_nodes[each_node].assign_hsc(hsc_string)
    return all_nodes

def update_commanders(commanders, nodes, cmdrs_data, units_data):
    units = {}
    for each_commander in commanders:
        cmdr = commanders[each_commander]
        unit_members_strings, dots_owned_strings, country_string = retrieve_cmdr_strings(cmdr.human, cmdrs_data)
        cmdr.assign_country(country_string)
        cmdr.add_units(units_data, unit_members_strings, nodes)
        units = {**units, **cmdr.unit_members}
        cmdr.retrieve_dots_owned(dots_owned_strings, nodes)
        cmdr.retrieve_hsc(dots_owned_strings, nodes)
    return commanders, units

def coastal_node_assign_occ(all_nodes):
    for each_node in all_nodes:
        if isinstance (all_nodes[each_node], Coastal_Node):
            parent_occ = False
            if isinstance(all_nodes[each_node].is_occ, Unit):
                all_nodes[each_node].assign_occ_to_family(parent_occ)
        elif len(each_node[:3]) > 0:
            if isinstance(all_nodes[each_node].is_occ, Unit):
                parent_occ = True
                for each in all_nodes:
                    if each[:3] in each_node and each != each_node:
                        all_nodes[each].assign_occ_to_family(parent_occ)
    return all_nodes

def assign_occ(nodes, units):
    for node in nodes:
        nodes[node].assign_occ(False)
    for unit in units:
        occupied_node = units[unit].loc
        occupied_node.assign_occ(units[unit])
    return nodes

def run_filter_owners(commands, commanders, units):
    valid_cmds = {}
    invalid_cmds = {}
    for cmding_unit in commands:
        cmd_obj = filter_owner(commands[cmding_unit], commanders, units)
        if cmd_obj.legal != 1:
            invalid_cmds[cmding_unit] = cmd_obj
        else:
            valid_cmds[cmding_unit] = cmd_obj
    return valid_cmds, invalid_cmds


def tgdp_objs(data_nodes_main, data_nodes_coastal, cmdrs_data, units_data, cmds_data):
    commanders = create_commanders(cmdrs_data)
    nodes = run_create_nodes(data_nodes_main, data_nodes_coastal)
    commanders, units = update_commanders(commanders, nodes, cmdrs_data, units_data)
    nodes = assign_occ(nodes, units)
    nodes = coastal_node_assign_occ(nodes)
    commands = create_commands(cmds_data, commanders, nodes, units)
    return commands, commanders, nodes, units

def tgdp_filter_cmds(commands, commanders, nodes):
    valid_cmds = {}
    invalid_cmds = {}
    for cmding_unit in commands:
        cmd_obj = commands[cmding_unit]
        cmd_obj = filter_owner(cmd_obj, commanders)
        cmd_obj = filter_unit_type(cmd_obj)
        cmd_obj = filter_neighbors(cmd_obj, nodes)
        if cmd_obj.legal != 1:
            invalid_cmds[cmding_unit] = cmd_obj
            cmd_obj.origin = cmd_obj.loc
            cmd_obj.destination = cmd_obj.loc
            valid_cmds[cmding_unit] = cmd_obj
        else:
            valid_cmds[cmding_unit] = cmd_obj
    return valid_cmds, invalid_cmds

def tgdp_process_cmds(commands):
    commands = det_valid_support(commands)
    commands = det_success_attacks(commands)
    for unit_id in commands:
        print(unit_id, commands[unit_id].strength, commands[unit_id].legal, commands[unit_id].succeed)
    return commands

def tgdp_process_outcomes(commands, nodes, units):
    units = det_outcome_locs(commands, nodes, units)
    units = det_retreats(units)
    for each in units:
        unit = units[each]
        if unit.retreat:
            retreat_choice = unit.retreat[0]
            retreat_node = nodes[retreat_choice]
            unit.assign_loc(retreat_node, False, False)
    nodes = assign_occ(nodes, units)
    """
    for node in nodes:
        if nodes[node].is_occ:
            if nodes[node].is_occ == 1:
                print(node, nodes[node].is_occ)
            else:
                print(node, nodes[node].is_occ.id)
    """
    return nodes, units