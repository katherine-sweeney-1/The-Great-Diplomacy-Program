import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/data/Data_Set_1"))
from Commanders_1 import cmdrs_1
from Commands_1 import cmds_1
from Units_1 import units_1
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/data/Data_Set_2"))
from Commanders_2 import cmdrs_2
from Commands_2 import cmds_2
from Units_2 import units_2
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/data/Data_Set_3"))
from Commanders_3 import cmdrs_3
from Commands_3 import cmds_3a, cmds_3b
from Units_3 import units_3a, units_3b
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/data/Data_Set_4"))
from Commanders_4 import cmdrs_4
from Commands_4 import cmds_4a
from Units_4 import units_4a
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Commands"))
from Functions_Command import create_commands
#sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Commands"))
from Run_Functions import tgdp_objs
from Run_Functions import tgdp_filter_cmds
from Run_Functions import tgdp_process_cmds
from Run_Functions import tgdp_process_outcomes

data_nodes = "data/Data_Ter_Main.csv"
data_coastal = "data/Data_Ter_Special_Coasts.csv"

"""
cmdrs_data = cmdrs_3
cmds_data = cmds_3b
units_data = units_3b

commands, commanders, nodes, units = tgdp_objs(data_nodes, data_coastal, cmdrs_data, units_data, cmds_data)

valid_commands, invalid_commands = tgdp_filter_cmds(commands, commanders, nodes)

valid_commands = tgdp_process_cmds(valid_commands)

nodes, units = tgdp_process_outcomes(valid_commands, nodes, units)
"""

cmdrs_data_list = cmdrs_3
cmds_data_list = [cmds_3a, cmds_3b]
units_data_list = units_3a
turn_count = 1901

for cmds_data in cmds_data_list:
    if turn_count == 1901:
        commands, commanders, nodes, units = tgdp_objs(data_nodes, data_coastal, cmdrs_data_list, units_data_list, cmds_data)
    else:
        commands = create_commands(cmds_data, commanders, nodes, units)
    valid_commands, invalid_commands = tgdp_filter_cmds(commands, commanders, nodes)
    valid_commands = tgdp_process_cmds(valid_commands)
    nodes, units = tgdp_process_outcomes(valid_commands, nodes, units)
    turn_count = turn_count + 0.5
    print(turn_count)