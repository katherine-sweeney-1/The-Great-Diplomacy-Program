import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Territories"))
from Get_Node import get_ters


class Unit ():
    
    def __init__ (self, id, type, loc, command):
        self.id = id
        self.type = type
        self.loc = loc
        self.command = command

    def get_loc (self):
        print("location of unit obj", self.loc)
        loc_node = get_ters(self.loc)
        self.loc = loc_node