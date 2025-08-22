def retrieve_cmd_dest_dict(commands):
    cmd_dest_dict = {}
    for id in commands:
        cmd_dest_dict[id] = commands[id].destination
    return cmd_dest_dict

def get_valid_support(commands, id = None, recur_bool = None):
    for id in commands:
        # if a unit is attacking
        if commands[id].loc == commands[id].origin:
            continue
        command = commands[id]
        # if a unit is supporting
        if command.loc != command.origin:
            for other_id in commands:
                # if another unit affects the supporting unit
                if command.loc == commands[other_id].destination:
                    # check if the affecting command is an attack
                    if commands[other_id].loc == commands[other_id].origin:
                        # check if command supports an attack on the unit trying to cut support
                        if command.destination == commands[other_id].loc:
                            print("check 1", id)

                            """
                            # recursion attempt
                            for pot_other_support in cmds:
                                if cmds[pot_other_support].loc != cmds[pot_other_support].origin and cmds[pot_other_support].origin != cmds[pot_other_support].destination:
                                    if recur_bool:
                                        print("test 0", unit_id)
                                        cmd_success = True
                                        break
                                    else:
                                        print("test 1", unit_id)
                                        other_success = pot_other_suppoprt_success = det_valid_support(cmds, unit_id, True)
                                        if other_success:
                                            cmd_success = False
                                            break
                                        else:
                                            cmd_success = True
                                            break
                                        #break
                                else:
                                    continue

                            """

                            #print("test 2", unit_id, other_unit)
                            command_success = True
                        else:
                            command_success = False
                            break
                    else:
                        command_success = True


                else:
                    command_success = True
        if command_success and command.origin.is_occ != False:
            if command.origin.is_occ == 1:
                origin = command.origin
                for id in commands:
                    if commands[id] == origin:
                        supported_command_id = id
                        supported_command = commands[supported_command_id].origin.is_occ.id
                        break
            else:
                supported_command_id = command.origin.is_occ.id
            supported_command = commands[supported_command_id]
            if supported_command_id in commands:
                if supported_command.loc != command.loc:
                    if command.origin and supported_command.origin and supported_command.destination == command.destination:
                        command_strength = 1
                        supported_command.cmd_strength(command_strength)
                    elif supported_command.origin != supported_command.destination and supported_command.loc != supported_command.origin:
                        command_strength = 1
                        supported_command.cmd_strength(command_strength)
                    elif supported_command.origin == supported_command.destination and supported_command.loc != supported_command.origin:
                        command_strength = 1
                        supported_command.cmd_strength(command_strength)
                    
                    else:
                        command_strength = 0
                else:
                    command_strength = 0
            else:
                command_strength = 0
    
        else:
            command_strength = 0
        command.success(command_success)
    return commands


"""
def det_valid_support(cmds, unit_id = None):
    for unit_id in cmds:
        # if a unit is attacking
        if cmds[unit_id].loc == cmds[unit_id].origin:
            continue
        cmd_obj = cmds[unit_id]
        # if a unit is supporting
        if cmd_obj.loc != cmd_obj.origin:
            for other_unit in cmds:
                # if another unit attacks the supporting unit
                if cmd_obj.loc == cmds[other_unit].destination:
                    if cmds[other_unit].loc == cmds[other_unit].origin:
                        # check if command supports an attack on the unit trying to cut support
                        if cmd_obj.destination == cmds[other_unit].loc:
                            print("test 1", unit_id, other_unit)
                            for pot_other_support in cmds:
                                # if there is a command that's not the supporting unit or attacking unit
                                #if cmds[pot_other_support].loc != cmd_obj.loc and cmds[pot_other_support].loc != cmds[other_unit].loc:
                                    # if the command is supporting an attack
                                if cmds[pot_other_support].loc != cmds[pot_other_support].origin and cmds[pot_other_support].origin != cmds[pot_other_support].destination:
                                        #print("yes 1", "unit", unit_id, "attacking unit", cmds[other_unit].unit.id, "pot sup", cmds[pot_other_support].unit.id)
                                    if count < 2:   
                                        pot_other_suppoprt_success = det_valid_support
                                        count += 1
                                    else:
                                        cmd_success = True
                                    #else:
                                        #continue
                                else:
                                    continue
                            # check if anything supports the attack on supporting unit in question
                            # if yes => check if support is valid
                            # if support is valid => supporting unit in question is not successful
                            # if supporting the attacki is not valid => supporting unit in question is successful
                            print("check", unit_id, cmd_success)
                            #cmd_success = True
                        else:
                            cmd_success = False
                            break
                    else:
                        cmd_success = True
                else:
                    cmd_success = True
        print(unit_id, cmd_success)
        if cmd_success and cmd_obj.origin.is_occ != False:
            if cmd_obj.origin.is_occ == 1:
                origin = cmd_obj.origin
                for each_cmd in cmds:
                    if cmds[each_cmd] == origin:
                        sup_id = each_cmd
                        sup_obj = cmds[sup_id].origin.is_occ.id
                        break
            else:
                sup_id = cmd_obj.origin.is_occ.id
            sup_obj = cmds[sup_id]
            if sup_id in cmds:
                if sup_obj.loc != cmd_obj.loc:
                    if cmd_obj.origin and sup_obj.origin and sup_obj.destination == cmd_obj.destination:
                        cmd_strength = 1
                        sup_obj.cmd_strength(cmd_strength)
                    elif sup_obj.origin != sup_obj.destination and sup_obj.loc != sup_obj.origin:
                        cmd_strength = 1
                        sup_obj.cmd_strength(cmd_strength)
                    elif sup_obj.origin == sup_obj.destination and sup_obj.loc != sup_obj.origin:
                        cmd_strength = 1
                        sup_obj.cmd_strength(cmd_strength)
                    
                    else:
                        cmd_strength = 0
                else:
                    cmd_strength = 0
            else:
                cmd_strength = 0
    
        else:
            cmd_strength = 0
        cmd_obj.success(cmd_success)
    return cmds
"""







