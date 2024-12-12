
from Commander_Class_Helper_Functions import get_ters, check_node_printing


class Commander ():

    """
        human => string
        country => string
        unit members => list of unit objects 
            1. need to create unit objects
            2. create commander class property to get the unit objects
        own_dot_ters => list of territory objects
        occ_dot_ters => list of territory objects
    """

    def __init__ (self, human, country, unit_members, owned_dots, occ_ters):
        self.human = human
        self.country = country
        self.unit_members = unit_members
        self.own_dots = owned_dots
        self.occ_ters = occ_ters

    def get_ter_obj (self):
        return "hello world"

    def verify_commander (self, person_giving_orders):
        if  person_giving_orders == self.human:
            return "Valid"
        else:
            return "Invalid"
    
    def get_own_dots(self):
        own_dots = get_ters(self.own_dots)
        self.own_dots = own_dots

    def get_occ_ters(self):
        occ_ters = get_ters(self.occ_ters)
        self.occ_ters = occ_ters