class Command ():

    def __init__ (self, country_string):
        self.country = country_string
        self.legal = 1
        self.strength = 1
        self.cmd_value = 1

    def assign_cmdr(self, cmding_owner, commanders):
        self.human = commanders[cmding_owner]
        return self.human
    
    def assign_unit(self, unit_string, units):
        if unit_string in units:
            self.unit = units[unit_string]
        else:
            self.legal = 0
            self.unit = 0
        return self.unit
    
    def assign_loc(self, loc_string, nodes):
        self.loc = nodes[loc_string]
        return self.loc
    
    def assign_origin (self, origin_string, nodes):
        self.origin = nodes[origin_string]
        return self.origin
    
    def assign_destination (self, dest_string, nodes):
        self.destination = nodes[dest_string]
        return self.destination
    
    def legal_command (self, filter_value):
        self.legal = filter_value
    
    def cmd_strength(self, additional_strength):
        self.strength = self.strength + additional_strength
        return self.strength
    
    def success(self, cmd_valid_boolean):
        self.succeed = cmd_valid_boolean
        return self.succeed
    
    def retreat_boolean(self, possible_retreat):
        self.retreat = possible_retreat
        return self.retreat
    
    def outcome_location(self, node):
        self.outcome_loc = node
        return self.outcome_loc
    
    def print_statement(self):
        print("command for unit {}, country {} has commander {}".format(self.unit.id, self.country, self.human.human))
        print("loc: {}, origin: {}, dest: {}".format(self.loc.name, self.origin.name, self.destination.name))

