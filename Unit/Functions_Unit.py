from Class_Unit import Unit

# dictionary of unit object : location to reduce run time
# used to find units occupying nodes in Class_Node
def get_units_objloc_dict(units_data):
    unit_loc_dict = {}
    for each_unit in units_data:
        nested_info = units_data[each_unit]
        new_unit = Unit(each_unit, nested_info)
        new_unit.get_loc_node()
        unit_loc_dict[new_unit.loc] = new_unit
    return unit_loc_dict
    

def create_units(units_data):
    unit_dict = {}
    for each_unit in units_data:
        nested_info = units_data[each_unit]
        new_unit = Unit(each_unit, nested_info)
        new_unit.get_loc_node()
        new_unit.print_statements()
        unit_dict[new_unit.id] = new_unit.loc
    return unit_dict