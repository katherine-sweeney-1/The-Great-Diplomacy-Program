import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Class_Sub_Node import Coastal_Node

def filter_owner(cmd, cmdrs):
    cmd_instructor = cmd.human.human
    if cmd.legal == 0:
        cmd.legal = "owner type error - unit does not exist"
    elif cmd.unit in cmdrs[cmd_instructor].unit_members.values():
        cmd.legal = cmd.legal
    else:
        cmd.legal = "owner type error - command for wrong country"
        #cmd.legal = 0
    return cmd

def filter_unit_type(cmd):
    if cmd.unit.type == "army":
        if cmd.destination.node_type == "Sea":
            cmd.legal = "unit type error - army attempts move directed at sea"
            #cmd.legal = 0
    else:
        if cmd.destination.node_type == "Land":
            cmd.legal = "unit type error - fleet attempts move directed at inland"
            #cmd.legal = 0
    return cmd

def filter_neighbors(cmd, nodes):
    # attacks and supports
    if isinstance(cmd.origin, Coastal_Node):
        if cmd.destination in cmd.origin.nbrs.values():
            cmd.legal = cmd.legal
        elif cmd.destination.name == cmd.origin.name:
            cmd.legal = cmd.legal
        else:
            cmd.legal = "neighboring territory error coastal"
    # holds
    else:
        if cmd.origin in cmd.destination.nbrs.values():
            cmd.legal = cmd.legal
        elif cmd.destination.name == cmd.origin.name:
            cmd.legal = cmd.legal
        else:
            cmd.legal = "neighboring territory error"
            #cmd.legal = 0
    return cmd

