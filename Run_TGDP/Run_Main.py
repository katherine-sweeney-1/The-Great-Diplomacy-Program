import sys
sys.path.append("../The_Great_Diplomacy_Program/Parse")
from Parse_Objects import parse_commands_and_units
sys.path.append("../The_Great_Diplomacy_Program/data/Txt_Hard_Data")
from Cmdrs_1 import cmdrs_1_1903, cmdrs_1_1904, cmdrs_1_1904b, cmdrs_1_1905, cmdrs_1_1906, cmdrs_1_1906b, cmdrs_1_1907, cmdrs_1_1907b, cmdrs_1_1908
from Cmdrs_2 import cmdrs_2_1901, cmdrs_2_1902, cmdrs_2_1903, cmdrs_2_1904, cmdrs_2_1904b, cmdrs_2_1905, cmdrs_2_1906, cmdrs_2_1907
from Cmdrs_3 import cmdrs_3_1901, cmdrs_3_1902, cmdrs_3_1903, cmdrs_3_1904, cmdrs_3_1905, cmdrs_3_1906, cmdrs_3_1907, cmdrs_3_1907b
from Run_Objects import create_objects
from Run_Processing import run_processing
sys.path.append("../The_Great_Diplomacy_Program/Tables")
from Functions_Table import yield_table

data_nodes = "data/Data_Ter_Main.csv"
data_coastal = "data/Data_Ter_Special_Coasts.csv"
data_fleet_coastal = "data/Data_Ter_Fleet.csv"
commands_data = "data/Txt_Hard_Data/Game2_1906_Fall.txt"

input_data_1 = {}
input_data_1["data/Txt_Hard_Data/Game1_1903_Spring.txt"] = cmdrs_1_1903
input_data_1["data/Txt_Hard_Data/Game1_1903_Fall.txt"] = cmdrs_1_1903
input_data_1["data/Txt_Hard_Data/Game1_1904_Spring.txt"] = cmdrs_1_1904
input_data_1["data/Txt_Hard_Data/Game1_1904_Fall.txt"] = cmdrs_1_1904b
input_data_1["data/Txt_Hard_Data/Game1_1905_Spring.txt"] = cmdrs_1_1905
input_data_1["data/Txt_Hard_Data/Game1_1905_Fall.txt"] = cmdrs_1_1905
input_data_1["data/Txt_Hard_Data/Game1_1906_Spring.txt"] = cmdrs_1_1906
input_data_1["data/Txt_Hard_Data/Game1_1906_Fall.txt"] = cmdrs_1_1906b
input_data_1["data/Txt_Hard_Data/Game1_1907_Spring.txt"] = cmdrs_1_1907
input_data_1["data/Txt_Hard_Data/Game1_1907_Fall.txt"] = cmdrs_1_1907b
input_data_1["data/Txt_Hard_Data/Game1_1908_Spring.txt"] = cmdrs_1_1908

input_data_2 = {}
input_data_2["data/Txt_Hard_Data/Game2_1901_Spring.txt"] = cmdrs_2_1901
input_data_2["data/Txt_Hard_Data/Game2_1901_Fall.txt"] = cmdrs_2_1901
input_data_2["data/Txt_Hard_Data/Game2_1902_Spring.txt"] = cmdrs_2_1902
input_data_2["data/Txt_Hard_Data/Game2_1902_Fall.txt"] = cmdrs_2_1902
input_data_2["data/Txt_Hard_Data/Game2_1903_Spring.txt"] = cmdrs_2_1903
input_data_2["data/Txt_Hard_Data/Game2_1903_Fall.txt"] = cmdrs_2_1903
input_data_2["data/Txt_Hard_Data/Game2_1904_Spring.txt"] = cmdrs_2_1904
input_data_2["data/Txt_Hard_Data/Game2_1904_Fall.txt"] = cmdrs_2_1904b
input_data_2["data/Txt_Hard_Data/Game2_1905_Spring.txt"] = cmdrs_2_1905
input_data_2["data/Txt_Hard_Data/Game2_1905_Fall.txt"] = cmdrs_2_1905
input_data_2["data/Txt_Hard_Data/Game2_1906_Spring.txt"] = cmdrs_2_1906
input_data_2["data/Txt_Hard_Data/Game2_1906_Fall.txt"] = cmdrs_2_1906
input_data_2["data/Txt_Hard_Data/Game2_1907_Spring.txt"] = cmdrs_2_1907

input_data_3 = {}
input_data_3["data/Txt_Hard_Data/Game3_1901_Spring.txt"] = cmdrs_3_1901
input_data_3["data/Txt_Hard_Data/Game3_1901_Fall.txt"] = cmdrs_3_1901
input_data_3["data/Txt_Hard_Data/Game3_1902_Spring.txt"] = cmdrs_3_1902
input_data_3["data/Txt_Hard_Data/Game3_1902_Fall.txt"] = cmdrs_3_1902
input_data_3["data/Txt_Hard_Data/Game3_1903_Spring.txt"] = cmdrs_3_1903
input_data_3["data/Txt_Hard_Data/Game3_1903_Fall.txt"] = cmdrs_3_1903
input_data_3["data/Txt_Hard_Data/Game3_1904_Spring.txt"] = cmdrs_3_1904
input_data_3["data/Txt_Hard_Data/Game3_1904_Fall.txt"] = cmdrs_3_1904
input_data_3["data/Txt_Hard_Data/Game3_1905_Spring.txt"] = cmdrs_3_1905
input_data_3["data/Txt_Hard_Data/Game3_1905_Fall.txt"] = cmdrs_3_1905
input_data_3["data/Txt_Hard_Data/Game3_1906_Spring.txt"] = cmdrs_3_1906
input_data_3["data/Txt_Hard_Data/Game3_1906_Fall.txt"] = cmdrs_3_1906
input_data_3["data/Txt_Hard_Data/Game3_1907_Spring.txt"] = cmdrs_3_1907
input_data_3["data/Txt_Hard_Data/Game3_1907_Fall.txt"] = cmdrs_3_1907b

def run_main_original():
    cmdrs_data_list = cmdrs_3
    cmds = cmds_3a
    units_data_list = units_3a
    commands, commanders, nodes, units = create_objects(data_nodes, data_coastal, cmdrs_data_list, units_data_list, cmds)
    nodes, units, processed_commands = run_processing(commands, commanders, nodes, units)
    db_table = yield_table(processed_commands)

def run_main_testing():
    commanders_data = cmdrs_2_1906
    parsed_cmds, parsed_units = parse_commands_and_units(commands_data)
    commands, commanders, nodes, units = create_objects(data_nodes, data_coastal, data_fleet_coastal, commanders_data, parsed_units, parsed_cmds)
    nodes, units, processed_commands = run_processing(commands, commanders, nodes, units)
    #db_table = yield_table(processed_commands)


def run_main_unit_testing(input_data):
    count = 0
    for commands_data in input_data:
        game_year = 1901 + count/2
        game_year = int(game_year)
        game_season = count % 2
        if game_season == 0:
            game_season = "Spring"
        if game_season != "Spring":
            game_season = "Fall"
        commanders_data = input_data[commands_data]
        parsed_cmds, parsed_units = parse_commands_and_units(commands_data)
        commands, commanders, nodes, units = create_objects(data_nodes, data_coastal, data_fleet_coastal, commanders_data, parsed_units, parsed_cmds)
        print("Game 2 {} {}".format(game_year, game_season))
        nodes, units, processed_commands = run_processing(commands, commanders, nodes, units)
        print(" ")
        count += 1

run_main_unit_testing(input_data_3)
