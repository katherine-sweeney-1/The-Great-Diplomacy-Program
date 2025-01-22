def retrieve_cmd_dest_dict(cmds):
    cmd_dest_dict = {}
    for cmd in cmds:
        cmd_dest_dict[cmd] = cmds[cmd].destination
    return cmd_dest_dict

def check_other_attacks(cmd, dict_wo_cmd):
    for unit_id in dict_wo_cmd:
        other_cmd = dict_wo_cmd[unit_id]
        # another attack on destination => check other attacks
        if other_cmd.origin != cmd.origin and other_cmd.destination == cmd.destination:
            # strength is greater than other attack's strength => attack succeeds (for each other attack)
            if cmd.strength > other_cmd.strength:
                cmd.success(1)
            # other attack has higher strength => attack does not succeed
            else:
                cmd.success(0)
                break
        # no attack on destination => cmd succeeds
        else:
            cmd.success(1)
    #print("test", cmd.succeed)
    return cmd.succeed

def det_attack_outcome(unit_id, cmd, all_cmds):
    cmd.success(1)
    dict_wo_cmd = all_cmds.copy()
    dict_wo_cmd.pop(unit_id)
    # if destination is occupied
    if cmd.destination.is_occ != 0 and cmd.destination.is_occ != 1:
        #print(unit_id, cmd.destination.is_occ.id)
        unit_on_dest_id = cmd.destination.is_occ.id
        #if unit_on_dest_id in all_cmds:
        # if unit on destination attacks
        if cmd.loc == cmd.origin and cmd.origin != cmd.destination:
            if cmd in all_cmds and cmd.succeed == 1:
                unit_on_dest_outcome = det_attack_outcome (unit_on_dest_id, all_cmds[unit_on_dest_id])
            else:
                cmd.success(0)
            # unit on destination attacks succeeds => check for other attacks
            if cmd in all_cmds and unit_on_dest_outcome != 0:
                check_other_attacks(cmd, dict_wo_cmd)
            # unit on destination attack fails => command must have strength > 1 to succeed
            else:
                if cmd.strength > 1:
                    cmd.success(1)
                else:
                    cmd.success(0)
        # no attack from destination => check other attacks
        else:
            #unit_on_dest_id = unit_on_dest.id
            if cmd in all_cmds and cmd.strength > all_cmds[unit_on_dest_id].strength:
                check_other_attacks(cmd, dict_wo_cmd)
            else:
                cmd.success(0)
    else:
        check_other_attacks(cmd, dict_wo_cmd)
    return cmd

def det_success_attacks(commands):
    for unit_id in commands:
        cmd = commands[unit_id]
        cmd.success(1)
        if cmd.loc == cmd.origin and cmd.origin != cmd.destination:
            det_attack_outcome(unit_id, commands[unit_id], commands)
    return commands