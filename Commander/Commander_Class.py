
#from Commander_Class_Helper_Functions import get_ters, check_node_printing
import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Territories"))
#from Get_Node import get_ters
from Nodes_Class import Node
from Nodes_Functions import run_dict_format
data = "data/Nodes_No_Coords.csv"

class Commander ():

    def __init__ (self, human, country, unit_members, owned_dots, occ_ters):
        self.human = human                              # string 
        self.country = country                          # string
        self.unit_members = unit_members                # unit object
        self.own_dots = owned_dots                      # node object
        self.occ_ters = occ_ters                        # node object
    
    def get_own_dots(self):                             # retrieve node objects for dots owned
       # own_dots = get_ters(self.own_dots)
       # self.own_dots = own_dots

        nodes_dict = run_dict_format(data)
        own_dict = {}
        #print(self.own_dots)
        for each_ter in self.own_dots:
           #print(each_ter)
           ter_data = nodes_dict.get(each_ter)
           own_dot = Node (
                            each_ter, 
                            ter_data["Full Name"], 
                            ter_data["Type"], 
                            ter_data["Neighbors"],
                            ter_data["Country"],
                            ter_data["Dot"],
                            ter_data["Home SupCenter"]
                            )
           own_dict[each_ter] = own_dot
        self.own_dots = own_dict
        #print("own", self.own_dots)
        
    def get_occ_ters(self):                             # retrieve node objects for occupied territories
        #occ_ters = get_ters(self.occ_ters)
        #self.occ_ters = occ_ters
        nodes_dict = run_dict_format(data)
        occ_dict = {}
        #print(self.occ_ters)
        for each_ter in self.occ_ters:
           #print(each_ter)
           ter_data = nodes_dict.get(each_ter)
           occ_ter = Node (
                            each_ter, 
                            ter_data["Full Name"], 
                            ter_data["Type"], 
                            ter_data["Neighbors"],
                            ter_data["Country"],
                            ter_data["Dot"],
                            ter_data["Home SupCenter"]
                            )
           occ_dict[each_ter] = occ_ter
        self.occ_ters = occ_dict
        #print("occupied", self.occ_ters)