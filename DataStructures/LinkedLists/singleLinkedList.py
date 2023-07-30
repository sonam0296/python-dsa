# Class Node will create the many nodes and each node contain 2 components ie. data and next 

class Node:
    # __init__() function is created whenever we create a new instance of the class
    def __init__(self, data):
        self.data = data
        self.next = None

# Now as we have created nodes we need to link them so we have created LinkedList class and it will have head 
class LinkedList:
    def __init__(self):
        self.head = None

    # Traversing the linked list
    def traverse_LL(self):
        if self.head == None:
            print('Linked list is empty!!!!')
        else:
            # As we need self.head many times so we are assign the self.head to a n variable
            n = self.head
            while n is not None:
                print(n.data, '------>>', end=" ")
                n = n.next
    
    # Inserting the element at beginning of LL
    def insert_beginning(self, data):
        # 1st step while insert the data or element is to create a Node
        new_node = Node(data)
        # Initially the new_node.next is None but we need to change that to head i.e whatever value is there in self.head we need to assign it to next
        new_node.next = self.head
        # Now the head node should point to new_node as it will be the first node in linked list. As the reference of first node of LL should be stored in HEAD
        self.head = new_node

# Inserting the element at end of LL
    def insert_end(self, data):
        # 1st step while insert the data or element is to create a Node
        new_node = Node(data)
        if self.head == None:
            # store the reference of newly create node i.e new_node to self.head
            self.head = new_node
        else:
            n = self.head
            # Using while loop to go to the last node
            while n.next is not None:
                n = n.next
            # When we found n.ref to be none we point the next pointer to new node
            n.next = new_node
        
    def insert_after_node(self, data, after_node):
        # First we will find the position of the after_node so fisrt we will store the value of head or first node in n variable and traverse until we found the position
        n = self.head
        while n is not None:
            if n.data == after_node:
                break
            n = n.next
        if n is None:
            print("Node is not present in LL")
        else:
            new_node = Node(data)
            # Change the reference point of next node to new_node 
            new_node.next = n.next
            # change the reference of previous node to new_node
            n.next = new_node

    def insert_before_node(self, data, befor_node):
        # Two scenerios we need to check
        #   1. Before the 1st node
        #   2. In middle of any node
        new_node = Node(data)
        # Herev we need have checked if the the before_node is the 1st element in the LL then head will point to the new_node
        if self.head == None:
            print("Linked list is empty")
            return
        if self.head.data == befor_node:
            new_node.next = self.head
            self.head = new_node
            return
        # Here we will find the previous node of the before_node position and check if it is true than will add the new node else traverse
        n = self.head
        while n.next is not None:
            if n.next.data == befor_node:
                break
            n = n.next
        
        if n is None:
            print("Node is not present in LL")
        else:
            new_node.next = n.next
            n.next = new_node
        
    # Delete the node
    def delete_beginning(self):
        if self.head == None:
            print('Linked List is empty')
        else:
            n = self.head
            self.head = n.next

    def delete_end(self):
        if self.head == None:
            print('Linked List is empty')
        elif self.head.next is None:
            self.head = None
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None

    def delete_middle(self, node):
        if self.head == None:
            print("Linked list is empty")
            return
        # Check whether the node is 1st node or not if it is true head should point to 2nd node
        n = self.head
        if n.data == node:
            self.head = n.next
            return
        # Loop until it is None and check the n.data = node if it is then break the loop else travserse
        while n.next is not None:
            if n.next.data == node:
                break
            n = n.next
        if n is None:
            print("Node is not found")
        else:
            n.next = n.next.next

linkedList = LinkedList()
linkedList.insert_beginning(10)
linkedList.insert_beginning(20)
linkedList.insert_beginning(30)
# linkedList.insert_end(40)
# linkedList.insert_after_node(100, 10)
# linkedList.insert_before_node(200, 10)
# linkedList.insert_end(30)
# linkedList.delete_beginning()
# linkedList.delete_end()
linkedList.delete_middle(20)
linkedList.traverse_LL()