import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/data/Data_Game_1"))
from Cmdrs_1 import cmdrs_1
from Cmds_1 import cmds_1a, cmds_1b
from Units_1 import units_1a, units_1b
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Commands"))
from Functions_Command import create_commands 
from Run_Objects import tgdp_objs
from Run_Processing import filter_cmds
from Run_Processing import process_cmds
from Run_Processing import process_outcomes
from Run_Processing import yield_table

data_nodes = "data/Data_Ter_Main.csv"
data_coastal = "data/Data_Ter_Special_Coasts.csv"

cmdrs_data_list = cmdrs_1
cmds = cmds_1b
units_data_list = units_1b
turn_count = 1901.5

def run_main():
    # Create objects
    commands, commanders, nodes, units = tgdp_objs(data_nodes, data_coastal, cmdrs_data_list, units_data_list, cmds)
    # Determine and process valid commands
    valid_commands, invalid_commands = filter_cmds(commands, commanders, nodes)
    valid_commands = process_cmds(valid_commands)
    # Update nodes and units
    # sql database to store outcomes
    nodes, units = process_outcomes(valid_commands, nodes, units)
    db_table = yield_table(valid_commands)