"""
import sys
import os

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Helper_Functions"))
from Run_Nodes_Data_Dict import run_nodes_data_dict

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Class_Node import Node

data = "data/Data_Ter_Main.csv"
data_special_cases = "data/Data_Ter_Special_Coasts.csv"
"""
class Unit ():
    
    def __init__ (self, unit_id, unit_type):
        self.id = unit_id
        self.type = unit_type
        self.loc = []
        self.command = []

    def assign_loc (self, loc_string, node_dict, special_node_dict):
        if "-" in loc_string:
            self.loc = special_node_dict[loc_string]
        else:
            self.loc = node_dict[loc_string]
        return self.loc

    def assign_cmdr(self, cmdr_obj):
        self.cmdr = cmdr_obj
        return self.cmdr

    def print_statements (self):
        print(" ")
        print("Unit ID", self.id)
        print("Unit type", self.type)
        print("Unit command", self.command)