class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_element(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_data(self):
        n = self.head
        if n is None:
            print('Linked list is empty')
        while n:
            print(n.data, '--->>', end=" ")
            n = n.next

    def reverse_linked_list(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        

    def length_ll(self):
        len = 0
        n = self.head
        while n is not None:
            len += 1
            n = n.next
        print(len, ':::length')
        return len

linkedList = LinkedList()
# linkedList.insert_element(20)
# linkedList.insert_element(40)
# linkedList.insert_element(60)
# linkedList.insert_element(100)
linkedList.reverse_linked_list()
linkedList.length_ll()
linkedList.print_data()
