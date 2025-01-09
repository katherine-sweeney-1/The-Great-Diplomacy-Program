
from Class_Node import Node

class Coastal_Node (Node):
    
    def __init__ (self, node_name, node_info):
        super().__init__(node_name, node_info)
    
    def get_main(self, main_name, main_info):
        self.main_obj = Node(main_name, main_info)
        return self.main_obj
    
    def get_sibling(self, sibling_name, sibling_info):
        self.sibling_obj = Node(sibling_name, sibling_info)
        return self.sibling_obj

    def related_node_print(self):
        print(" ")
        print("node {} has parent node {} and sibling node {}".format
              (self.name, self.main_obj.name, self.sibling_obj.name))