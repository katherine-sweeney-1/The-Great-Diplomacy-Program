def retrieve_cmd_dest_dict(cmds):
    cmd_dest_dict = {}
    for cmd in cmds:
        cmd_dest_dict[cmd] = cmds[cmd].destination
    return cmd_dest_dict

def det_valid_support(cmds):
    for unit_id in cmds:
        if cmds[unit_id].loc == cmds[unit_id].origin:
            continue
        cmd_obj = cmds[unit_id]
        # if a support
        if cmd_obj.loc != cmd_obj.origin:
            # if another unit attacks the supporting unit
            for each in cmds:
                if cmds[each].destination == cmd_obj.loc:# and cmds[each].origin == cmd_obj.origin:
                    if cmds[each].loc == cmds[each].origin:
                        cmd_success = False
                        #print("aye", unit_id, each)
                        break
                    else:
                        cmd_success = True
                else:
                    cmd_success = True
        if cmd_success and cmd_obj.origin.is_occ:
            if cmd_obj.origin.is_occ == 1:
                #print("YO", unit_id, cmd_obj.origin.name)
                origin = cmd_obj.origin
                for each_cmd in cmds:
                    if cmds[each_cmd] == origin:
                        sup_id = each
                        sup_obj = cmds[sup_id].origin.is_occ
                        #print("aye", unit_id, each)
                        break
            else:
                sup_id = cmd_obj.origin.is_occ.id
            sup_obj = cmds[sup_id]
            if sup_id in cmds:
                """
                if cmds[sup_id].destination == cmd_obj.destination and cmds[sup_id].origin == cmd_obj.origin:
                    if cmds[sup_id].loc != cmd_obj.loc:
                        cmd_strength = 1
                        cmds[sup_id].cmd_strength(cmd_strength)
                        print(unit_id, sup_id, cmds[sup_id].strength)
                """
                if sup_obj.loc != cmd_obj.loc:
                    """
                        if sup_obj.destination == cmd_obj.destination and sup_obj.origin == cmd_obj.origin:
                            cmd_strength = 1
                            sup_obj.cmd_strength(cmd_strength)
                        elif sup_obj.origin != sup_obj.destination and sup_obj.loc != sup_obj.origin:
                            cmd_strength = 1
                            sup_obj.cmd_strength(cmd_strength)
                        elif cmd_obj.loc == cmd_obj.origin and cmd_obj.origin == cmd_obj.destination:
                            cmd_strength = 1
                            sup_obj.cmd_strength(cmd_strength)
                        """
                    # support an attack
                    if cmd_obj.origin and sup_obj.origin and sup_obj.destination == cmd_obj.destination:
                        print("TEST 1")
                        cmd_strength = 1
                        sup_obj.cmd_strength(cmd_strength)
                    # support a unit who holds
                    # support a hold for a unit who supports an attack
                    elif sup_obj.origin != sup_obj.destination and sup_obj.loc != sup_obj.origin:
                        print("TEST 2")
                        cmd_strength = 1
                        sup_obj.cmd_strength(cmd_strength)
                    #elif cmd_obj.loc == cmd_obj.origin and cmd_obj.origin == cmd_obj.destination:
                        #print("TEST 3")
                        #cmd_strength = 1
                        #sup_obj.cmd_strength(cmd_strength)
                    # supporting a hold
                    #elif cmd_obj.origin == sup_obj.origin and sup_obj.destination == sup_obj.origin:
                    elif sup_obj.origin == sup_obj.destination and sup_obj.loc != sup_obj.origin:
                        cmd_strength = 1
                        print("TEST 3")
                        sup_obj.cmd_strength(cmd_strength)
                        
                    else:
                        cmd_strength = 0
                        #print("oof", unit_id, sup_id, sup_obj.strength)
                else:
                    cmd_strength = 0
            else:
                cmd_strength = 0
    
        else:
            cmd_strength = 0
        #cmds[sup_id].cmd_strength(cmd_strength)
        cmd_obj.success(cmd_success)
        #print(unit_id, cmd_obj.succeed)
        #if cmd_success:
    """
            # add command strength if unit occupies the destination for support
            if cmd_obj.origin.is_occ:
                if cmd_obj.origin.is_occ == 1:
                    origin = cmd_obj.origin
                    for each_cmd in cmds:
                        if cmds[each_cmd] == origin:
                            sup_id = each_cmd
                            break
                        else:
                            continue
                else:
                    sup_id = cmd_obj.origin.is_occ.id
                #sup_id = cmd_obj.origin.is_occ
                if sup_id in cmds:
                    if cmds[sup_id].destination == cmd_obj.destination and cmds[sup_id].origin == cmd_obj.origin:
                        cmd_strength = 1
                    else:
                        cmd_strength = 0
                else:
                    cmd_strength = 0
                cmds[sup_id].cmd_strength(cmd_strength)
            """
        #cmd_obj.success(cmd_success)
    return cmds


    if cmd.destination.is_occ:
        # special case node occupied => get id for unit on special case node
        if cmd.destination.is_occ == 1:
            destination_node = cmd.destination
            for each_cmd in all_cmds:
                if all_cmds[each_cmd].loc == destination_node:
                    unit_dest_id = each_cmd
                    break
        # regular case node occupied => get id for unit on node
        else:
            unit_dest_id = cmd.destination.is_occ.id