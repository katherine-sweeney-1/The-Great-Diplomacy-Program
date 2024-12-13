import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Territories"))
from Nodes_Class import Node


class Unit ():
    
    def __init__ (self, id, type, loc, command):
        self.id = id
        self.type = type
        self.loc = loc
        self.command = command

    def get_loc (self):
        print("location of unit obj", self.loc)
        loc_node = Node(
                        
                        )
        self.loc = loc_node