def retrieve_cmd_dest_dict(cmds):
    cmd_dest_dict = {}
    for cmd in cmds:
        cmd_dest_dict[cmd] = cmds[cmd].destination
    return cmd_dest_dict

def det_valid_support(cmds):
    for unit_id in cmds:
        cmd_obj = cmds[unit_id]
        # if a support
        if cmd_obj.loc != cmd_obj.origin:
            # if another unit attacks the supporting unit
            for each in cmds:
                if cmds[each].destination == cmd_obj.loc and cmds[each].origin == cmd_obj.origin:
                    cmd_success = False
                    cmd_strength = 0
                    break
                else:
                    cmd_success = True
            if cmd_success:
                # add command strength if unit occupies the destination for support
                if cmd_obj.origin.is_occ != 0:
                    sup_id = cmd_obj.origin.is_occ.id
                    if sup_id in cmds:
                        if cmds[sup_id].destination == cmd_obj.destination and cmds[sup_id].origin != cmd_obj.origin:
                            cmd_strength = 0
                        else:
                            cmd_strength = 1
                        cmds[sup_id].cmd_strength(cmd_strength)
            cmd_obj.success(cmd_success)
    return cmds