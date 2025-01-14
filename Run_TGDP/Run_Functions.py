
"""
def loc_unit_dict(units_dict):
    loc_unit_dict = {}
    for each_unit in units_dict:
        unit_obj = units_dict[each_unit]
        unit_loc = unit_obj.loc
        loc_unit_dict[unit_loc] = unit_obj
    return loc_unit_dict
"""

"""
def get_nodes_w_occ_units(nodes, units_on_nodes):
    for each_node in nodes:
        node_obj = nodes[each_node]
        node_occ = node_obj.is_occ(units_on_nodes)
        node_obj.is_occ = node_occ
    return nodes
"""

"""
def attribute_nodes_unit_objs(nodes, units_on_nodes):
    for each_node in nodes:
        obj = nodes[each_node]
        obj.is_occ(units_on_nodes)
        #this gives what I want - is the issue that this occupied isnt being added to node dict?
        print(obj.is_occ(units_on_nodes))
        #print(occupied)
    return nodes
"""


"""
def get_cmdr_unit_dict(cmdrs, units):
    for each_cmdr in cmdrs:
        unit_members_dict = {}
        for each_member in each_cmdr.unit_members:
            obj = units[each_member]
            unit_members_dict[each_member] = obj
        each_cmdr.unit_members = unit_members_dict
    return cmdrs
"""