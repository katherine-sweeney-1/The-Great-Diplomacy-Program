import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Units"))
from Hard_Data_Units import units_data_1
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Commanders"))
from Functions_Commander import create_commanders
from Hard_Data_Commanders import cmdrs_data_1
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Commands"))
from Functions_Command import create_commands
from Hard_Data_Commands import cmds_data_1

from Run_Functions import run_create_nodes
from Run_Functions import coastal_node_assign_occ
from Run_Functions import update_commanders
from Run_Functions import update_units
from Run_Functions import filter_unit_type

data_nodes_main = "data/Data_Ter_Main.csv"
data_nodes_coastal = "data/Data_Ter_Special_Coasts.csv"

commanders = create_commanders(cmdrs_data_1)

nodes = run_create_nodes(data_nodes_main, data_nodes_coastal)

commanders, units = update_commanders(commanders, nodes, cmdrs_data_1, units_data_1)

units = update_units(units)

nodes = coastal_node_assign_occ(nodes)

commands = create_commands(cmds_data_1, commanders, units, nodes)

commands = filter_unit_type(commands)


"""
for cmdr in commanders:
    commanders[cmdr].print_statements()

for unit in units:
    units[unit].print_statements()

for node in nodes:
    nodes[node].print_statements()

for cmd in commands:
    commands[cmd].print_statement()
    print(commands[cmd].legal)
"""


