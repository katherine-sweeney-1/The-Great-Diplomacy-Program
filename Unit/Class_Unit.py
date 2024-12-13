import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Territories"))
from Class_Node import Node
from Functions_Node import run_dict_format
data = "data/Nodes_No_Coords.csv"


class Unit ():
    
    def __init__ (self, id, type, loc, command):
        self.id = id
        self.type = type
        self.loc = loc
        self.command = command

    def get_loc_node (self):
        nodes_dict = run_dict_format(data)
        loc_data = nodes_dict[self.loc]
        loc_node = Node (self.loc, loc_data)
        self.loc = loc_node

    def print_statements(self):
        print(" ")
        print("Unit ID", self.id)
        print("Unit type", self.type)
        print("Unit location", self.loc.name, self.loc)
        print("Unit command", self.command)