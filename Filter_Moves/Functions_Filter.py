import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Class_Sub_Node import Coastal_Node


def filter_unit_type(cmd, cmding_unit):
    filter_value = 1
        # armies cannot have sea destinations
    if cmd.unit.type == "army":
        if cmd.destination.node_type == "Sea":
            #filter_value = 0
            filter_value = "unit type error"
        # fleets cannot have inland destinations
    else:
        if cmd.destination.node_type == "Land":
            #filter_value = 0
            filter_value = "unit type error"
    #print(cmding_unit.id, filter_value)
    cmd.legal_command(filter_value)
    return cmd

def filter_neighbors(cmd, nodes):
    goal_destination = cmd.destination
    neighboring_nodes = nodes[cmd.loc.name].nbrs
    if goal_destination.name in neighboring_nodes.keys() or goal_destination.name == cmd.loc.name:
        cmd.legal = cmd.legal
    elif isinstance (goal_destination, Coastal_Node) and cmd.unit.type == "army":
        parent_neighbors = goal_destination.parent.nbrs
        sibling_neighbors = goal_destination.sibling.nbrs
        if goal_destination.name in parent_neighbors or goal_destination.name in sibling_neighbors:
            cmd.legal = cmd.legal
        else:
            cmd.legal = "neighboring territory error, coastal edition"
    else:
        cmd.legal = "neighboring territory error"
        #filter_value = 0
    print(cmd.unit.id, cmd.legal)
    print(" ")
    return cmd