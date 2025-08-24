from Class_Unit import Unit

def create_unit(units_data, unit_data_id, nodes, cmdr):
    unit_type = units_data[unit_data_id]["type"]
    unit_loc_string = units_data[unit_data_id]["loc"]
    unit = Unit(unit_data_id, unit_type)
    unit.assign_location(False, unit_loc_string, nodes)
    unit.assign_commander(cmdr)
    return unit

def retrieve_units_dict(units_dict, cmdr):
    for each_unit in cmdr.unit_members:
        unit_obj = cmdr.unit_members[each_unit]
        units_dict[each_unit] = unit_obj
    return units_dict