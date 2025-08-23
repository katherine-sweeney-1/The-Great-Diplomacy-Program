from Class_Node import Node
from Class_Sub_Node import Coastal_Node
from Visualize_Node_Class import GraphVisualization

def get_nodes_data_dictionary(csv_file):
    nodes_data_dictionary = {}
    # parse the csv file
    open_file = open(csv_file)
    i = 0
    for line in open_file.readlines():
        line = line.replace("\n", "")
        line = line.split(sep = ",")
        if i > 0:
            # create a nested dictionary of node information
            nested_entry = {"Full Name": line[1], 
                            "Type": line[2],
                            "Neighbors": line[3],
                            "Country": line[4],
                            "Dot": line[5],
                            "Home SupCenter": line[6]}
            nodes_data_dictionary[line[0]] = nested_entry
        i += 1
    return nodes_data_dictionary

def create_nodes (csv_file):
    nodes = {}
    nodes_data_dictionary = get_nodes_data_dictionary(csv_file)
    for id in nodes_data_dictionary:
        node = Node(id, nodes_data_dictionary[id])
        nodes[id] = node
    return nodes

def create_special_nodes (nodes, coastal_csv):
    coastal_nodes = {}
    special_dict = get_nodes_data_dictionary(coastal_csv)
    for id in special_dict:
        each_node = Coastal_Node(id, special_dict[id])
        parent_name = each_node.name[:3]
        parent_node = nodes[parent_name]
        each_node.assign_parent(parent_node)
        coastal_nodes[id] = each_node
    return coastal_nodes

def assign_sibling_nodes(nodes_coastal):
    for each_coastal in nodes_coastal:
        nodes_coastal[each_coastal].assign_sibling(nodes_coastal)
    return nodes_coastal

def retrieve_node_strings(node_name, nodes_data, nodes_coastal_data):
    if "-" in node_name:
        node_data_dictionary = get_nodes_data_dictionary(nodes_coastal_data)
    else:
        node_data_dictionary = get_nodes_data_dictionary(nodes_data)
    neighbors_string = node_data_dictionary[node_name]["Neighbors"]
    dots_string = node_data_dictionary[node_name]["Dot"]
    homesupplycenter_string = node_data_dictionary[node_name]["Home SupCenter"]
    neighbors_string = neighbors_string.split(" ")
    return neighbors_string, dots_string, homesupplycenter_string

def create_graph (nodes):
    territory_graph = GraphVisualization()
    for territory in nodes:
        nbrs = nodes[territory].nbrs.split(" ")
        for each_nbr in nbrs:
            territory_graph.addEdge(territory, each_nbr)
    return territory_graph

def run_create_graph (nodes):
    visual_graph = create_graph(nodes)
    visual_graph.visualize()
    return visual_graph