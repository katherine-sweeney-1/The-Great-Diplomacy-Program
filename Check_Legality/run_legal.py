
import sys
import os

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Command"))
from Functions_Command import create_commands
from Hard_Data_Commands import cmds_data_1

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Commander"))
from Functions_Commander import create_commanders
from Hard_Data_Commanders import cmdrs_data_1

from functions_legal import run_check_legal

commands = create_commands(cmds_data_1)

commanders = create_commanders(cmdrs_data_1)

legal_commands = run_check_legal(commands)
