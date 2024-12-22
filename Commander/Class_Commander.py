
#from Commander_Class_Helper_Functions import get_ters, check_node_printing
import sys
import os

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Territories"))
from Class_Node import Node
from Functions_Node import run_dict_format

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Unit"))
from Class_Unit import Unit
#from Functions_Unit import run_dict_format
from Hard_Data_Units import Unit_Data_1 as starting_data_units

data = "data/Nodes_No_Coords.csv"

class Commander ():

    def __init__ (self, human, country, unit_members, owned_dots):
        self.human = human                                  # string 
        self.country = country                              # string
        self.unit_members = unit_members                    # unit object
        self.own_dots = owned_dots                          # node object

    def get_unit_object(self):                              # retrieve unit objects for unit members
        units_dict = {}
        for each_unit in self.unit_members:
            unit_info = starting_data_units[each_unit]
            unit_object = Unit(each_unit, unit_info)
            units_dict[each_unit] = unit_object
        self.unit_objs = units_dict

    def get_own_dots_nodes(self):                             # retrieve node objects for dots owned
        nodes_dict = run_dict_format(data)
        own_dict = {}
        for each_ter in self.own_dots:
           ter_data = nodes_dict.get(each_ter)
           own_dot_node = Node (each_ter, ter_data)
           own_dict[each_ter] = own_dot_node
        self.own_dots = own_dict

    def print_statements(self):
        print(" ")
        print("commander {} has dots in territories {}".
            format(self.human, self.own_dots))
        print(" ")
        print("commander {} has units {} which are objects {}".
              format(self.human, self.unit_members, self.unit_objs))
        print(" ")