"""
Nodes_Main establishes the nodes for the territories.

parse_file creates a nested dictionary of territories and their properties.

Node class is used to create nodes for the territories.
"""

import Functions_Node as funcs
from Class_Node import Node

territories = funcs.run_create_nodes("data/Nodes_No_Coords.csv")
territories_graph = funcs.run_create_graph(territories)



