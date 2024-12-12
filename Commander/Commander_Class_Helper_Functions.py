
import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Territories"))
from Nodes_Functions import run_dict_format
from Nodes_Class import Node
data = "data/Nodes_No_Coords.csv"

def get_ters(ters_list):
        nodes_dict = run_dict_format(data)
        ters_dict = {}
        for each_ter in ters_list:
            ter_data = nodes_dict.get(each_ter)
            ter_node = Node(ter_data, 
                            ter_data["Full Name"], 
                            ter_data["Type"], 
                            ter_data["Neighbors"],
                            ter_data["Country"],
                            ter_data["Dot"],
                            ter_data["Home SupCenter"])
            ters_dict[each_ter] = ter_node
            #check_node_printing(ter_node)
        return ters_dict

def check_node_printing(one_node):
    print("Node Object:", one_node)
    print("full name:", one_node.full_name)
    print("node type:", one_node.node_type)
    print("nbrs:", one_node.nbrs)
    print("country:", one_node.country)
    print("dot and HSC status:", one_node.dot, one_node.hsc)
    print(" ")