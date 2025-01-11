def run_units_obj_loc_dict(units_data):
    import sys
    import os
    sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Unit"))
    from Class_Unit import Node
    from Functions_Unit import get_unit_objloc_dict
    unit_objloc_dict = get_unit_objloc_dict(units_data)
    return unit_objloc_dict