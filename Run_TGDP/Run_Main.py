import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Data_Set_1"))
from Commanders_1 import cmdrs_1
from Commands_1 import cmds_1
from Units_1 import units_1
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Data_Set_2"))
from Commanders_2 import cmdrs_2
from Commands_2 import cmds_2
from Units_2 import units_2
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Commands"))
from Run_Functions import tgdp_objs
from Run_Functions import tgdp_filter_cmds
from Run_Functions import tgdp_process_cmds

data_nodes = "data/Data_Ter_Main.csv"
data_coastal = "data/Data_Ter_Special_Coasts.csv"

cmdrs_data = cmdrs_2
cmds_data = cmds_2
units_data = units_2

commands, commanders, nodes, units = tgdp_objs(data_nodes, data_coastal, cmdrs_data, units_data, cmds_data)

valid_commands, invalid_commands = tgdp_filter_cmds(commands, commanders, nodes)

valid_commands = tgdp_process_cmds(valid_commands)
"""
for each in valid_commands:
    print("outcome:", each, valid_commands[each].succeed)
"""

"""
for cmdr in commanders:
    commanders[cmdr].print_statements()

for each in units:
        print("CHECK", each, units[each], units[each].cmdr)
        print(units[each].cmdr.unit_members)
        print(" ")
    #units[unit].print_statements()

for node in nodes:
    nodes[node].print_statements()

for cmd in commands:
    commands[cmd].print_statement()
    #print(commands[cmd].legal)
"""