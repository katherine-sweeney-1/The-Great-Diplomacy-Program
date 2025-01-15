"""
import sys
import os


sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Helper_Functions"))
from Run_Nodes_Data_Dict import run_nodes_data_dict

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Territories"))
from Class_Node import Node

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Unit"))
from Class_Unit import Unit
from Hard_Data_Units import units_data_1 as starting_data_units

nodes_hard_data = "data/Data_Ter_Main.csv"
data_special_cases = "data/Data_Ter_Special_Coasts.csv"
nodes_dict_special = run_nodes_data_dict(data_special_cases)
nodes_dict = run_nodes_data_dict(nodes_hard_data)
"""
class Command ():

    def __init__ (self, country_string):
        #self.unit = cmding_unit
        #self.loc = cmd_dict["location"]
        #self.origin = cmd_dict["origin"]
        #self.dest = cmd_dict["destination"]
        self.country = country_string
        #self.human = cmd_dict["owner"]
    """
    def assign_country(self, country_string):
        self.country = country_string
        return self.country
    """
    def assign_cmdr(self, unit_string, commanders):
        for indiv_cmdr in commanders:
            cmdr = commanders[indiv_cmdr]
            unit_members = cmdr.unit_members
            if unit_string in unit_members.keys():
                self.human = cmdr
                break
            else:
                continue
        return self.human
    
    def assign_unit(self, unit_string, units):
        self.unit = units[unit_string]
        return self.unit
    
    def assign_loc(self, loc_string, nodes):
        self.loc = nodes[loc_string]
        return self.loc
    
    def assign_origin (self, origin_string, nodes):
        self.origin = nodes[origin_string]
        return self.origin
    
    def assign_destination (self, dest_string, nodes):
        self.destination = nodes[dest_string]
        return self.destination
    
    def print_statement(self):
        print("command for unit {}, country {} has commander {}".format(self.unit.id, self.country, self.human.human))
        print("loc: {}, origin: {}, dest: {}".format(self.loc.name, self.origin.name, self.destination.name))
    """
    def get_commander(cmd_unit):
        for indiv_cmdr in cmdrs_data:
            cmdr_info = cmdrs_data[indiv_cmdr]
            indiv_cmdr_obj = Commander(indiv_cmdr, cmdr_info)
            if cmd_unit.id in indiv_cmdr_obj.unit_members:                   # check if unit belongs to any country
                cmdr_obj = indiv_cmdr_obj
                break
            else:
                continue
        return cmdr_obj
    """
    """
    def get_unit_obj(self):                              # get unit objects
        unit_info = starting_data_units[self.unit]
        unit_obj = Unit(self.unit, unit_info)
        self.unit = unit_obj
        return self.unit
    

    def get_loc_node(self):
        nodes_dict = get_nodes_dict(self.loc)
        loc_data = nodes_dict.get(self.loc)
        loc_node = Node (self.loc, loc_data)
        self.loc = loc_node
        return self.loc

    def get_origin_node(self):
        nodes_dict = get_nodes_dict(self.origin)
        origin_data = nodes_dict.get(self.origin)
        origin_node = Node (self.origin, origin_data)
        self.origin = origin_node
        return self.origin

    def get_dest_node(self):
        nodes_dict = get_nodes_dict(self.dest)
        dest_data = nodes_dict.get(self.dest)
        dest_node = Node (self.dest, dest_data)
        self.dest = dest_node
        return self.dest


    def validate_human (self, cmdr_obj):
        if self.human == cmdr_obj.human:                         # if the person giving the cmd is the correct cmdr
            valid_person = True
        else:
            valid_person = False
        if self.country == cmdr_obj.country:             # if command's affected unit is in the cmdr's country
            valid_country = True
        else:
            valid_country = False
        if valid_person == True and valid_country == True:
            self.valid = True
        else:
            self.valid = False
        return self.valid
    """

    """
    def print_statements(self):                         # check class works
        print(" ")
        print("origin", self.origin.name)
        print("Unit {} at location {} applies effort from origin {} to destination {}".
              format(self.unit.id, self.loc.name, self.origin.name, self.dest.name))
        print("Is command valid? ", self.valid)
    
def get_nodes_dict(territory):
    if "-" in territory:
        nodes_dict = run_nodes_data_dict(data_special_cases)
    else:
        nodes_dict = run_nodes_data_dict(nodes_hard_data)
    return nodes_dict
"""
