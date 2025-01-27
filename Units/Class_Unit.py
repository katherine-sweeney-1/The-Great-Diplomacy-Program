class Unit ():
    
    def __init__ (self, unit_id, unit_type):
        self.id = unit_id
        self.type = unit_type
        self.loc = []
        self.command = []

    def assign_loc (self, node_obj, loc_string, nodes_dict):
        if node_obj:
            self.loc = node_obj
        else:
            self.loc = nodes_dict[loc_string]
        return self.loc

    def assign_cmdr(self, cmdr_obj):
        self.cmdr = cmdr_obj
        return self.cmdr
    
    def assign_retreat_disband(self, bool):
        self.retreat = bool
        return self.retreat

    def print_statements (self):
        print(" ")
        print("Unit ID", self.id)
        print("Unit type", self.type)
        print("Unit command", self.command)