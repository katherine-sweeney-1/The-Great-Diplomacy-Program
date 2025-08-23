from Class_Node import Node
from Class_Sub_Node import Coastal_Node
from Visualize_Node_Class import GraphVisualization
import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Units"))
from Class_Unit import Unit

# get a dictionary of node data
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

# create node objects
def create_nodes(nodes_data, nodes_data_coastal):
    nodes_main = {}
    nodes_coastal = {}
    nodes_data_dictionary = get_nodes_data_dictionary(nodes_data)
    special_dict = get_nodes_data_dictionary(nodes_data_coastal)
    # create nodes for non-coastal territories
    for id in nodes_data_dictionary:
        node = Node(id, nodes_data_dictionary[id])
        nodes_main[id] = node
    # create nodes for coastal territories
    for id in special_dict:
        each_node = Coastal_Node(id, special_dict[id])
        parent_name = each_node.name[:3]
        parent_node = nodes_main[parent_name]
        each_node.assign_parent(parent_node)
        nodes_coastal[id] = each_node
    # coastal nodes assign sibling nodes
    for each_coastal in nodes_coastal:
        for each_coastal in nodes_coastal:
            nodes_coastal[each_coastal].assign_sibling(nodes_coastal)
    # combine non-coastal and coastal nodes
    nodes = {**nodes_main, **nodes_coastal}
    # assign class properties to nodes
    for node_id in nodes:
        if "-" in node_id:
            node_data_dictionary = get_nodes_data_dictionary(nodes_data_coastal)
        else:
            node_data_dictionary = get_nodes_data_dictionary(nodes_data)
        neighbors_string = node_data_dictionary[node_id]["Neighbors"]
        dots_string = node_data_dictionary[node_id]["Dot"]
        homesupplycenter_string = node_data_dictionary[node_id]["Home SupCenter"]
        neighbors_string = neighbors_string.split(" ")
        # assign string data to node class properties
        nodes[node_id].assign_neighbors(nodes, neighbors_string)
        nodes[node_id].assign_dot(dots_string)
        nodes[node_id].assign_supply_center(homesupplycenter_string)
    return nodes

# Coastal nodes occupied status
def assign_occ_coastal(nodes):
    for id in nodes:
        if isinstance (nodes[id], Coastal_Node):
            parent_occ = False
            if isinstance(nodes[id].is_occupied, Unit):
                nodes[id].assign_occ_to_family(parent_occ)
        elif len(id[:3]) > 0:
            if isinstance(nodes[id].is_occupied, Unit):
                parent_occ = True
                for each_id in nodes:
                    if each_id[:3] in id and each_id != id:
                        nodes[each_id].assign_occ_to_family(parent_occ)
    return nodes

# Nodes occupied status
def assign_occupied(nodes, units):
    for id in nodes:
        nodes[id].assign_occupied(False)
    for id in units:
        occupied_node = units[id].loc
        occupied_node.assign_occupied(units[id])
    return nodes, units

def create_graph (nodes):
    territory_graph = GraphVisualization()
    for territory in nodes:
        nbrs = nodes[territory].neighbors.split(" ")
        for each_nbr in nbrs:
            territory_graph.addEdge(territory, each_nbr)
    return territory_graph

def run_create_graph (nodes):
    visual_graph = create_graph(nodes)
    visual_graph.visualize()
    return visual_graph