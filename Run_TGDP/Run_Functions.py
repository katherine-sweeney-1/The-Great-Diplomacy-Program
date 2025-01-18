import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Functions_Node import create_nodes
from Functions_Node import create_special_nodes
from Functions_Node import retrieve_node_strings
from Class_Sub_Node import Coastal_Node
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Commanders"))
from Functions_Commander import retrieve_cmdr_strings
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Filter_Moves"))
from Functions_Filter import filter_owner
from Functions_Filter import filter_unit_type
from Functions_Filter import filter_neighbors

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
            all_nodes[each_node].assign_occ_to_family()
    return all_nodes

def update_units(units):
    for unit in units:
        occupied_node = units[unit].loc
        occupied_node.assign_occ(units[unit])
    return units

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

def run_filter_commands(commands, nodes):
    valid_cmds = {}
    for cmding_unit in commands:
        cmd_obj = commands[cmding_unit]
        cmd_obj = filter_unit_type(cmd_obj)
        cmd_obj = filter_neighbors(cmd_obj, nodes)
        print(cmd_obj.unit.id, cmd_obj.legal)
    return valid_cmds
