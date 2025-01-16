import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Unit"))
from Functions_Unit import create_unit

class Commander ():

    def __init__ (self, human):
        self.human = human
        self.unit_members = {}

    def assign_country(self, country_string):
        self.country = country_string
        return self.country
    
    def add_units(self, units_data, strings_list, nodes_dict):
        unit_members = {}
        for each_unit_string in strings_list:
            one_member = create_unit(units_data, each_unit_string, nodes_dict, self)
            unit_members[each_unit_string] = one_member
        self.unit_members = unit_members
        return self.unit_members

    def retrieve_dots_owned(self, nodes_strings_list, all_nodes_dict):
        dots_owned = {}
        for each_dot_string in nodes_strings_list:
            node_obj = all_nodes_dict[each_dot_string]
            dots_owned[each_dot_string] = node_obj
        self.dots_owned = dots_owned
        return self.dots_owned

    def print_statements(self):
        for each_unit in self.unit_members:
            print("commander {} for country {} has unit {} in location {}".
                  format(self.human, self.country, each_unit, self.unit_members[each_unit].loc.name))
            print("unit {} has commander {}".format(each_unit, self.unit_members[each_unit].cmdr.human))
            print("owned dots are {}".format(self.dots_owned))
        print(" ")
        