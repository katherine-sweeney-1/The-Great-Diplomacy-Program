import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Units"))
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
            if node_obj.dot == True:
                dots_owned[each_dot_string] = node_obj
        self.dots_owned = dots_owned
        return self.dots_owned
    
    def retrieve_hsc(self, nodes_strings_list, all_nodes_dict):
        hsc = {}
        for each_ter in nodes_strings_list:
            node_obj = all_nodes_dict[each_ter]
            if node_obj.hsc != False:
                hsc[each_ter] = node_obj
        self.hsc_nodes = hsc
        return self.hsc_nodes

    def print_statements(self):
        for each_unit in self.unit_members:
            print("commander {} for country {} has unit {} in location {}".
                  format(self.human, self.country, each_unit, self.unit_members[each_unit].loc.name))
            print("unit {} has commander {}".format(each_unit, self.unit_members[each_unit].cmdr.human))
        print("dots owned: {}".format(self.dots_owned))
        print("hsc: {}".format(self.hsc_nodes))
        print(" ")
        