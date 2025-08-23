from Class_Commander import Commander

def create_commanders (commanders_starting_data):
    commanders = {}
    for each_key in commanders_starting_data:
        indiv_cmdr = Commander(each_key)
        commanders[indiv_cmdr.human] = indiv_cmdr
    return commanders

def update_commanders(commanders, nodes, commanders_data, units_data):
    units = {}
    for id in commanders:
        commander = commanders[id]
        # get class properties from data
        for each_key in commanders_data:
            if each_key == commander.human:
                members = commanders_data[each_key]["Unit Members"]
                dots_owned = commanders_data[each_key]["Dots Owned"]
                country = commanders_data[each_key]["Country"]
        # assign class properties
        commander.assign_country(country)
        commander.add_units(units_data, members, nodes)
        # update units
        units = {**units, **commander.unit_members}
        # assign class properties
        commander.retrieve_dots_owned(dots_owned, nodes)
        commander.retrieve_hsc(dots_owned, nodes)
    return commanders, units
