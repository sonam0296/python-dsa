class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SortLinkedList:
    def __init__(self):
        self.head = None
    
    def create_linkedList(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_LL(self):
        print()
        n = self.head
        if n is None:
            print("Linked list is empty!!!")
        else:
            while n is not None:
                print(n.data, '-->', end=' ')
                n = n.next

    def reverse_LL(self):
        n = self.head
        index = None
        if n.next == None:
            print('Linked list is empty')
        else:
            # Check whether head is not None and point the index to n.next
            while n != None:
                index = n.next
                # Check index is not None and n.data is greater than index.data than swap the values
                while index != None:
                    if n.data > index.data:
                        temp = n.data
                        n.data = index.data
                        index.data = temp
                    index = index.next
                n = n.next


sortLL = SortLinkedList()
sortLL.create_linkedList(1)
sortLL.create_linkedList(3)
sortLL.create_linkedList(6)
sortLL.create_linkedList(4)
sortLL.print_LL()  
sortLL.reverse_LL()
sortLL.print_LL()          
