import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Class_Sub_Node import Coastal_Node

def filter_owner(command, commanders):
    cmd_instructor = command.human.human
    if command.legal == 0:
        command.legal = "owner type error - unit does not exist"
    elif command.unit in commanders[cmd_instructor].unit_members.values():
        command.legal = command.legal
    else:
        command.legal = "owner type error - command for wrong country"
        #cmd.legal = 0
    return command

def filter_unit_type(command):
    if command.unit.type == "army":
        if command.destination.node_type == "Sea":
            command.legal = "unit type error - army attempts move directed at sea"
            #cmd.legal = 0
    else:
        if command.destination.node_type == "Land":
            command.legal = "unit type error - fleet attempts move directed at inland"
            #cmd.legal = 0
    return command

def filter_neighbors(command, nodes):
    # attacks and supports
    if isinstance(command.origin, Coastal_Node):
        if command.destination in command.origin.nbrs.values():
            command.legal = command.legal
        elif command.destination.name == command.origin.name:
            command.legal = command.legal
        else:
            command.legal = "neighboring territory error coastal"
    # holds
    else:
        if command.origin in command.destination.nbrs.values():
            command.legal = command.legal
        elif command.destination.name == command.origin.name:
            command.legal = command.legal
        else:
            command.legal = "neighboring territory error"
            #cmd.legal = 0
    return command

