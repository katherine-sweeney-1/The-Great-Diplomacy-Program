import sys
import os

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Helper_Functions"))
from Run_Nodes_Data_Dict import run_nodes_data_dict

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Class_Node import Node

data = "data/Data_Ter_Main.csv"
data_special_cases = "data/Data_Ter_Special_Coasts.csv"

class Unit ():
    
    def __init__ (self, unit_id, unit_info):
        self.id = unit_id
        self.type = unit_info["type"]
        self.loc = unit_info["loc"]
        self.command = unit_info["command"]

    """
    def get_loc_node (self):
        if "-" in self.loc:
            nodes_dict = run_nodes_data_dict(data_special_cases)
        else:
            nodes_dict = run_nodes_data_dict(data)
        loc_data = nodes_dict[self.loc]
        loc_node = Node (self.loc, loc_data)
        self.loc = loc_node
    """

    def get_loc_node (self, node_dict):
        unit_loc_obj = node_dict[self.loc]
        self.loc = unit_loc_obj
        return self.loc

    def print_statements (self):
        print(" ")
        print("Unit ID", self.id)
        print("Unit type", self.type)
        print("Unit command", self.command)

