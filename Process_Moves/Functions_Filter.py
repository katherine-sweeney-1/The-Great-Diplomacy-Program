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
    if cmd.loc in cmd.destination.nbrs.values():
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

"""
    if cmd.unit.type == "fleet" and isinstance (cmd.destination, Coastal_Node):
        print("yes")
        print("coastal!!", cmd.destination.name, cmd.loc.name, cmd.destination.nbrs)
        if cmd.loc in cmd.destination.nbrs.values():
            print("fuck yes")
        else:
            print("oh no bro")
"""

"""
elif cmd.loc in cmd.destination.nbrs.values() and cmd.destination.name == cmd.origin.name:
    cmd.legal = cmd.legal
"""