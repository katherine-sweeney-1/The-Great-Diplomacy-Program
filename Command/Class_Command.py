
import sys
import os

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Territories"))
from Class_Node import Node
from Functions_Node import run_dict_format

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Unit"))
from Class_Unit import Unit
from Hard_Data_Units import Unit_Data_1 as starting_data_units


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

    def print_statements(self):                         # check class works
        print(" ")
        print("Unit {} at location {} applies effort from origin {} to destination {}".
              format(self.unit.id, self.loc, self.origin, self.dest))