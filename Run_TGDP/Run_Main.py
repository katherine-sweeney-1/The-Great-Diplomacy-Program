import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/data/Data_Game_1"))
from Cmdrs_1 import cmdrs_1
from Cmds_1 import cmds_1a, cmds_1b
from Units_1 import units_1a, units_1b
from Cmdrs_2 import cmdrs_2
from Cmds_2 import cmds_2a, cmds_2b
from Units_2 import units_2a, units_2b
from Cmdrs_3 import cmdrs_3
from Cmds_3 import cmds_3a
from Units_3 import units_3a
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/data/Parsing_Data"))
from Functions_Parse import parse_cmds_units
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Commands"))
from Functions_Command import create_commands 
from Run_Objects import tgdp_objs
from Run_Processing import filter_cmds
from Run_Processing import process_cmds
from Run_Processing import process_outcomes
from Run_Processing import yield_table

data_nodes = "data/Data_Ter_Main.csv"
data_coastal = "data/Data_Ter_Special_Coasts.csv"
cmds_data = "data/Game1_Spring1903.txt"

def run_main_original():
    cmdrs_data_list = cmdrs_3
    cmds = cmds_3a
    units_data_list = units_3a
    #parsed_cmds, parsed_units = parse_cmds_units(cmds_data)
    # Create objects
    commands, commanders, nodes, units = tgdp_objs(data_nodes, data_coastal, cmdrs_data_list, units_data_list, cmds)
    # Determine and process valid commands
    valid_commands, invalid_commands = filter_cmds(commands, commanders, nodes)
    valid_commands = process_cmds(valid_commands)
    # Update nodes and units
    # sql database to store outcomes
    nodes, units = process_outcomes(valid_commands, nodes, units)
    db_table = yield_table(valid_commands)


def run_main_testing():
    cmdrs_data_list = cmdrs_3
    parsed_cmds, parsed_units = parse_cmds_units(cmds_data)
    #for each in parsed_units:
        #print(each, parsed_units[each])
    # Create objects
    commands, commanders, nodes, units = tgdp_objs(data_nodes, data_coastal, cmdrs_data_list, parsed_units, parsed_cmds)
    # Determine and process valid commands
    valid_commands, invalid_commands = filter_cmds(commands, commanders, nodes)
    valid_commands = process_cmds(valid_commands)
    # Update nodes and units
    # sql database to store outcomes
    nodes, units = process_outcomes(valid_commands, nodes, units)
    db_table = yield_table(valid_commands)

# add a success or fail check function eventually