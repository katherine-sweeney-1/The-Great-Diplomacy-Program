from Hard_Data_Commanders import cmdrs_data_1 as data
from Functions_Commander import create_commanders

commanders = create_commanders(data)

"""
print(commanders)                                       #check list of commanders is correct 
for each_cmdr in commanders:
    print(each_cmdr.human, each_cmdr.country)
"""
