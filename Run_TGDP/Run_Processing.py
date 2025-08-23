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
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Process_Moves"))
from Functions_Filter import filter_cmds

# Process commands
def process_cmds(commands):
    #commands = convoying_unit(commands)
    commands = get_valid_support(commands)
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

# need to include filter owners I think 
# do this later 
def tgdp_processing(commands, commanders, nodes, units):
    valid_commands, invalid_commands = filter_cmds(commands, commanders, nodes)
    valid_commands = process_cmds(valid_commands)
    nodes, units = process_outcomes(valid_commands, nodes, units)
    return nodes, units, valid_commands

def yield_table (commands):
    db_table = Table()
    db_table.create_table()
    db_table.save(commands)
    return db_table
