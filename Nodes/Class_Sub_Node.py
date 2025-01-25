from Class_Node import Node

class Coastal_Node (Node):
    
    def __init__ (self, node_name, node_info):
        super().__init__(node_name, node_info)
    
    def assign_parent(self, main_obj):
        self.parent = main_obj
        return self.parent
    
    def assign_sibling(self, special_dict):
        for each_ter in special_dict:
            if self.name[:3] in each_ter and self.name != each_ter:
                sibling_name = each_ter
                break
            else:
                continue
        sibling_node = special_dict[sibling_name]
        self.sibling = sibling_node
        return self.sibling
    
    def assign_occ_to_family(self, parent_occ):
        if parent_occ:
            self.is_occ = 1
            self.sibling.is_occ = 1
            """
            elif if_child_occ:
                self.is_occ = 1
                self.parent.is_occ = 1
            """
        else:
            self.parent.is_occ = 1
            self.sibling.is_occ = 1
        return self
            
    def print_statements(self):
        print("node {} has parent node {} and sibling node {}".format(self.name, self.parent.name, self.sibling.name))
        print("occupied {}, {}, {}".format(self.is_occ, self.parent.is_occ, self.sibling.is_occ))
        print("Territory {} / {}".format(self.name, self.full_name))
        print("dot status: {}, hsc status {},occupied status {}".format(self.dot, self.hsc, self.is_occ))
        print("neighbors: {}".format(self.nbrs))
        print(" ")