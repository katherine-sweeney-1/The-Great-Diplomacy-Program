import sys
import os

"""
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Helper_Functions"))
from Run_Units_Loc_Obj_Dict import run_units_loc_obj_dict
"""
class Node ():
    
    def __init__ (self, node_name, node_info):
        self.name = node_name
        self.full_name = node_info["Full Name"]
        self.node_type = node_info["Type"]
        self.nbrs = node_info["Neighbors"]
        self.country = node_info["Country"]
        self.dot = node_info["Dot"]
        self.hsc = node_info["Home SupCenter"]
        self.is_occ = 0

    def parse_nbrs (self):
        self.nbrs = self.nbrs.split(" ")
        return(self.nbrs)

    def assign_occ(self, unit):
        self.is_occ = unit
        return self.is_occ

    def print_statements (self):
        print("Territory {} / {} is owned by {} with neighbors {}"
              .format(self.name, self.full_name, self.country, self.nbrs))
        print("Territory {} has dot status {} and hsc status {} and occupied status {}"
              .format(self.name, self.dot, self.hsc, self.is_occ))
        #print("Territory is occupied by {}".format(self.occ_unit))
        print("   ")




    
    