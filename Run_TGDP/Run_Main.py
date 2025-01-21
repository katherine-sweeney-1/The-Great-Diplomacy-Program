import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Units"))
from Hard_Data_Units import units_data_1 as units_1
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Commanders"))
from Hard_Data_Commanders import cmdrs_data_1 as cmdrs_1
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Commands"))
from Hard_Data_Commands import cmds_data_1 as cmds_1
from Run_Functions import tgdp_objs
from Run_Functions import tgdp_filter_cmds
from Run_Functions import tgdp_process_cmds

data_nodes = "data/Data_Ter_Main.csv"
data_coastal = "data/Data_Ter_Special_Coasts.csv"

commands, commanders, nodes, units = tgdp_objs(data_nodes, data_coastal, cmdrs_1, units_1, cmds_1)

valid_commands, invalid_commands = tgdp_filter_cmds(commands, commanders, nodes)

valid_commands = tgdp_process_cmds(valid_commands)

"""
for cmdr in commanders:
    commanders[cmdr].print_statements()

for unit in units:
    units[unit].print_statements()
    
for node in nodes:
    nodes[node].print_statements()

for cmd in commands:
    commands[cmd].print_statement()
    #print(commands[cmd].legal)
"""