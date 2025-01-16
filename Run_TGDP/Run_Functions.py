import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Units"))
from Functions_Unit import retrieve_units_dict
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Functions_Node import create_nodes
from Functions_Node import create_special_nodes
from Functions_Node import assign_sibling_nodes
from Class_Sub_Node import Coastal_Node
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Commanders"))
from Functions_Commander import retrieve_cmdr_strings
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Filter_Moves"))
from Functions_Filter import filter_unit_type


def run_create_nodes(data_nodes_main, data_nodes_coastal):
    nodes = create_nodes(data_nodes_main)
    nodes_coastal = create_special_nodes(nodes, data_nodes_coastal)
    assign_sibling_nodes(nodes_coastal)
    all_nodes = {**nodes, **nodes_coastal}
    return all_nodes

def update_commanders(commanders, nodes, cmdrs_data, units_data):
    units = {}
    for each_commander in commanders:
        cmdr = commanders[each_commander]
        unit_members_strings, dots_owned_strings, country_string = retrieve_cmdr_strings(cmdr.human, cmdrs_data)
        cmdr.assign_country(country_string)
        cmdr.add_units(units_data, unit_members_strings, nodes)
        retrieve_units_dict(units, cmdr)
        cmdr.retrieve_dots_owned(dots_owned_strings, nodes)
    return commanders, units

def coastal_node_assign_occ(all_nodes):
    for each_node in all_nodes:
        if isinstance (all_nodes[each_node], Coastal_Node):
            all_nodes[each_node].assign_occ_to_family()
    return all_nodes

def update_units(units):
    for unit in units:
        unit_obj = units[unit]
        occupied_node = unit_obj.loc
        occupied_node.assign_occ(unit_obj)
    return units

def run_filter_commands(commands):
    commands = filter_unit_type(commands)
    return commands
