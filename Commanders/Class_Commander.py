import sys
import os

#sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Territories"))
#from Class_Node import Node

#sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Helper_Functions"))
#from Run_Nodes_Data_Dict import run_nodes_data_dict

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Unit"))
from Functions_Unit import create_unit
#from Hard_Data_Units import units_data_1 as starting_data_units

data = "data/Data_Ter_Main.csv"
data_special_nodes = "data/Data_Ter_Special_Coasts.csv"

class Commander ():

    def __init__ (self, human):
        self.human = human                                  # string 
        #self.info = cmdr_info                             # string
        self.unit_members = {}                    # unit object
        #self.own_dots = cmdr_info["Dots Owned"]                          # node object

    def add_units(self, strings_list, nodes_dict, nodes_coastal_dict):
        unit_members = {}
        for each_unit_string in strings_list:
            one_member = create_unit(each_unit_string, nodes_dict, nodes_coastal_dict)
            unit_members[each_unit_string] = one_member
        self.unit_members = unit_members
        return self.unit_members
    """
    def get_unit_object(self):                              # retrieve unit objects for unit members
        units_dict = {}
        for each_unit in self.unit_members:
            unit_info = starting_data_units[each_unit]
            unit_object = Unit(each_unit, unit_info)
            units_dict[each_unit] = unit_object
        self.unit_members = units_dict
    """

    """
    def add_unit_members(self, units):
        unit_members_dict = {}
        units_strings = self.info["Unit Members"]
        for each_member in units_strings:
            obj = units[each_member]
            unit_members_dict[each_member] = obj
        self.unit_members = unit_members_dict
        return self.unit_members
    """

    """
    def get_own_dots_nodes(self):                             # retrieve node objects for dots owned
        #nodes_dict = run_dict_format(data)
        own_dict = {}
        for each_ter in self.own_dots:
            #print(each_ter, self.own_dots)
            if "-" in each_ter:
               nodes_dict = run_nodes_data_dict(data_special_nodes)
            else:
                nodes_dict = run_nodes_data_dict(data)
            ter_data = nodes_dict.get(each_ter)
            own_dot_node = Node (each_ter, ter_data)
            own_dict[each_ter] = own_dot_node
        self.own_dots = own_dict
    """

    
    def print_statements(self):
        #print("commander {} has units {}".format(self.human, self.unit_members))
        for each_unit in self.unit_members:
            print("commander {} has unit {} in location {}".format(self.human, each_unit, self.unit_members[each_unit].loc.name))
        print(" ")
        