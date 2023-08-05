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

    def traverse_list(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            n = self.head
            print(n.data, '--->', end=' ')

    def get_length(self):
        len = 0
        n = self.head
        while n is not None:
            len += 1
            n = n.next
        return len

    def get_middle(self):
        print()
        n = self.head
        if n is not None:
            length = self.get_length()
            mid = length // 2
            while mid != 0:
                n = n.next
                mid -= 1
            print('The middle element is :', n.data)

# if __name__ == 'main':
linkList = LinkedList()
for i in range(5, 0, -1):
    linkList.insert_element(i)
    linkList.get_middle()
    # linkList.traverse_list()