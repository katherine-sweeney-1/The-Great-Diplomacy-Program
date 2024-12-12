


class Unit ():
    
    def __init__ (self, id, type, loc, commander, command):
        self.id = id
        self.type = type
        self.loc = loc
        self.commander = commander
        self.command = command

    def verify_unit (self, possible_commander):
        if self.id in possible_commander.unit_members:
            return "Valid"
        else: 
            return "Invalid"