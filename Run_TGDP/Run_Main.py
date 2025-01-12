import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Units"))
from Functions_Unit import create_units
from Hard_Data_Units import units_data_1 as units_data
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Functions_Node import create_nodes
from Run_Functions import loc_unit_dict
from Run_Functions import get_nodes_w_occ_units
from Run_Functions import get_units_w_loc_node
from Run_Functions import print_statements

data_nodes_main = "data/Data_Ter_Main.csv"
data_nodes_coastal = "data/Data_Ter_Special_Coasts.csv"

# Dictionary - unit id : unit object
units = create_units(units_data)

# Dictionary - node name : node object
nodes = create_nodes(data_nodes_main)
nodes_coastal = create_nodes(data_nodes_coastal)

# Dictionary - loc : unit object
units_on_nodes_dict = loc_unit_dict(units)

# Nodes have unit objects for the unit occupying each node
nodes = get_nodes_w_occ_units(nodes, units_on_nodes_dict)
nodes_coastal = get_nodes_w_occ_units(nodes_coastal, units_on_nodes_dict)

# Units have node objects for the location of each unit
units = get_units_w_loc_node(units, nodes, nodes_coastal)

printing = print_statements(units, nodes)




