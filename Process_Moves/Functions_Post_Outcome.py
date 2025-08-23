import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Tables"))
from Run_Objects import assign_occupied

# get outcome locations for processed commands
def get_outcome_locs(commands, nodes, units):
    for id in commands:
        if commands[id].succeed:
            # outcome location for holds
            if commands[id].location == commands[id].origin == commands[id].destination:
                outcome_node = commands[id].destination
            # outcome location for attacks
            elif commands[id].location == commands[id].origin and commands[id].origin != commands[id].destination:
                outcome_node = commands[id].destination
            # outcomes location for supports
            else:
                outcome_node = commands[id].location
            retreat_bool = False
        # determine if displaced
        else:
            for other_id in commands:
                if other_id != id:
                    if commands[other_id].destination.name == commands[id].location.name:
                        if commands[other_id].location == commands[other_id].origin and commands[other_id].origin != commands[other_id].destination:
                            if commands[other_id].strength > commands[id].strength:
                                outcome_node = commands[id].location
                                retreat_bool = True
                                break
                            else:
                                retreat_bool = False
                        else:
                            retreat_bool = False
                    else:
                        retreat_bool = False
                else:
                    retreat_bool = False
                    outcome_node = commands[id].location
        units[id].assign_retreat_disband(retreat_bool)
        units[id].assign_loc(outcome_node, False, False)
        commands[id].outcome_location(outcome_node)
    return units

# get retreat nodes for processed commands
def get_retreats(units):
    for unit in units:
        if units[unit].retreat == True:
            neighbors = units[unit].location.nbrs
            retreat_options = []
            for neighbor in neighbors:
                if neighbors[neighbor].is_occupied:
                    pass
                else:
                    if units[unit].type == "army" and neighbors[neighbor].node_type == "Land":
                        retreat_options.append(neighbor)
                    elif units[unit].type == "fleet" and neighbors[neighbor].node_type == "Sea":
                        retreat_options.append(neighbor)
                    elif neighbors[neighbor].node_type == "Coast":
                        retreat_options.append(neighbor)
            units[unit].assign_retreat_disband(retreat_options)
    return units

# process outcomes
def process_outcomes(commands, nodes, units):
    units = get_outcome_locs(commands, nodes, units)
    units = get_retreats(units)
    for id in units:
        if units[id].retreat:
            retreat_choice = units[id].retreat[0]
            retreat_node = nodes[retreat_choice]
            units[id].assign_location(retreat_node, False, False)
    nodes = assign_occupied(nodes, units)
    return nodes, units