class BinarySearchTree:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None
    
    # Insertion Operation
    def insert_node(self, data):
        if self.key == None:
            self.key = data 
            return
        # Duplicate
        if self.key == data:
            return
        if self.key > data:
            if self.left_child:
                self.left_child.insert_node(data)
            else:
                self.left_child = BinarySearchTree(data)
        else:
            if self.right_child:
                self.right_child.insert_node(data)
            else:
                self.right_child = BinarySearchTree(data)

    def search(self, data):
        if self.key == data:
            print('Yayy!!! Found the data')
            return
        if self.key > data:
            if self.left_child:
                self.left_child.search(data)
            else:
                print('Node is not present')
        else:
            if self.right_child:
                self.right_child.search(data)
            else:
                print('Node is not present')

# Traversal Tree
    # Pre order
    # In order
    # Post order

    # Pre-order ===>>> First root, then left and than right
    def pre_order_traversal(self):
        if self.key == None:
            print('Tree is empty!!!')
            return
        print( self.key, '----', end=' ') 
        if self.left_child:
            self.left_child.pre_order_traversal()
        if self.right_child:
            self.right_child.pre_order_traversal()

    # In-order ===>>> First left, then print root and than right
    def in_order_traversal(self):
        if self.left_child:
            self.left_child.in_order_traversal()
        print(self.key, '---', end=' ')
        if self.right_child:
            self.right_child.in_order_traversal()
        
    # Pre-order ===>>> First left, then right and than print root
    def post_order_traversal(self):
        if self.left_child:
            self.left_child.post_order_traversal()
        if self.right_child:
            self.right_child.post_order_traversal()
        print( self.key, '----', end=' ') 

    #  Deletion operation :
        # Tree is empty or not -- If it is empty print message
            # --- If it is not empty 1. Find the node if node is present delete that 
            #                        2. If node is not present print message
    
    def deletion(self, data):
        if self.key is None:
            print('Tree is empty!!!')
            return
        if self.key > data:
            if self.left_child is not None:
                self.left_child = self.left_child.deletion(data)
            else:
                print('Given node is not present')
        elif self.key < data:
            if self.right_child != None:
                self.right_child = self.right_child.deletion(data)
            else:
                print('Given node is not present')
        # else:
        #     # If node not present in right and left ST. So it is root node


root = BinarySearchTree(10)
for i in range(1, 30, 5):
    root.insert_node(i)
# print(root.search(63)) 
print("Pre-Order Traversal")
root.pre_order_traversal()
print()
print("In-Order Traversal")
root.in_order_traversal()
print()
print("Post-Order Traversal")
root.post_order_traversal()