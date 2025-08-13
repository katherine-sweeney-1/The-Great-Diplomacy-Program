def retrieve_cmd_dest_dict(cmds):
    cmd_dest_dict = {}
    for cmd in cmds:
        cmd_dest_dict[cmd] = cmds[cmd].destination
    return cmd_dest_dict

def det_valid_support(cmds):
    for unit_id in cmds:
        #print("test", unit_id)
        if cmds[unit_id].loc == cmds[unit_id].origin:
            continue
        cmd_obj = cmds[unit_id]
        # if a support
        #print("test")
        if cmd_obj.loc != cmd_obj.origin:
            #print("test 1")
            # if another unit attacks the supporting unit
            for each in cmds:
                if cmds[each].destination == cmd_obj.loc:
                    if cmds[each].loc == cmds[each].origin:
                        cmd_success = False
                        break
                    else:
                        cmd_success = True
                        print("yes")
                else:
                    cmd_success = True
                    #print("yessss")
                #print("test")
        #the origin is occupied is not being ran
        print(cmd_obj.origin.is_occ, cmd_obj.loc.name, cmd_obj.origin.name)
        if cmd_success and cmd_obj.origin.is_occ != False:
            #print("check")
            if cmd_obj.origin.is_occ == 1:
                origin = cmd_obj.origin
                for each_cmd in cmds:
                    if cmds[each_cmd] == origin:
                        sup_id = each
                        sup_obj = cmds[sup_id].origin.is_occ.id
                        break
            else:
                sup_id = cmd_obj.origin.id
            sup_obj = cmds[sup_id]
            #print(cmds, sup_id)
            if sup_id in cmds:
                #print("yes", sup_id)
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
                    #print("check func support", unit_id, sup_obj.strength)
                else:
                    cmd_strength = 0
            else:
                cmd_strength = 0
    
        else:
            cmd_strength = 0
        cmd_obj.success(cmd_success)
        #print("test", unit_id, sup_obj.unit_id, sup_obj.strength)
    return cmds