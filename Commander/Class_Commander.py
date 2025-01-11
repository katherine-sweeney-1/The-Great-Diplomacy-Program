import sys
import os

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Territories"))
from Class_Node import Node
from Functions_Node import get_data_dict

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Unit"))
from Class_Unit import Unit
from Hard_Data_Units import units_data_1 as starting_data_units

data = "data/Data_Ter_Main.csv"
data_special_nodes = "data/Data_Ter_Special_Coasts.csv"

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
        self.unit_members = units_dict

    def get_own_dots_nodes(self):                             # retrieve node objects for dots owned
        #nodes_dict = run_dict_format(data)
        own_dict = {}
        for each_ter in self.own_dots:
            #print(each_ter, self.own_dots)
            if "-" in each_ter:
               nodes_dict = get_data_dict(data_special_nodes)
            else:
                nodes_dict = get_data_dict(data)
            ter_data = nodes_dict.get(each_ter)
            own_dot_node = Node (each_ter, ter_data)
            own_dict[each_ter] = own_dot_node
        self.own_dots = own_dict

    def print_statements(self):
        print(" ")
        print("commander {} has dots in territories {}".
            format(self.human, self.own_dots))
        print(" ")
        print("commander {} has units {}".
              format(self.human, self.unit_members))
        print(" ")