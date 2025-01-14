from Class_Commander import Commander

def create_commanders (commanders_starting_data):
    commander_list = []
    for each_key in commanders_starting_data:
        nested_info = commanders_starting_data[each_key]
        members = commanders_starting_data[each_key]["Unit Members"]
        indiv_cmdr = Commander(each_key)
        commander_list.append(indiv_cmdr)
    return commander_list

def retrieve_cmdr_strings(human, commanders_starting_data):
    for each_key in commanders_starting_data:
        if each_key == human:
            members = commanders_starting_data[each_key]["Unit Members"]
            dots_owned = commanders_starting_data[each_key]["Dots Owned"]
            break
    return members, dots_owned

