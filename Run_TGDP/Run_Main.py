import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Units"))
from Functions_Unit import create_unit
from Hard_Data_Units import units_data_1
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Functions_Node import create_nodes
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Commanders"))
from Functions_Commander import create_commanders
from Functions_Commander import retrieve_members_strings
from Hard_Data_Commanders import cmdrs_data_1
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
nodes_coastal = create_nodes(data_nodes_coastal)

for cmdr in commanders:
    unit_members = retrieve_members_strings(cmdr.human, cmdrs_data_1)
    cmdr.add_units(unit_members, nodes, nodes_coastal)
    cmdr.print_statements()

"""
for node in nodes:
    nodes[node].print_statements()
for coastal in nodes_coastal:
    nodes_coastal[coastal].print_statements()
"""




