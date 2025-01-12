import sys
import os

# Import Unit Files
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Units"))
from Functions_Unit import create_units
from Hard_Data_Units import units_data_1 as units_data

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Functions_Node import create_nodes

data_nodes_main = "data/Data_Ter_Main.csv"

def loc_unit_dict(units_dict):
    loc_unit_dict = {}
    for each_unit in units_dict:
        unit_obj = units_dict[each_unit]
        unit_loc = unit_obj.loc
        loc_unit_dict[unit_loc] = unit_obj
    return loc_unit_dict

def get_nodes_occ(nodes, units_on_nodes):
    for each_node in nodes:
        node_obj = nodes[each_node]
        node_occ = node_obj.is_occ(units_on_nodes)
        node_obj.is_occ = node_occ
    return nodes

# unit id : unit object
units = create_units(units_data)

# node name : node object
nodes = create_nodes(data_nodes_main)

units_on_nodes = loc_unit_dict(units)
#print(units_locunit_dict)

nodes = get_nodes_occ(nodes, units_on_nodes)
#print(nodes)

"""
for node in nodes:
    node_obj = nodes[node]
    print(node_obj.name, node_obj.is_occ)
    if node_obj.is_occ != 0:
        print("UNIT", node_obj.is_occ.id)
"""





