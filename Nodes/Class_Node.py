class Node ():
    
    def __init__ (self, node_name, node_info):
        self.name = node_name
        self.full_name = node_info["Full Name"]
        self.node_type = node_info["Type"]
        self.is_occ = False

    def parse_nbrs (self):
        self.nbrs = self.nbrs.split(" ")
        return(self.nbrs)

    def assign_occ(self, unit):
        self.is_occ = unit
        return self.is_occ
    
    def assign_nbrs(self, nodes, nbrs_string):
        nbrs_dict = {}
        for each_nbr in nbrs_string:
            nbr = nodes[each_nbr]
            nbrs_dict[each_nbr] = nbr
        self.nbrs = nbrs_dict
        return self.nbrs
    
    def assign_dot(self, dot_str):
        if dot_str == "TRUE":
            self.dot = True
        else:
            self.dot = False
        return self.dot

    def assign_hsc(self, hsc_str):
        if hsc_str != "FALSE":
            self.hsc = hsc_str
        else:
            self.hsc = False
        return self.hsc

    def print_statements (self):
        print("Territory {} / {}".format(self.name, self.full_name))
        print("dot status: {}, hsc status {},occupied status {}".format(self.dot, self.hsc, self.is_occ))
        print("neighbors: {}".format(self.nbrs))
        print("   ")




    
    