import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Process_Moves"))
from Functions_Filter import filter_owner
from Functions_Filter import filter_unit_type
from Functions_Filter import filter_neighbors
from Functions_Support import det_valid_support
from Functions_Attack import det_success_attacks
from Functions_Convoy import convoying_unit
from Functions_Post_Outcome import det_outcome_locs
from Functions_Post_Outcome import det_retreats
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Tables"))
from Class_Table import Table
from Run_Objects import assign_occ

# Filter commands by who owns the units
def run_filter_owners(commands, commanders, units):
    valid_cmds = {}
    invalid_cmds = {}
    for cmding_unit in commands:
        cmd_obj = filter_owner(commands[cmding_unit], commanders, units)
        if cmd_obj.legal != 1:
            invalid_cmds[cmding_unit] = cmd_obj
        else:
            valid_cmds[cmding_unit] = cmd_obj
    return valid_cmds, invalid_cmds

# Filter commands for legal commands
def tgdp_filter_cmds(commands, commanders, nodes):
    valid_cmds = {}
    invalid_cmds = {}
    for cmding_unit in commands:
        cmd_obj = commands[cmding_unit]
        cmd_obj = filter_owner(cmd_obj, commanders)
        cmd_obj = filter_unit_type(cmd_obj)
        cmd_obj = filter_neighbors(cmd_obj, nodes)
        if cmd_obj.legal != 1:
            invalid_cmds[cmding_unit] = cmd_obj
            cmd_obj.origin = cmd_obj.loc
            cmd_obj.destination = cmd_obj.loc
            valid_cmds[cmding_unit] = cmd_obj
        else:
            valid_cmds[cmding_unit] = cmd_obj
    return valid_cmds, invalid_cmds

# Process commands
def tgdp_process_cmds(commands):
    #commands = convoying_unit(commands)
    commands = det_valid_support(commands)
    commands = det_success_attacks(commands)
    for unit_id in commands:
       print(unit_id, commands[unit_id].strength, commands[unit_id].legal, commands[unit_id].succeed)
    return commands

#Process outcome locations and retreats
def tgdp_process_outcomes(commands, nodes, units, db, turn_count):
    units = det_outcome_locs(commands, nodes, units)
    units = det_retreats(units)
    for each in units:
        unit = units[each]
        unit.create_table(db)
        unit.save(db)
        if unit.retreat:
            retreat_choice = unit.retreat[0]
            retreat_node = nodes[retreat_choice]
            unit.assign_loc(retreat_node, False, False)
    db_table = Table(turn_count)
    db_table.create_table(db)
    db_table.save(db, commands)
    nodes = assign_occ(nodes, units)
    return nodes, units
