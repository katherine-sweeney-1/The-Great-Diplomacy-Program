import sys
import os
"""
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/data/Hard_Data/Data_Game_1"))
from Cmdrs_1 import cmdrs_1
from Cmds_1 import cmds_1a, cmds_1b
from Units_1 import units_1a, units_1b
from Cmdrs_2 import cmdrs_2
from Cmds_2 import cmds_2a, cmds_2b
from Units_2 import units_2a, units_2b
from Cmdrs_3 import cmdrs_3
from Cmds_3 import cmds_3a
from Units_3 import units_3a
"""
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Parse"))
from Functions_Parse import parse_commands_and_units
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/data/Txt_Hard_Data"))
from Cmdrs_1 import cmdrs_1_1903, cmdrs_1_1904, cmdrs_1_1904b, cmdrs_1_1905, cmdrs_1_1906, cmdrs_1_1906b, cmdrs_1_1907, cmdrs_1_1907b, cmdrs_1_1908
from Cmdrs_2 import cmdrs_2_1901, cmdrs_2_1902, cmdrs_2_1903, cmdrs_2_1904
from Run_Objects import create_objects
from Run_Processing import run_processing
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Tables"))
from Functions_Table import yield_table

data_nodes = "data/Data_Ter_Main.csv"
data_coastal = "data/Data_Ter_Special_Coasts.csv"
commands_data = "data/Txt_Hard_Data/Game2_1904_Spring.txt"

def run_main_original():
    cmdrs_data_list = cmdrs_3
    cmds = cmds_3a
    units_data_list = units_3a
    commands, commanders, nodes, units = create_objects(data_nodes, data_coastal, cmdrs_data_list, units_data_list, cmds)
    nodes, units, processed_commands = run_processing(commands, commanders, nodes, units)
    db_table = yield_table(processed_commands)

def run_main_testing():
    commanders_data = cmdrs_2_1904
    parsed_cmds, parsed_units = parse_commands_and_units(commands_data)
    commands, commanders, nodes, units = create_objects(data_nodes, data_coastal, commanders_data, parsed_units, parsed_cmds)
    nodes, units, processed_commands = run_processing(commands, commanders, nodes, units)
    #db_table = yield_table(processed_commands)
