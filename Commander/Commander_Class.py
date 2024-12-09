
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


    def verify_commander (self, person_giving_orders):
        if  person_giving_orders == self.human:
            return "Valid"
        else:
            return "Invalid"