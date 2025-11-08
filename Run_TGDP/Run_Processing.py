import sys
import os
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Process_Moves"))
from Functions_Support import get_valid_support
from Functions_Attack import get_success_attacks
from Functions_Convoy import convoying_unit
from Functions_Post_Outcome import process_outcomes
sys.path.append(os.path.join("/home/katherine/Documents/The-Great-Diplomacy-Program/Process_Moves"))
from Functions_Filter import filter_commands

# need to include filter owners I think 
# do this later 
def run_processing(commands, commanders, nodes, units):
    valid_commands, invalid_commands = filter_commands(commands, commanders)
    valid_commands = get_valid_support(valid_commands)
    valid_commands = get_success_attacks(valid_commands)
    
    for id in commands:
        """
        if commands[id].succeed == commands[id].predet_outcome and commands[id].legal == 1:
           print(id, "Correct outcome", commands[id].succeed)
        else:
            print("uh oh", id, commands[id].strength, commands[id].legal, commands[id].succeed)
        """
        if commands[id].check_other_attacks == True:
            if commands[id].succeed == commands[id].predet_outcome and commands[id].legal == 1:
                print(id, "Correct outcome", commands[id].succeed)
            else:
                print("uh oh", id, commands[id].strength, commands[id].legal, commands[id].succeed)
        
    nodes, units = process_outcomes(valid_commands, nodes, units)
    return nodes, units, valid_commands


