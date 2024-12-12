
from Class_Unit import Unit

def create_unit(indiv_unit_name, nested_info):
    indiv_unit = Unit(
                        indiv_unit_name, 
                        nested_info["type"],
                        nested_info["loc"],
                        nested_info["command"]
                    )
    return indiv_unit

def run_create_unit(units_data):
    for each_unit in units_data:
        new_unit = create_unit(each_unit, units_data[each_unit])
        new_unit.get_loc()
        print(" ")
        print("Unit ID", new_unit.id)
        print("Unit type", new_unit.type)
        print("Unit location", new_unit.loc)
        print("Unit command", new_unit.command)