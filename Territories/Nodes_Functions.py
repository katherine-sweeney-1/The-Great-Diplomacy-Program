"""
Functions used to create the nodes and visualize the nodes

Functions to Create Nodes
        
    parse_file: parses CSV file and returns a list of the lines

    create_node: calls the node_class to make a node based on one line of the 
            parsed csv file and returns a node object

    run_create_node: takes the csv file, runs the parse_file function, and runs
            the lines of the parse_file output into the create_node function. 
            The node objects are entered into a dictionary.
            Key => name (e.g. "Mun")
            Value => node object

Functions to Visualize Nodes

    create_graph: create the nodes and edges for the territories graph

    run_create_graph: run the create_graph function and return the visual graph
"""

import networkx as nx
from Nodes_Class import Node
from Node_Visualize_Class import GraphVisualization

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

#check to make sure the dictionary is working correctly
def run_dict_format(csv_file):
    parsed_csv = parse_file(csv_file)
    data_dict = dict_format(parsed_csv)
    return data_dict


def create_node (dict_key, dict_values):
    indiv_node = Node(dict_key, 
                      dict_values["Full Name"], 
                      dict_values["Type"], 
                      dict_values["Neighbors"], 
                      dict_values["Country"],
                      dict_values["Dot"],
                      dict_values["Home SupCenter"])
    return indiv_node

def run_create_nodes (csv_file):
    obj_dict = {}
    #input data for node is an entry of a nested dictionay
    get_data_dict = run_dict_format(csv_file)
    for each_entry in get_data_dict:
        each_node = create_node(each_entry, get_data_dict[each_entry])
        #node object dictionary keys are the territories' three letter abbreviations
        obj_dict[each_entry] = each_node
        each_node.print_node_info()
    #print(obj_dict)
    run_create_graph(obj_dict)
    return obj_dict


def create_graph (node_dict):
    territory_graph = GraphVisualization()
    for territory in node_dict:
        for each_nbr in node_dict[territory].nbrs:
            territory_graph.addEdge(territory, each_nbr)
    return territory_graph

def run_create_graph (node_dict):
    visual_graph = create_graph(node_dict)
    visual_graph.visualize()
    return visual_graph
