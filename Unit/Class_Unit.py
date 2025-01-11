import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Territories"))
from Class_Node import Node
from Functions_Node import get_data_dict
data = "data/Data_Ter_Main.csv"
data_special_cases = "data/Data_Ter_Special_Coasts.csv"

class Unit ():
    
    def __init__ (self, unit_id, unit_info):
        self.id = unit_id
        self.type = unit_info["type"]
        self.loc = unit_info["loc"]
        self.command = unit_info["command"]

    def get_loc_node (self):
        if "-" in self.loc:
            nodes_dict = get_data_dict(data_special_cases)
        else:
            nodes_dict = get_data_dict(data)
        loc_data = nodes_dict[self.loc]
        loc_node = Node (self.loc, loc_data)
        self.loc = loc_node

    def print_statements(self):
        print(" ")
        print("Unit ID", self.id)
        print("Unit type", self.type)
        print("Unit location", self.loc.name, self.loc)
        print("Unit command", self.command)