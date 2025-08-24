import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Tables"))
from Run_Objects import assign_occupied

# get outcome locations for processed commands
def get_outcome_nodes(commands, units):
    for command_id in commands:
        # get outcomes for successful commands
        if commands[command_id].succeed:
            # outcome location for holds
            if commands[command_id].location == commands[command_id].origin == commands[command_id].destination:
                outcome_node = commands[command_id].destination
            # outcome location for attacks
            elif commands[command_id].location == commands[command_id].origin and commands[command_id].origin != commands[command_id].destination:
                outcome_node = commands[command_id].destination
            # outcomes location for supports
            else:
                outcome_node = commands[command_id].location
            retreat = False
        # get outcomes for unsuccessful commands
        else:
            # determine if any commands displace the unsuccessful command
            for potential_attack_id in commands:
                if potential_attack_id != command_id:
                    if commands[potential_attack_id].destination.name == commands[command_id].location.name:
                        if commands[potential_attack_id].location == commands[potential_attack_id].origin and commands[potential_attack_id].origin != commands[potential_attack_id].destination:
                            if commands[potential_attack_id].strength > commands[command_id].strength:
                                outcome_node = commands[command_id].location
                                retreat = True
                                break
                            else:
                                retreat = False
                        else:
                            retreat = False
                    else:
                        retreat = False
                else:
                    retreat = False
                    outcome_node = commands[command_id].location
        units[command_id].assign_retreat_disband(retreat)
        units[command_id].assign_location(outcome_node, False, False)
        commands[command_id].outcome_location(outcome_node)
    return units

# get retreat nodes for processed commands
def get_retreats(units):
    for unit_id in units:
        if units[unit_id].retreat == True:
            neighbors = units[unit_id].location.neighbors
            retreat_options = []
            for neighbor in neighbors:
                if neighbors[neighbor].is_occupied:
                    pass
                else:
                    if units[unit_id].type == "army" and neighbors[neighbor].node_type == "Land":
                        retreat_options.append(neighbor)
                    elif units[unit_id].type == "fleet" and neighbors[neighbor].node_type == "Sea":
                        retreat_options.append(neighbor)
                    elif neighbors[neighbor].node_type == "Coast":
                        retreat_options.append(neighbor)
            units[unit_id].assign_retreat_disband(retreat_options)
    return units

# process outcomes
def process_outcomes(commands, nodes, units):
    units = get_outcome_nodes(commands, units)
    units = get_retreats(units)
    for unit_id in units:
        if units[unit_id].retreat:
            retreat_choice = units[unit_id].retreat[0]
            retreat_node = nodes[retreat_choice]
            units[unit_id].assign_location(retreat_node, False, False)
    nodes = assign_occupied(nodes, units)
    return nodes, units