from Class_Commander import Commander

def create_commanders (commanders_starting_data):
    commanders = {}
    for id in commanders_starting_data:
        commander = Commander(id)
        commanders[commander.human] = commander
    return commanders

def update_commanders(commanders, nodes, commanders_data, units_data):
    units = {}
    for id in commanders:
        commander = commanders[id]
        # get class properties from data
        for id in commanders_data:
            if id == commander.human:
                members = commanders_data[id]["Unit Members"]
                dots_owned = commanders_data[id]["Dots Owned"]
                country = commanders_data[id]["Country"]
        # assign class properties
        commander.assign_country(country)
        commander.add_units(units_data, members, nodes)
        # update units
        units = {**units, **commander.unit_members}
        # assign class properties
        commander.retrieve_dots_owned(dots_owned, nodes)
        commander.retrieve_supply_center(dots_owned, nodes)
    return commanders, units
