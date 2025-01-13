from Class_Unit import Unit
from Hard_Data_Units import units_data_1 as units_data

def create_units(units_data):
    unit_dict = {}
    for each_unit in units_data:
        nested_info = units_data[each_unit]
        new_unit = Unit(each_unit, nested_info)
        #new_unit.get_loc_node()
        #new_unit.print_statements()
        unit_dict[new_unit.id] = new_unit
    return unit_dict

def create_unit(unit_name):
    unit_info = units_data[unit_name]
    unit = Unit(unit_name, unit_info)
    return unit
