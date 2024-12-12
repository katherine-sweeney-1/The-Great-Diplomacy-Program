
from Commander_Class_Helper_Functions import get_ters, check_node_printing

class Commander ():

    def __init__ (self, human, country, unit_members, owned_dots, occ_ters):
        self.human = human                              # string 
        self.country = country                          # string
        self.unit_members = unit_members                # unit object
        self.own_dots = owned_dots                      # node object
        self.occ_ters = occ_ters                        # node object
    
    def get_own_dots(self):                             # retrieve node objects for dots owned
        own_dots = get_ters(self.own_dots)
        self.own_dots = own_dots

    def get_occ_ters(self):                             # retrieve node objects for occupied territories
        occ_ters = get_ters(self.occ_ters)
        self.occ_ters = occ_ters