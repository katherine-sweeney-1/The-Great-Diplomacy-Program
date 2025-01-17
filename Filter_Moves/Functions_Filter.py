import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Class_Sub_Node import Coastal_Node

def filter_owner(cmd, cmdrs, units):
    cmd_instructor = cmd.human.human
    if cmd.legal == 0:
        cmd.legal = "owner type error - unit does not exist"
    elif cmd.unit.id in cmdrs[cmd_instructor].unit_members.keys():
        cmd.legal = cmd.legal
    else:
        cmd.legal = "owner type error - command for wrong country"
        #cmd.legal = 0
    return cmd

def filter_unit_type(cmd):
    if cmd.unit.type == "army":
        if cmd.destination.node_type == "Sea":
            cmd.legal = "unit type error - army attempts move to sea"
            #cmd.legal = 0
    else:
        if cmd.destination.node_type == "Land":
            cmd.legal = "unit type error - fleet attempts move to inland"
            #cmd.legal = 0
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
            #cmd.legal = 0
    else:
        cmd.legal = "neighboring territory error"
        #cmd.legal = 0
    return cmd