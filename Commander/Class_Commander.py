
#from Commander_Class_Helper_Functions import get_ters, check_node_printing
import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Territories"))
#from Get_Node import get_ters
from Class_Node import Node
from Functions_Node import run_dict_format
data = "data/Nodes_No_Coords.csv"

class Commander ():

    def __init__ (self, human, country, unit_members, owned_dots, occ_ters):
        self.human = human                              # string 
        self.country = country                          # string
        self.unit_members = unit_members                # unit object
        self.own_dots = owned_dots                      # node object
        self.occ_ters = occ_ters                        # node object
    
    def get_own_dots_nodes(self):                             # retrieve node objects for dots owned
        nodes_dict = run_dict_format(data)
        own_dict = {}
        for each_ter in self.own_dots:
           ter_data = nodes_dict.get(each_ter)
           own_dot_node = Node (each_ter, ter_data)
           own_dict[each_ter] = own_dot_node
        self.own_dots = own_dict
        
    def get_occ_ters_nodes(self):                             # retrieve node objects for occupied territories
        nodes_dict = run_dict_format(data)
        occ_dict = {}
        for each_ter in self.occ_ters:
           ter_data = nodes_dict.get(each_ter)
           occ_ter_node = Node (each_ter, ter_data)
           occ_dict[each_ter] = occ_ter_node
        self.occ_ters = occ_dict

    def check_class_works(self):
        print("commander {} has dots in territories {}".
            format(self.human, self.own_dots))
        print("commander {} occupies territories {}".
            format(self.human, self.occ_ters))
        print(" ")