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
    
    def add_units(self, units_data, strings_list, nodes):
        units = {}
        for unit_data_id in strings_list:
            unit = create_unit(units_data, unit_data_id, nodes, self)
            units[unit_data_id] = unit
        self.unit_members = units
        return self.unit_members

    def retrieve_dots_owned(self, nodes_strings_list, nodes):
        dots_owned = {}
        for node_data_id in nodes_strings_list:
            node = nodes[node_data_id]
            if node.dot == True:
                dots_owned[node_data_id] = node
        self.dots_owned = dots_owned
        return self.dots_owned
    
    def retrieve_supply_center(self, nodes_strings_list, nodes):
        supply_centers = {}
        for node_data_id in nodes_strings_list:
            node = nodes[node_data_id]
            if node.supply_center != False:
                supply_centers[node_data_id] = node
        self.supply_centers = supply_centers
        return self.supply_centers

    def print_statements(self):
        for each_unit in self.unit_members:
            print("commander {} for country {} has unit {} in location {}".
                  format(self.human, self.country, each_unit, self.unit_members[each_unit].location.name))
            print("unit {} has commander {}".format(each_unit, self.unit_members[each_unit].commander.human))
        print("dots owned: {}".format(self.dots_owned))
        print("hsc: {}".format(self.hsc_nodes))
        print(" ")
        