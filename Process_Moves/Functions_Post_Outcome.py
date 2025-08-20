def det_outcome_locs(cmds, nodes, units):
    for unit_id in cmds:
        if cmds[unit_id].succeed:
            # outcome location for holds
            if cmds[unit_id].loc == cmds[unit_id].origin == cmds[unit_id].destination:
                outcome_node = cmds[unit_id].destination
            # outcome location for attacks
            elif cmds[unit_id].loc == cmds[unit_id].origin and cmds[unit_id].origin != cmds[unit_id].destination:
                outcome_node = cmds[unit_id].destination
            # outcomes location for supports
            else:
                outcome_node = cmds[unit_id].loc
            retreat_bool = False
        # determine if displaced
        else:
            for one_unit in cmds:
                if one_unit != unit_id:
                    if cmds[one_unit].destination.name == cmds[unit_id].loc.name:
                        if cmds[one_unit].loc == cmds[one_unit].origin and cmds[one_unit].origin != cmds[one_unit].destination:
                            if cmds[one_unit].strength > cmds[unit_id].strength:
                                outcome_node = cmds[unit_id].loc
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
                    outcome_node = cmds[unit_id].loc
        units[unit_id].assign_retreat_disband(retreat_bool)
        units[unit_id].assign_loc(outcome_node, False, False)
        cmds[unit_id].outcome_location(outcome_node)
    return units

def det_retreats(units):
    for unit in units:
        if units[unit].retreat == True:
            neighbors = units[unit].loc.nbrs
            retreat_options = []
            for nbr in neighbors:
                if neighbors[nbr].is_occ:
                    pass
                else:
                    if units[unit].type == "army" and neighbors[nbr].node_type == "Land":
                        retreat_options.append(nbr)
                    elif units[unit].type == "fleet" and neighbors[nbr].node_type == "Sea":
                        retreat_options.append(nbr)
                    elif neighbors[nbr].node_type == "Coast":
                        retreat_options.append(nbr)
            units[unit].assign_retreat_disband(retreat_options)
    return units