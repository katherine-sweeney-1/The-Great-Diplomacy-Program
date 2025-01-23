def retrieve_cmd_dest_dict(cmds):
    cmd_dest_dict = {}
    for cmd in cmds:
        cmd_dest_dict[cmd] = cmds[cmd].destination
    return cmd_dest_dict
"""
def det_valid_supportu(cmds):
    cmd_origin_dict = retrieve_cmd_dest_dict(cmds)
    for unit_id in cmds:
        cmd_obj = cmds[unit_id]
        dict_wo_cmd = cmd_origin_dict.copy()
        dict_wo_cmd.pop(unit_id)
        # if a support
        if cmd_obj.loc != cmd_obj.origin:
            # if another unit attacks the supporting unit
            if cmd_obj.loc in dict_wo_cmd.values():
                cmd_success = False
                cmd_strength = 0
            else:
                cmd_success = True
                cmd_strength = 1
                # add command strength if unit occupies the destination for support
                if cmd_obj.origin.is_occ != 0:
                    sup_obj = cmd_obj.origin.is_occ
                    print("obh", sup_obj, sup_obj.id)
                    print(dict_wo_cmd)
                    if sup_obj in dict_wo_cmd:
                        print("YAY", sup_obj.id)
                    #sup_obj = dict_wo_cmd[sup_id]
                    #if cmd_obj in dict_wo_specified_cmd.values() and dict_wo_specified_cmd[sup_id]== cmd_obj.destination:
                    if sup_obj in dict_wo_cmd and sup_obj.destination == cmd_obj.destination:# and sup_obj.origin == cmd_obj.origin:
                        sup_obj.cmd_strength(cmd_strength)
                        print("check 2")
            cmd_obj.success(cmd_success)
    return cmds


def det_valid_support(unit_id, cmds):
    #other_cmds = retrieve_cmd_dest_dict(cmds)
    cmd_obj = cmds[unit_id]
    #cmds.pop(unit_id)
    # if a support
    for cmd in cmds:
        if cmd_obj.loc != cmd_obj.origin:
            # if another unit attacks the supporting unit
            if cmd_obj.loc in cmds.values():
                cmd_success = False
                cmd_strength = 0
            else:
                cmd_success = True
                cmd_strength = 1
                # add command strength if unit occupies the destination for support
                if cmd_obj.origin.is_occ != 0:
                    sup_obj = cmd_obj.origin.is_occ
                    print("obh", sup_obj, sup_obj.id)
                    print(cmds)
                    if sup_obj in cmds.values():
                        print("YAY", sup_obj.id)
                    #sup_obj = dict_wo_cmd[sup_id]
                    #if cmd_obj in dict_wo_specified_cmd.values() and dict_wo_specified_cmd[sup_id]== cmd_obj.destination:
                        if sup_obj.destination == cmd_obj.destination:# and sup_obj.origin == cmd_obj.origin:
                            sup_obj.cmd_strength(cmd_strength)
                            print("check 2")
            cmd_obj.success(cmd_success)
    return cmds
"""
def det_valid_support(cmds):
    for unit_id in cmds:

        cmd_obj = cmds[unit_id]
        # if a support
        if cmd_obj.loc != cmd_obj.origin:
            # if another unit attacks the supporting unit
            for each in cmds:
                if cmds[each].destination == cmd_obj.loc and cmds[each].origin == cmd_obj.origin:
                    #print("FAIL", unit_id)
                    cmd_success = False
                    cmd_strength = 0
                    break
                else:
                    cmd_success = True
                    #print("SUCCESS", unit_id)
                    #cmd_strength = 1
            if cmd_success:
                # add command strength if unit occupies the destination for support
                if cmd_obj.origin.is_occ != 0:
                    sup_id = cmd_obj.origin.is_occ.id
                    #print("obh", sup_id)
                    
                    if sup_id in cmds:
                        #print("YAY", sup_id, cmds[sup_id])
                    #sup_obj = dict_wo_cmd[sup_id]
                    #if cmd_obj in dict_wo_specified_cmd.values() and dict_wo_specified_cmd[sup_id]== cmd_obj.destination:
                    #if sup_obj in dict_wo_cmd and sup_obj.destination == cmd_obj.destination:# and sup_obj.origin == cmd_obj.origin:
                        if cmds[sup_id].destination == cmd_obj.destination and cmds[sup_id].origin != cmd_obj.origin:
                            cmd_strength = 0
                            #print("AFKJAWFKJWFJLHWAELJJLWAEFJ")
                        else:
                            cmd_strength = 1
                        cmds[sup_id].cmd_strength(cmd_strength)
                        #print("check 2")
            #print(unit_id, cmd_success)
            cmd_obj.success(cmd_success)
    return cmds