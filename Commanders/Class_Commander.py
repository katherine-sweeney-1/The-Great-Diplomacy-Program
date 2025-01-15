import sys
import os

#sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Territories"))
#from Class_Node import Node

#sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Helper_Functions"))
#from Run_Nodes_Data_Dict import run_nodes_data_dict

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Unit"))
from Functions_Unit import create_unit
#from Hard_Data_Units import units_data_1 as starting_data_units


class Commander ():

    def __init__ (self, human):
        self.human = human                                  # string 
        self.unit_members = {}                    # unit object
        #self.own_dots = cmdr_info["Dots Owned"]                          # node object

    def assign_country(self, country_string):
        self.country = country_string
        return self.country
    
    def add_units(self, strings_list, nodes_dict, nodes_coastal_dict):
        unit_members = {}
        for each_unit_string in strings_list:
            one_member = create_unit(each_unit_string, nodes_dict, nodes_coastal_dict, self)
            unit_members[each_unit_string] = one_member
        self.unit_members = unit_members
        return self.unit_members

    def retrieve_dots_owned(self, nodes_strings_list, nodes_dict, nodes_coastal_dict):
        dots_owned = {}
        for each_dot_string in nodes_strings_list:
            if "-" in each_dot_string:
                node_obj = nodes_coastal_dict[each_dot_string]
            else:
                node_obj = nodes_dict[each_dot_string]
            dots_owned[each_dot_string] = node_obj
        self.dots_owned = dots_owned
        return self.dots_owned

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
            print("commander {} for country {} has unit {} in location {}".
                  format(self.human, self.country, each_unit, self.unit_members[each_unit].loc.name))
            print("unit {} has commander {}".format(each_unit, self.unit_members[each_unit].cmdr.human))
            print("owned dots are {}".format(self.dots_owned))
        print(" ")
        