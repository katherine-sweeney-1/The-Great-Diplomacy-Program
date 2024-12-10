
import sys
import os
sys.path.append(os.path.join("C:\\Users\\kathe\\Documents\\Py_Code\\Diplomacy"))
from Territories import Nodes_Class
from Territories import Nodes_Main


class Commander ():

    """
        human => string
        country => string
        unit members => list of unit objects?
        own_dot_ters => list of territory objects?
        occ_dot_ters => list of territory objects?
    """

    def __init__ (self, human, country, unit_members, owned_dots, occ_dots):
        self.human = human
        self.country = country
        self.unit_members = unit_members
        self.own_dots = owned_dots
        self.occ_dots = occ_dots

# want to use the node class to create the node object and have those objects be
# the self.own_dots and self.occ_dots
# need to grab the info from the csv file lines and use that as input to get the node
# do the same thing for units eventuall
    def get_ter_obj (self):

        return "hello world"


    def verify_commander (self, person_giving_orders):
        if  person_giving_orders == self.human:
            return "Valid"
        else:
            return "Invalid"
        
    #add get territories property