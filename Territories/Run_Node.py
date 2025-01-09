"""
Nodes_Main establishes the nodes for the territories.

parse_file creates a nested dictionary of territories and their properties.

Node class is used to create nodes for the territories.
"""

import Functions_Node as funcs
from Class_Node import Node

territories = funcs.create_nodes("data/Data_Ter_Main.csv")
#territories_graph = funcs.run_create_graph(territories)

special_territories = funcs.create_special_nodes("data/Data_Ter_Main.csv", "data/Data_Ter_Special_Coasts.csv", )



