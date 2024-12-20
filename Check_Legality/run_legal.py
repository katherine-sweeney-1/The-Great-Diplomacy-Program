
import sys
import os

sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy\\Command"))
from Functions_Command import run_commands
from Hard_Data_Commands import cmds_data_1

from functions_legal import run_check_legal

commands = run_commands(cmds_data_1)

legal_commands = run_check_legal(commands)


