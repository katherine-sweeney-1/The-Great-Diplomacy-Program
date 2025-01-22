def retrieve_cmd_dest_dict(cmds):
    cmd_dest_dict = {}
    for cmd in cmds:
        cmd_dest_dict[cmd] = cmds[cmd].destination
    return cmd_dest_dict

def det_valid_support(cmds):
    cmd_origin_dict = retrieve_cmd_dest_dict(cmds)
    for unit_id in cmds:
        cmd_obj = cmds[unit_id]
        dict_wo_specified_cmd = cmd_origin_dict.copy()
        dict_wo_specified_cmd.pop(unit_id)
        # if a support
        if cmd_obj.loc != cmd_obj.origin:
            # if another unit attacks the supporting unit
            if cmd_obj.loc in dict_wo_specified_cmd.values():
                cmd_success = 0
            else:
                cmd_success = 1
                # add command strength if unit occupies the destination for support
                if cmd_obj.origin.is_occ != 0:
                    supported_unit_id = cmd_obj.origin.is_occ.id
                    if dict_wo_specified_cmd[supported_unit_id] == cmd_obj.destination:
                        cmds[supported_unit_id].cmd_strength(cmd_success)
            cmd_obj.success(cmd_success)
    return cmds