import networkx as nx
from Class_Node import Node
from Class_Sub_Node import Coastal_Node
from Visualize_Node_Class import GraphVisualization
import sys
import os

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Unit"))
from Hard_Data_Units import units_data_1

"""
CVS File Line List - Elements:
    0 => Abbreviated name (e.g. Mun, Sev)
    1 => Full name (e.g. Munich, Sevestapol)
    2 => Type (land, sea, or coast)
    3 => Neighbors (terrritory abbreviations separated by spaces)
    4 => Country (e.g. Neutral, Fra, Aus)
    5 => Dot (True or False)
    6 => Home SupCenter (True or False)
"""
def parse_file (file_name):
    open_file = open(file_name)
    i = 0
    csv_lines = []
    for line in open_file.readlines():
        line = line.replace("\n", "")
        line = line.split(sep = ",")
        if i > 0:
            csv_lines.append(line)
        i += 1
    return csv_lines

def dict_indiv_ter (csv_file, line_int):
    parsed_file = parse_file(csv_file)
    parsed_line = parsed_file[line_int]
    indiv_ter_name = parsed_line[0]
    indiv_ter_dict = {"Full Name": parsed_line[1], 
                    "Type": parsed_line[2],
                    "Neighbors": parsed_line[3],
                    "Country": parsed_line[4],
                    "Dot": parsed_line[5],
                    "Home SupCenter": parsed_line[6]}
    return indiv_ter_name, indiv_ter_dict

def dict_file (parsed):
    parsed_data_dict = {}
    for each_line in parsed:
        nested_entry = {"Full Name": each_line[1], 
                        "Type": each_line[2],
                        "Neighbors": each_line[3],
                        "Country": each_line[4],
                        "Dot": each_line[5],
                        "Home SupCenter": each_line[6]}
        parsed_data_dict[each_line[0]] = nested_entry
    return parsed_data_dict

def indiv_info(ter, data_dict):
    related_ter_name = ter[:3]
    related_ter_info = data_dict[related_ter_name]
    return related_ter_name, related_ter_info

def get_nodes_data_dict(csv_file):
    parsed_csv = parse_file(csv_file)
    data_dict = dict_file(parsed_csv)
    return data_dict

def create_nodes (csv_file):
    obj_dict = {}
    data_dict = get_nodes_data_dict(csv_file)
    for each_ter in data_dict:
        each_node = Node(each_ter, data_dict[each_ter])
        #each_node.is_occ(units_data_1)
        #each_node.print_statements()
        obj_dict[each_ter] = each_node
    return obj_dict

def create_special_nodes (csv, special_csv):
    i = 0
    obj_dict = {}
    main_dict = get_nodes_data_dict(csv)
    special_dict = get_nodes_data_dict(special_csv)
    for each_entry in special_dict:
        # parent node info
        main_name, main_info = indiv_info(each_entry, main_dict)
        # sibling node info; use even/odd to determine which line of csv is sibling node
        if (i + 1) % 2 == 0:
            sibling_name, sibling_info = dict_indiv_ter(special_csv, i - 1)
        else:
            sibling_name, sibling_info = dict_indiv_ter(special_csv, i + 1)
        each_node = Coastal_Node(each_entry, special_dict[each_entry])
        each_node.get_main(main_name, main_info)
        each_node.get_sibling(sibling_name, sibling_info)
        #each_node.print_statements()
        obj_dict[each_entry] = each_node
        i += 1
    return obj_dict

def create_graph (node_dict):
    territory_graph = GraphVisualization()
    for territory in node_dict:
        nbrs = node_dict[territory].nbrs.split(" ")
        for each_nbr in nbrs:
            territory_graph.addEdge(territory, each_nbr)
    return territory_graph

def run_create_graph (node_dict):
    visual_graph = create_graph(node_dict)
    visual_graph.visualize()
    return visual_graph
