class Unit ():
    
    def __init__ (self, unit_id, unit_type):
        self.id = unit_id
        self.type = unit_type
        self.location = []
        self.command = []

    def assign_location (self, node_obj, loc_string, nodes_dict):
        if node_obj:
            self.location = node_obj
        else:
            self.location = nodes_dict[loc_string]
        return self.location

    def assign_commander(self, cmdr_obj):
        self.commander = cmdr_obj
        return self.commander
    
    def assign_retreat_disband(self, bool):
        self.retreat = bool
        return self.retreat

    def print_statements (self):
        print(" ")
        print("Unit ID", self.id)
        print("Unit type", self.type)
        print("Unit command", self.command)