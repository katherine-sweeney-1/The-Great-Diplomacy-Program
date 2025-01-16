from Class_Node import Node
from Class_Sub_Node import Coastal_Node
from Visualize_Node_Class import GraphVisualization

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

def get_nodes_data_dict(csv_file):
    parsed_csv = parse_file(csv_file)
    data_dict = dict_file(parsed_csv)
    return data_dict

def create_nodes (csv_file):
    obj_dict = {}
    data_dict = get_nodes_data_dict(csv_file)
    for each_ter in data_dict:
        each_node = Node(each_ter, data_dict[each_ter])
        obj_dict[each_ter] = each_node
    return obj_dict

def create_special_nodes (main_nodes, special_csv):
    i = 0
    obj_dict = {}
    special_dict = get_nodes_data_dict(special_csv)
    for each_entry in special_dict:
        each_node = Coastal_Node(each_entry, special_dict[each_entry])
        parent_name = each_node.name[:3]
        parent_obj = main_nodes[parent_name]
        each_node.assign_parent(parent_obj)
        obj_dict[each_entry] = each_node
        i += 1
    return obj_dict

def assign_sibling_nodes(nodes_coastal_dict):
    for each_coastal in nodes_coastal_dict:
        nodes_coastal_dict[each_coastal].assign_sibling(nodes_coastal_dict)
    return nodes_coastal_dict


def retrieve_nbrs_strings(human, commanders_starting_data):
    for each_key in commanders_starting_data:
        if each_key == human:
            members = commanders_starting_data[each_key]["Unit Members"]
            dots_owned = commanders_starting_data[each_key]["Dots Owned"]
            country = commanders_starting_data[each_key]["Country"]
            break
    return members, dots_owned, country

def retrieve_nbrs_string(node_name, node_obj, nodes_data, nodes_coastal_data):
    nodes_data_dict = get_nodes_data_dict(nodes_data)
    nodes_coastal_data_dict = get_nodes_data_dict(nodes_coastal_data)
    if "-" in node_name:
        nbrs_string = nodes_coastal_data_dict[node_name]["Neighbors"]
    else:
        nbrs_string = nodes_data_dict[node_name]["Neighbors"]
    nbrs_string = nbrs_string.split(" ")
    return nbrs_string


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
