import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Units"))
#from Functions_Unit import create_unit
from Functions_Unit import retrieve_units_dict
#from Hard_Data_Units import units_data_1
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Functions_Node import create_nodes
from Functions_Node import create_special_nodes
from Functions_Node import assign_sibling_nodes
from Class_Sub_Node import Coastal_Node
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Commanders"))
from Functions_Commander import create_commanders
from Functions_Commander import retrieve_cmdr_strings
from Hard_Data_Commanders import cmdrs_data_1
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Commands"))
from Hard_Data_Commands import cmds_data_1
from Functions_Command import create_commands
"""
from Run_Functions import loc_unit_dict
from Run_Functions import attribute_nodes_unit_objs
from Run_Functions import get_units_w_loc_node
from Run_Functions import print_nodes
from Run_Functions import print_units
from Run_Functions import print_cmdrs
from Run_Functions import attribute_cmdrs_unit_objs
"""
data_nodes_main = "data/Data_Ter_Main.csv"
data_nodes_coastal = "data/Data_Ter_Special_Coasts.csv"

# Dictionary - commander human : commander object
commanders = create_commanders(cmdrs_data_1)
"""
for cmdr in commanders:
    cmdr.print_statements()
"""

# Dictionary - node name : node object
nodes = create_nodes(data_nodes_main)
nodes_coastal = create_special_nodes(nodes, data_nodes_coastal)
assign_sibling_nodes(nodes_coastal)
all_nodes = {**nodes, **nodes_coastal}
#for coastal in nodes_coastal:
    #nodes_coastal[coastal].assign_sibling_nodes(nodes_coastal)

units = {}
for each_commander in commanders:
    cmdr = commanders[each_commander]
    unit_members_strings, dots_owned_strings, country_string = retrieve_cmdr_strings(cmdr.human, cmdrs_data_1)
    cmdr.assign_country(country_string)
    cmdr.add_units(unit_members_strings, nodes, nodes_coastal)
    retrieve_units_dict(units, cmdr)
    cmdr.retrieve_dots_owned(dots_owned_strings, nodes, nodes_coastal)
    #cmdr.print_statements()


for unit in units:
    unit_obj = units[unit]
    occupied_node = unit_obj.loc
    occupied_node.assign_occ(unit_obj)


for each_node in all_nodes:
    if isinstance (all_nodes[each_node], Coastal_Node):
        all_nodes[each_node].assign_occ_to_family()
    else:
        continue

commands = create_commands(cmds_data_1, commanders, units)
for cmd in commands:
    commands[cmd].print_statement()

"""
for node in all_nodes:
    all_nodes[node].print_statements()
"""



