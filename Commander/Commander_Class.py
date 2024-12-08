
class Commander ():

    def __init__ (self, human, country, unit_members, dots):
        self.human = human
        self.country = country
        self.unit_members = unit_members
        self.dots = dots

    def verify_commander (self, person_giving_orders):
        if  person_giving_orders == self.human:
            return "Valid Commander"
        else:
            return "Invalid Commander"
