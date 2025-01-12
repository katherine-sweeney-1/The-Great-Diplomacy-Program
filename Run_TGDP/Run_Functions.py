def loc_unit_dict(units_dict):
    loc_unit_dict = {}
    for each_unit in units_dict:
        unit_obj = units_dict[each_unit]
        unit_loc = unit_obj.loc
        loc_unit_dict[unit_loc] = unit_obj
    return loc_unit_dict

def get_nodes_w_occ_units(nodes, units_on_nodes):
    for each_node in nodes:
        node_obj = nodes[each_node]
        node_occ = node_obj.is_occ(units_on_nodes)
        node_obj.is_occ = node_occ
    return nodes

def get_units_w_loc_node(units, nodes_dict, coastal_nodes_dict):
    for each_unit in units:
        unit_obj = units[each_unit]
        #print("UNIT", unit_obj, unit_obj.loc)
        # temporary pass over weird cases
        if "-" in unit_obj.loc:
            unit_loc = unit_obj.get_loc_node(coastal_nodes_dict)
            unit_obj.loc = unit_loc
        else:
            unit_loc = unit_obj.get_loc_node(nodes_dict)
            unit_obj.loc = unit_loc
            #print("unit", unit_obj.id, unit_obj.loc.name)
    return units

def print_statements(units, nodes):
    for unit in units:
        obj = units[unit]
        print("unit {} has loc {} and is object {}".format(obj.id, obj.loc.name, obj))
    for node in nodes:
        obj = nodes[node]
        print("node {} has a unit {} occupying it and is object {}".format(obj.name, obj.is_occ, obj))
