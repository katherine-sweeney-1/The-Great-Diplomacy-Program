
from Class_Unit import Unit


import sys
import os

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Territories"))
from Class_Node import Node
from Functions_Node import run_dict_format




def create_units(units_data):
    unit_dict = {}
    for each_unit in units_data:
        nested_info = units_data[each_unit]
        new_unit = Unit(each_unit, nested_info)
        new_unit.get_node()
        #new_unit.print_statements()
        unit_dict[each_unit] = new_unit
    return unit_dict