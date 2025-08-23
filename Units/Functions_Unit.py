from Class_Unit import Unit

def create_unit(units_data, unit_id_string, nodes_dict, cmdr):
    unit_type = units_data[unit_id_string]["type"]
    unit_loc_string = units_data[unit_id_string]["loc"]
    unit = Unit(unit_id_string, unit_type)
    unit.assign_location(False, unit_loc_string, nodes_dict)
    unit.assign_commander(cmdr)
    return unit

def retrieve_units_dict(units_dict, cmdr):
    for each_unit in cmdr.unit_members:
        unit_obj = cmdr.unit_members[each_unit]
        units_dict[each_unit] = unit_obj
    return units_dict