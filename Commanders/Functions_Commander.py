from Class_Commander import Commander

def create_commanders (commanders_starting_data):
    commanders = {}
    for each_key in commanders_starting_data:
        nested_info = commanders_starting_data[each_key]
        members = commanders_starting_data[each_key]["Unit Members"]
        indiv_cmdr = Commander(each_key)
        commanders[indiv_cmdr.human] = indiv_cmdr
    return commanders

def retrieve_cmdr_strings(human, commanders_starting_data):
    for each_key in commanders_starting_data:
        if each_key == human:
            members = commanders_starting_data[each_key]["Unit Members"]
            dots_owned = commanders_starting_data[each_key]["Dots Owned"]
            country = commanders_starting_data[each_key]["Country"]
            break
    return members, dots_owned, country

