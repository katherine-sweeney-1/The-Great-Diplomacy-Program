from Class_Node import Node

class Coastal_Node (Node):
    
    def __init__ (self, node_name, node_info):
        super().__init__(node_name, node_info)
    
    def assign_parent(self, main_obj):
        self.parent = main_obj
        return self.parent
    
    def assign_sibling(self, special_dict):
        #self.sibling_obj = Node(sibling_name, sibling_info)
        for each_ter in special_dict:
            if self.name[:3] in each_ter and self.name != each_ter:
                sibling_name = each_ter
                break
            else:
                continue
        sibling_node = special_dict[sibling_name]
        print(sibling_node, "siblings")
        self.sibling = sibling_node
        return self.sibling
    
    def assign_occ_to_family(self, unit):
        if self.assign_occ != 0:
            print("hi")
            

    def print_statements(self):
        print(" ")
        print("node {} has parent node {} and sibling node {}".format
              (self.name, self.parent.name, self.sibling.name))