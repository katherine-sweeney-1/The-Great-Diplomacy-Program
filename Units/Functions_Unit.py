from Class_Unit import Unit
from Hard_Data_Units import units_data_1 as units_data

"""
def create_units(units_data):
    unit_dict = {}
    for each_unit in units_data:
        nested_info = units_data[each_unit]
        new_unit = Unit(each_unit, nested_info)
        #new_unit.get_loc_node()
        #new_unit.print_statements()
        unit_dict[new_unit.id] = new_unit
    return unit_dict
"""

def create_unit(unit_id_string, nodes_dict, nodes_coastal_dict, cmdr):
    unit_type = units_data[unit_id_string]["type"]
    unit_loc_string = units_data[unit_id_string]["loc"]
    unit = Unit(unit_id_string, unit_type)
    unit.assign_loc(unit_loc_string, nodes_dict, nodes_coastal_dict)
    unit.assign_cmdr(cmdr)
    return unit

def retrieve_units_dict(units_dict, cmdr):
    for each_unit in cmdr.unit_members:
        unit_obj = cmdr.unit_members[each_unit]
        units_dict[each_unit] = unit_obj
    return units_dict