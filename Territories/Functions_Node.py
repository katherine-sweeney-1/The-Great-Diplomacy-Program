
import networkx as nx
from Class_Node import Node
from Graph_Nodes import GraphVisualization

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

def dict_format (parsed):
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

def run_dict_format(csv_file):
    parsed_csv = parse_file(csv_file)
    data_dict = dict_format(parsed_csv)
    return data_dict

def run_create_nodes (csv_file):
    obj_dict = {}
    get_data_dict = run_dict_format(csv_file)
    for each_entry in get_data_dict:
        each_node = Node(each_entry, get_data_dict[each_entry])
        obj_dict[each_entry] = each_node
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
