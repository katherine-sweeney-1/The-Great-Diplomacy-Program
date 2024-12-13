
from Commander_Class import Commander

def create_commander (indiv_key, nested_info):
    commander = Commander(indiv_key, 
                                nested_info["Country"], 
                                nested_info["Unit Members"],
                                nested_info["Dots Owned"],
                                nested_info["Dots Occ"])
    return commander

def run_create_commander (commander_data):
    commander_list = []
    for each_key in commander_data:
        indiv_cmdr = create_commander(each_key, commander_data[each_key])
        indiv_cmdr.get_own_dots()
        indiv_cmdr.get_occ_ters()
        # indiv_cmdr.check_class_works()
        commander_list.append(indiv_cmdr)
    return commander_list