"""
def det_valid_support(cmds, id = None):
    # if there is a particular support to look at
    if id != None:
        unit_id = id
        cmd_obj = cmds[unit_id]
        cmd_success = is_support_cut(unit_id, cmds, True)
        cmd_strength = det_sup_strength(cmd_obj, cmd_success, cmds)
    else:
        for unit_id in cmds:
        # if a unit is attacking
            if cmds[unit_id].loc == cmds[unit_id].origin:
                continue
            cmd_obj = cmds[unit_id]
            cmd_success = is_support_cut(unit_id, cmds)
            cmd_strength = det_sup_strength(cmd_obj, cmd_success, cmds)
    return cmds


def is_support_cut(unit_id, cmds, recur_bool = None):
    cmd_obj = cmds[unit_id]
    if cmd_obj.loc != cmd_obj.origin:
        for other_unit in cmds:
            # if another unit attacks the supporting unit
            if cmd_obj.loc == cmds[other_unit].destination:
                if cmds[other_unit].loc == cmds[other_unit].origin:
                    # check if command supports an attack on the unit trying to cut support
                    if cmd_obj.destination == cmds[other_unit].loc:
                        #print("test 1", unit_id, other_unit)
                        for pot_other_support in cmds:
                        # if there is a command that's not the supporting unit or attacking unit
                        #if cmds[pot_other_support].loc != cmd_obj.loc and cmds[pot_other_support].loc != cmds[other_unit].loc:
                            # if the command is supporting an attack
                            if cmds[pot_other_support].loc != cmds[pot_other_support].origin and cmds[pot_other_support].origin != cmds[pot_other_support].destination:
                                #print("yes 1", "unit", unit_id, "attacking unit", cmds[other_unit].unit.id, "pot sup", cmds[pot_other_support].unit.id)
                                if recur_bool:
                                    cmd_success = True
                                else:
                                    other_success = pot_other_suppoprt_success = det_valid_support(cmds, unit_id)
                                    if other_success:
                                        cmd_success = True
                                    else:
                                        cmd_success = False
                                
                            #else:
                                #continue
                            else:
                                continue
                    # check if anything supports the attack on supporting unit in question
                    # if yes => check if support is valid
                    # if support is valid => supporting unit in question is not successful
                    # if supporting the attacki is not valid => supporting unit in question is successful
                        #print("check", unit_id, cmd_success)
                    #cmd_success = True
                    else:
                        cmd_success = False
                        break
                else:
                    cmd_success = True
            else:
                cmd_success = True
    #print(unit_id, cmd_success)
        
def det_sup_strength(cmd_obj, cmd_success, cmds):
    if cmd_success and cmd_obj.origin.is_occ != False:
        if cmd_obj.origin.is_occ == 1:
            origin = cmd_obj.origin
            for each_cmd in cmds:
                if cmds[each_cmd] == origin:
                    sup_id = each_cmd
                    sup_obj = cmds[sup_id].origin.is_occ.id
                    break
        else:
            sup_id = cmd_obj.origin.is_occ.id
        sup_obj = cmds[sup_id]
        if sup_id in cmds:
            if sup_obj.loc != cmd_obj.loc:
                if cmd_obj.origin and sup_obj.origin and sup_obj.destination == cmd_obj.destination:
                    cmd_strength = 1
                    sup_obj.cmd_strength(cmd_strength)
                elif sup_obj.origin != sup_obj.destination and sup_obj.loc != sup_obj.origin:
                    cmd_strength = 1
                    sup_obj.cmd_strength(cmd_strength)
                elif sup_obj.origin == sup_obj.destination and sup_obj.loc != sup_obj.origin:
                    cmd_strength = 1
                    sup_obj.cmd_strength(cmd_strength)    
                else:
                    cmd_strength = 0
            else:
                cmd_strength = 0
        else:
            cmd_strength = 0
    else:
        cmd_strength = 0
    cmd_obj.success(cmd_success)
    return cmd_obj.success
"""