class Node ():
    
    def __init__ (self, node_name, node_info):
        self.name = node_name
        self.full_name = node_info["Full Name"]
        self.node_type = node_info["Type"]
        self.nbrs = node_info["Neighbors"]
        self.country = node_info["Country"]
        self.dot = node_info["Dot"]
        self.hsc = node_info["Home SupCenter"]

    def parse_nbrs (self):
        self.nbrs = self.nbrs.split(" ")
        return(self.nbrs)
    
    def is_node_occupied(self, unit_obj_dict):
        return

    def print_statements (self):
        print("Territory {} / {} is owned by {} with neighbors {}"
              .format(self.name, self.full_name, self.country, self.nbrs))
        print("Territory {} has dot status {} and hsc status {}"
              .format(self.name, self.dot, self.hsc))
        print("   ")




    
    