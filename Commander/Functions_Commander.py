
from Commander_Class import Commander

def create_commander (indiv_key, nested_info):
    commander = Commander(indiv_key, 
                                nested_info["Country"], 
                                nested_info["Unit Members"],
                                nested_info["Dots Owned"],
                                nested_info["Dots Occ"])
    return commander

def check_class_works(cmdr_object):
    print("commander {} has dots in territories {}".
          format(cmdr_object.human, cmdr_object.own_dots))
    print("commander {} occupies territories {}".format(cmdr_object.human, cmdr_object.occ_ters))
    print(" ")

def run_create_commander (commander_data):
    for each_key in commander_data:
        indiv_cmdr = create_commander(each_key, commander_data[each_key])
        indiv_cmdr.get_own_dots()
        indiv_cmdr.get_occ_ters()
        check_class_works(indiv_cmdr)