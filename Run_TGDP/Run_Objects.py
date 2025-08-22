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

# Nodes
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

# Commanders
def update_commanders(commanders, nodes, cmdrs_data, units_data):
    units = {}
    for id in commanders:
        commander = commanders[id]
        unit_members_strings, dots_owned_strings, country_string = retrieve_cmdr_strings(commander.human, cmdrs_data)
        commander.assign_country(country_string)
        commander.add_units(units_data, unit_members_strings, nodes)
        units = {**units, **commander.unit_members}
        commander.retrieve_dots_owned(dots_owned_strings, nodes)
        commander.retrieve_hsc(dots_owned_strings, nodes)
    return commanders, units

# Coastal nodes occupied status
def coastal_node_assign_occ(nodes):
    for id in nodes:
        if isinstance (nodes[id], Coastal_Node):
            parent_occ = False
            if isinstance(nodes[id].is_occ, Unit):
                nodes[id].assign_occ_to_family(parent_occ)
        elif len(id[:3]) > 0:
            if isinstance(nodes[id].is_occ, Unit):
                parent_occ = True
                for each_id in nodes:
                    if each_id[:3] in id and each_id != id:
                        nodes[each_id].assign_occ_to_family(parent_occ)
    return nodes

# Nodes occupied status
def assign_occ(nodes, units):
    for id in nodes:
        nodes[id].assign_occ(False)
    for id in units:
        occupied_node = units[id].loc
        occupied_node.assign_occ(units[id])
    return nodes, units

# Create Objects
def tgdp_objs(data_nodes_main, data_nodes_coastal, cmdrs_data, units_data, cmds_data):
    commanders = create_commanders(cmdrs_data)
    nodes = run_create_nodes(data_nodes_main, data_nodes_coastal)
    commanders, units = update_commanders(commanders, nodes, cmdrs_data, units_data)
    nodes, units = assign_occ(nodes, units)
    nodes = coastal_node_assign_occ(nodes)
    # commanders, units = update_commanders(commanders, nodes, cmdrs_data, units_data)
    commands = create_commands(cmds_data, commanders, nodes, units)
    return commands, commanders, nodes, units