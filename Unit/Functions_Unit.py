
from Class_Unit import Unit


def create_units(units_data):
    for each_unit in units_data:
        nested_info = units_data[each_unit]
        new_unit = Unit(
                        each_unit,
                        nested_info["type"],
                        nested_info["loc"],
                        nested_info["command"]

        )
        new_unit.get_loc_node()
        new_unit.print_statements()