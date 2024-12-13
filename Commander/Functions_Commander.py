
from Class_Commander import Commander

def create_commanders (commanders_starting_data):
    commander_list = []
    for each_key in commanders_starting_data:
        nested_info = commanders_starting_data[each_key]
        indiv_cmdr = Commander(each_key, 
                                nested_info["Country"], 
                                nested_info["Unit Members"],
                                nested_info["Dots Owned"],
                                nested_info["Dots Occ"])
        indiv_cmdr.get_own_dots_nodes()
        indiv_cmdr.get_occ_ters_nodes()
        #indiv_cmdr.check_class_works()
        commander_list.append(indiv_cmdr)
    return commander_list