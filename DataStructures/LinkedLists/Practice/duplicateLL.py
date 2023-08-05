class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DuplicateLL:
    def __init__(self):
        self.head = None
    
    def create_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def print_LL(self):
        print()
        n = self.head
        if n is None:
            print('Linked list is null')
        else:
            while n is not None:
                print(n.data, '-->', end='')
                n = n.next

    def duplicate_elements(self):
        n = self.head
        temp = None
        index = None
        if n == None:
            print('Linked list is empty')
        else:
            while n is not None:
                temp = n
                index = n.next

                while index != None:
                    if index.data == n.data:
                        temp.next = index.next
                    else:
                        temp = index
                    index = index.next
                n = n.next

duplicateLL = DuplicateLL()
duplicateLL.create_node(1)
duplicateLL.create_node(2)
duplicateLL.create_node(1)
duplicateLL.create_node(3)
duplicateLL.create_node(3)
duplicateLL.create_node(4)
duplicateLL.create_node(2)
duplicateLL.print_LL()
duplicateLL.duplicate_elements()
duplicateLL.print_LL()