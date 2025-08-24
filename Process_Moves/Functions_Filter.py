import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Nodes"))
from Class_Sub_Node import Coastal_Node

# filter by unit owners
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

# filter by unit types
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

# filter by neighboring destinations
def filter_neighbors(command):
    # attacks and supports
    if isinstance(command.origin, Coastal_Node):
        if command.destination in command.origin.neighbors.values():
            command.legal = command.legal
        elif command.destination.name == command.origin.name:
            command.legal = command.legal
        else:
            command.legal = "neighboring territory error coastal"
    # holds
    else:
        if command.origin in command.destination.neighbors.values():
            command.legal = command.legal
        elif command.destination.name == command.origin.name:
            command.legal = command.legal
        else:
            command.legal = "neighboring territory error"
            #cmd.legal = 0
    return command

# Filter commands by who owns the units
# THIS IS NOT RUNNING I THINK
def run_filter_owners(commands, commanders, units):
    valid_commands = {}
    invalid_commands = {}
    for command_id in commands:
        command = filter_owner(commands[command_id], commanders, units)
        if command.legal != 1:
            invalid_commands[command_id] = command
        else:
            valid_commands[command_id] = command
    return valid_commands, invalid_commands

# Filter commands for legal commands
def filter_commands(commands, commanders):
    valid_commands = {}
    invalid_commands = {}
    for command_id in commands:
        command = commands[command_id]
        command = filter_owner(command, commanders)
        command = filter_unit_type(command)
        command = filter_neighbors(command)
        if command.legal != 1:
            invalid_commands[command_id] =command
            command.origin = command.location
            command.destination = command.location
            valid_commands[command_id] = command
        else:
            valid_commands[command_id] = command
    return valid_commands, invalid_commands
