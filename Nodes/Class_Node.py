class Node ():
    
    def __init__ (self, node_name, node_info):
        self.name = node_name
        self.full_name = node_info["Full Name"]
        self.node_type = node_info["Type"]
        self.is_occupied = False

    def parse_neighbors(self):
        self.neighbors = self.neighbors.split(" ")
        return(self.neighbors)

    def assign_occupied(self, unit):
        self.is_occupied = unit
        return self.is_occupied
    
    def assign_neighbors(self, nodes, neighbors_string):
        neighbors_dictionary = {}
        for each_nbr in neighbors_string:
            nbr = nodes[each_nbr]
            neighbors_dictionary[each_nbr] = nbr
        self.neighbors = neighbors_dictionary
        return self.neighbors
    
    def assign_dot(self, dot_str):
        if dot_str == "TRUE":
            self.dot = True
        else:
            self.dot = False
        return self.dot

    def assign_supply_center(self, hsc_str):
        if hsc_str != "FALSE":
            self.supply_center = hsc_str
        else:
            self.supply_center = False
        return self.supply_center
    
    def assign_outcome_occupied(self, unit):
        self.outcome_occupied = unit
        return self.outcome_occupied

    def print_statements (self):
        print("Territory {} / {}".format(self.name, self.full_name))
        print("dot status: {}, hsc status {},occupied status {}".format(self.dot, self.hsc, self.is_occ))
        print("neighbors: {}".format(self.nbrs))
        print("   ")




    
    