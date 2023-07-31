class Node:
    def __init__(self, data):
        self.data = data
        self.prev_ref = None
        self.next_ref = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def traversal_LL_forward(self):
        if self.head == None:
            print('Linked list is empty!!')
        else:
            # Forward traversing
            n = self.head
            while n is not None:
                print(n.data, '---->>', end=" ")
                n = n.next_ref
    
    def traversal_LL_backward(self):
        print()
        if self.head == None:
            print('Linked list is empty!!')
        else:
            # backward traversing
            n = self.head
            while n.next_ref is not None:
                n = n.next_ref
            while n is not None:
                print(n.data, '---->>', end=" ")
                n = n.prev_ref

    # Insert when linked list is empty
    def insert_in_emptyLL(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('Linked list is not empty')
    
    def insert_begin(self, data):
        new_node = Node(data)
        # Check if LL is empty or not if it's empty than we need to point the head to new node i.e need to add at the begining
        if self.head is None:
            self.head = new_node
        # else we need to pint the head to new node also change the ref of next and previous node
        else:
            new_node.next_ref = self.head
            self.head.prev_ref = new_node
            self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        # Check if LL is empty or not if it's empty than we need to point the head to new node i.e need to add at the begining
        if self.head is None:
            self.head = new_node
        # else we need to pint the head to new node also change the ref of next and previous node
        else:
            n = self.head
            while n.next_ref is not None:
                n = n.next_ref
            n.next_ref = new_node
            new_node.prev_ref = n

    def insert_after_node(self, data, node):
        new_node = Node(data)
        if self.head == None:
            print('Linked list is empty')
        else:
            n = self.head
            while n.next_ref is not None:
                if node == n.data:
                    break
                n = n.next_ref
            if n is None:
                print("Node not found")
            else:
                # Need to check whether we are inserting after the last node or in the middle
                new_node.next_ref = n.next_ref
                new_node.prev_ref = n
                # We need to update the position of n.next_node, n.next_node.prev_node i.e node of next node of previous value
                if n.next_ref is not None:
                    n.next_ref.prev_ref = new_node
                n.next_ref = new_node
    
    def insert_before_node(self, data, node):
        new_node = Node(data)
        if self.head == None:
            print('Linked list is empty')
        else:
            n = self.head
            while n.next_ref is not None:
                if node == n.next_ref.data:
                    break
                n = n.next_ref
            if n.next_ref is None:
                print("Node not found")
            else:
                # Need to check whether we are inserting before the fisrt node or in the middle 
                new_node.prev_ref = n.prev_ref
                new_node.next_ref = n
                if n.prev_ref is not None:
                    n.prev_ref.next_ref = new_node
                else:
                    self.head = new_node
                n.prev_ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            self.head = n.next_ref
            n.next_ref.prev_ref = None
    
    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
        if self.head.next_ref is None:
            print('Double linked list is empty after deleting all the nodes')
        else:
            n = self.head
            while n.next_ref is not None:
                n = n.next_ref
            n.next_ref = None

    def delete_value(self, node):
        if self.head is None:
            print("Linked list is empty")
            return
        # Check if 1st node is last node
        if self.head.next_ref is None:
            if self.head.next_ref.data == node:
                self.head = None
            else:
                print('Node is not present')
            return
        # Only node
        if self.head.data == node:
            self.head = self.head.next_ref
            self.head.prev_ref = None
            return
        # Middle node
        n = self.head
        while n.next_ref is not None:
            if node == n.data:
                break
            n = n.next_ref
        if n.next_ref is not None:
            n.next_ref.prev_ref = n.prev_ref
            n.prev_ref.next_ref = n.next_ref
        # To delete the last node
        else:
            if n.data == node:
                n.prev_ref.next_ref = None
            else:
                print('Node not found')

doubleLL = DoubleLinkedList()
# doubleLL.insert_in_emptyLL(10)
doubleLL.insert_begin(20)
doubleLL.insert_begin(100)
doubleLL.insert_end(250)
doubleLL.insert_end(350)
doubleLL.insert_after_node(200, 250)
# doubleLL.insert_before_node(100, 20000)
# doubleLL.delete_begin()
# doubleLL.delete_end()
doubleLL.delete_value(20)
doubleLL.traversal_LL_forward()
doubleLL.traversal_LL_backward()