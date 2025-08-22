import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Process_Moves"))
from Functions_Filter import filter_owner
from Functions_Filter import filter_unit_type
from Functions_Filter import filter_neighbors
from Functions_Support import get_valid_support
from Functions_Attack import get_success_attacks
from Functions_Convoy import convoying_unit
from Functions_Post_Outcome import get_outcome_locs
from Functions_Post_Outcome import get_retreats
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Tables"))
from Class_Table import Table
from Run_Objects import assign_occ

# Filter commands by who owns the units
def run_filter_owners(commands, commanders, units):
    valid_commands = {}
    invalid_commands = {}
    for cmding_unit in commands:
        cmd_obj = filter_owner(commands[cmding_unit], commanders, units)
        if cmd_obj.legal != 1:
            invalid_commands[cmding_unit] = cmd_obj
        else:
            valid_commands[cmding_unit] = cmd_obj
    return valid_commands, invalid_commands

# Filter commands for legal commands
def filter_cmds(commands, commanders, nodes):
    valid_commands = {}
    invalid_commands = {}
    for id in commands:
        command = commands[id]
        command = filter_owner(command, commanders)
        command = filter_unit_type(command)
        command = filter_neighbors(command, nodes)
        if command.legal != 1:
            invalid_commands[id] =command
            command.origin = command.loc
            command.destination = command.loc
            valid_commands[id] = command
        else:
            valid_commands[id] = command
    return valid_commands, invalid_commands

# Process commands
def process_cmds(commands):
    #commands = convoying_unit(commands)
    commands = get_valid_support(commands)
    #for c in commands:
        #print("check", c, commands[c].loc.name, commands[c].origin.name, commands[c].destination.name)
    commands = get_success_attacks(commands)
    for id in commands:
        if commands[id].succeed == commands[id].predet_outcome and commands[id].legal == 1:
           print(id, "Correct outcome", commands[id].succeed)
        else:
            print("uh oh", id, commands[id].strength, commands[id].legal, commands[id].succeed)
    return commands

#Process outcome locations and retreats
def process_outcomes(commands, nodes, units):
    units = get_outcome_locs(commands, nodes, units)
    units = get_retreats(units)
    for id in units:
        if units[id].retreat:
            retreat_choice = units[id].retreat[0]
            retreat_node = nodes[retreat_choice]
            units[id].assign_loc(retreat_node, False, False)
    nodes = assign_occ(nodes, units)
    return nodes, units

def yield_table (commands):
    db_table = Table()
    db_table.create_table()
    db_table.save(commands)
    return db_table
