class Command ():

    def __init__ (self, cmd_dict):
        self.unit = cmd_dict
        self.loc = cmd_dict["location"]
        self.origin = cmd_dict["origin"]
        self.dest = cmd_dict["destination"]
    
    def print_statements(self):
        print(" ")
        print("Unit {} at location {} applies effort from origin {} to destination {}".
              format(self.unit, self.loc, self.origin, self.dest))