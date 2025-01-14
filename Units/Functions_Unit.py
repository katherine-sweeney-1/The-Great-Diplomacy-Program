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

def create_unit(unit_id_string, nodes_dict, nodes_coastal_dict):
    unit_type = units_data[unit_id_string]["type"]
    unit_loc_string = units_data[unit_id_string]["loc"]
    unit = Unit(unit_id_string, unit_type)
    unit.assign_loc(unit_loc_string, nodes_dict, nodes_coastal_dict)
    return unit

#def run_unit_assign_loc(loc_st)