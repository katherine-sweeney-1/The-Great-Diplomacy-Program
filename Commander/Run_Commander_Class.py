
from Commander_Hard_Data import Commander_Data_1 as data
from Functions_Commander import run_create_commander

commanders = run_create_commander(data)

"""
print(commanders)                                       #check list of commanders is correct 
for each_cmdr in commanders:
    print(each_cmdr.human, each_cmdr.country)
"""
