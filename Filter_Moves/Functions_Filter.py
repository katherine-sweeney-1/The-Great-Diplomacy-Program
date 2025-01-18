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
            cmd.legal = "unit type error - army attempts move directed at sea"
            #cmd.legal = 0
    else:
        if cmd.destination.node_type == "Land":
            cmd.legal = "unit type error - fleet attempts move directed at inland"
            #cmd.legal = 0
    return cmd

def filter_neighbors(cmd, nodes):
    loc_nbrs = nodes[cmd.loc.name].nbrs
    origin_nbrs = nodes[cmd.origin.name].nbrs
    # attacks and supports for attacks
    if cmd.destination.name in loc_nbrs.keys() and cmd.destination.name in origin_nbrs.keys():
        cmd.legal = cmd.legal
    # support holds
    elif cmd.destination.name in loc_nbrs.keys() and cmd.destination.name == cmd.origin.name:
        cmd.legal = cmd.legal
    # holds
    elif cmd.destination.name == cmd.loc.name:
        cmd.legal = cmd.legal
    else:
        cmd.legal = "neighboring territory error"
        #cmd.legal = 0
    return cmd

"""
Attack: loc A, origin A, dest C

Support (A): loc A, origin B, dest C

Support (H): loc A, origin B, dest B

Hold: loc A, origin A, dest A
"""