import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Territories"))
from Class_Node import Node
from Functions_Node import run_dict_format
data = "data/Data_Ter_Main.csv"


class Unit ():
    

    def __init__ (self, unit_id, unit_info):
        self.id = unit_id
        self.type = unit_info["type"]
        self.loc = unit_info["loc"]
        self.command = unit_info["command"]

    def get_node (self):
        nodes_dict = run_dict_format(data)
        loc_data = nodes_dict[self.loc]
        loc_node = Node (self.loc, loc_data)
        loc_node = loc_node.occ_ter(self)
        self.loc = loc_node

    def print_statements(self):
        print(" ")
        print("Unit ID", self.id)
        print("Unit type", self.type)
        print("Unit location", self.loc.name, self.loc)
        print("Unit command", self.command)