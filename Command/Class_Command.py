
import sys
import os

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Territories"))
from Class_Node import Node
from Functions_Node import run_dict_format

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Unit"))
from Class_Unit import Unit
from Hard_Data_Units import Unit_Data_1 as starting_data_units

nodes_hard_data = "data/Nodes_No_Coords.csv"
nodes_dict = run_dict_format(nodes_hard_data)

class Command ():

    def __init__ (self, cmding_unit, cmd_dict):
        self.unit = cmding_unit
        self.loc = cmd_dict["location"]
        self.origin = cmd_dict["origin"]
        self.dest = cmd_dict["destination"]

    def get_unit_obj(self):                              # get unit objects
        unit_info = starting_data_units[self.unit]
        unit_obj = Unit(self.unit, unit_info)
        self.unit = unit_obj

    def get_loc_node(self):
        loc_data = nodes_dict.get(self.loc)
        loc_node = Node (self.loc, loc_data)
        self.loc = loc_node

    def get_origin_node(self):
        origin_data = nodes_dict.get(self.origin)
        origin_node = Node (self.origin, origin_data)
        self.origin = origin_node
        #print(self.origin.name)

    def get_dest_node(self):
        dest_data = nodes_dict.get(self.dest)
        dest_node = Node (self.dest, dest_data)
        self.dest = dest_node

    def print_statements(self):                         # check class works
        print(" ")
        print("origin", self.origin.name)
        print("Unit {} at location {} applies effort from origin {} to destination {}".
              format(self.unit.id, self.loc.name, self.origin.name, self.dest.name))