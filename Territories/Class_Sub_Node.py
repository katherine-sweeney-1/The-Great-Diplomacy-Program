
from Class_Node import Node

class Coastal_Node (Node):
    
    def __init__ (self, node_name, node_info):
        super().__init__(node_name, node_info)
    
    def get_main(self, main_name, main_info):
        self.main_obj = Node(main_name, main_info)
        #self.main_obj.print_statements()
        return self.main_obj
    
    def get_sibling(self, sibling_name, sibling_info):
        self.sibling_obj = Node(sibling_name, sibling_info)
        #self.sibling_obj.print_statements()
        return self.sibling_obj


    def related_node_print(self):
        print(" ")
        print("created node ", self.name)
        print("the main node is ", self.main_obj.name)
        print("the sibling node is ", self.sibling_obj.name)
    """
    want grouping of "main node" and each coast nodes
    """