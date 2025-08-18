def parse_cmds_units (txt):
    parsed_cmds = {}
    parsed_units = {}
    file = open(txt)
    lines = file.readlines()
    line_count = 0
    country = ""
    commander = ""
    for line in lines:   
        stripped_line = ''.join([char for char in line if char.isalnum()])
        if len(stripped_line) > 0 and stripped_line[0] == "F":
             unit_type = "fleet"
        elif len(stripped_line) > 0 and stripped_line[0] == "A":
             unit_type = "army"
        # country --> get country and commander info
        if len(stripped_line) == 2:
            country = stripped_line
            commander = lines[line_count + 1]
            commander = ''.join([char for char in commander if char.isalnum()])
            unit_count = 1
        # command --> get success and fail status
        else:
            if stripped_line[-5:-1] == "FAIL":
                outcome = False
            else:
                outcome = True
        # commands --> get location, origin, and destination
        if stripped_line != commander and stripped_line != country and stripped_line != "":
            unit_name = country + str(0) + str(unit_count)
            loc_count = 0
            origin_count = 0
            dest_count = 0
            # if there is a coastal node
            if len(stripped_line) > 2 and "/" in line:
                # location is coastal
                if line[5] == "/":
                    loc_count = 3
                # origin is coastal
                elif stripped_line[9] == "/" or stripped_line[10] == "/":
                     origin_count = 3
                # only destination is coastal:
                elif stripped_line[16] == "/":
                     dest_count = 3
            location, origin, destination = det_node_names(line, loc_count, origin_count, dest_count)
            unit_count += 1
            parsed_cmds[unit_name] = {
                 "location": location,
                 "origin": origin,
                 "destination": destination,
                 "country": country,
                 "owner": commander,
                 "outcome": outcome
            }
            parsed_units[unit_name] = {
                 "type": unit_type,
                 "loc": location,
                 "country": country
            }
        line_count += 1
    return parsed_cmds, parsed_units

def det_node_names(line, loc_count, origin_count, dest_count):       
    stripped_line = line[2:]
    location = stripped_line[loc_count : loc_count + 3]
    # get location
    if loc_count != 0:
        location = stripped_line[0:6]
    else:
        location = stripped_line[0:3]
    # supports --> get origin and destination
    if stripped_line[loc_count + 3 : loc_count + 6] == " S ":
        # supports --> get origin
        origin = stripped_line[loc_count + 6 : loc_count + origin_count + 9]
        # supports --> get destination for supporting attacks
        if "to" in stripped_line:
            destination = stripped_line[loc_count + 13: loc_count + origin_count + dest_count+ 16]
        # supports --> get destination for supporting holds
        else:
            destination = stripped_line[loc_count + origin_count + 6 : origin_count + dest_count + 9]
    # convoys --> get origin and destination
    elif stripped_line[loc_count + 3 : loc_count + 6] == " C ":
        origin = stripped_line[loc_count + 6: loc_count + origin_count + 9]
        destination = stripped_line[loc_count + origin_count + 13 : loc_count + origin_count + dest_count + 16]
    # holds --> get origin and destination
    elif stripped_line[loc_count + 4] == "H":
        origin = location
        destination = location
    # attacks --> get origin and destination
    else:
        origin = stripped_line[loc_count + 0:loc_count + origin_count + 3]
        destination = stripped_line[loc_count + origin_count + 7 : loc_count + origin_count + dest_count + 10]
    # format word
    # title node names
    location = location.title()
    origin = origin.title()
    destination = destination.title()
    # replace "/" with "-"
    if "/" in location:
        location = location.replace("/", "-")
        last_letter = location[-1].upper()
        location = location[:-1] + last_letter
    if "/" in origin:
        origin = origin.replace("/", "-")
        last_letter = origin[-1].upper()
        origin = origin[:-1] + last_letter
    if "/" in destination:
        destination = destination.replace("/", "-")
        last_letter = destination[-1].upper()
        destination = destination[:-1] + last_letter
    return location, origin, destination