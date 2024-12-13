import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Territories"))
from Nodes_Class import Node
from Nodes_Functions import run_dict_format
data = "data/Nodes_No_Coords.csv"


class Unit ():
    
    def __init__ (self, id, type, loc, command):
        self.id = id
        self.type = type
        self.loc = loc
        self.command = command

    def get_loc (self):
        nodes_dict = run_dict_format(data)
        loc_data = nodes_dict[self.loc]
        loc_node = Node ( self.loc,
                         loc_data["Full Name"],
                         loc_data["Type"],
                         loc_data["Neighbors"],
                         loc_data["Country"],
                         loc_data["Dot"],
                         loc_data["Home SupCenter"]
                        )
        self.loc = loc_node

    def print_statements(self):
        print(" ")
        print("Unit ID", self.id)
        print("Unit type", self.type)
        print("Unit location", self.loc.name, self.loc)
        print("Unit command", self.command)