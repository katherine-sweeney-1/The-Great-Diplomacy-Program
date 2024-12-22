
from Class_Commander import Commander

def create_commanders (commanders_starting_data):
    commander_dict = {}
    for each_key in commanders_starting_data:
        nested_info = commanders_starting_data[each_key]
        indiv_cmdr = Commander(each_key, 
                                nested_info["Country"], 
                                nested_info["Unit Members"],
                                nested_info["Dots Owned"]
        )
        indiv_cmdr.get_own_dots_nodes()
        indiv_cmdr.get_unit_object()
        #indiv_cmdr.print_statements()
        commander_dict[each_key] = indiv_cmdr
    return commander_dict