from Class_Commander import Commander

def create_commanders (commanders_starting_data):
    commander_list = []
    for each_key in commanders_starting_data:
        nested_info = commanders_starting_data[each_key]
        members = commanders_starting_data[each_key]["Unit Members"]
        indiv_cmdr = Commander(each_key)
        #indiv_cmdr.add_units(members)
        #indiv_cmdr.get_own_dots_nodes()
        #indiv_cmdr.get_unit_object()
        #indiv_cmdr.print_statements()
        commander_list.append(indiv_cmdr)
    return commander_list

def retrieve_members_strings(human, commanders_starting_data):
    for each_key in commanders_starting_data:
        if each_key == human:
            members = commanders_starting_data[each_key]["Unit Members"]
            break
    return members