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

    def printNfromEnd(self, position):
        n = self.head
        length = 0
        while n is not None:
            n = n.next
            length += 1
        # Print count
        if position > length:
            print('Location is greater than the length of LinkedList')
            return
        n = self.head
        for i in range(0, length - position):
            n = n.next
        print(f'Node from {position} position from end',n.data)

linkList = LinkedList()
for i in range(5, 0, -1):
    linkList.insert_element(i)
    linkList.printNfromEnd(4)