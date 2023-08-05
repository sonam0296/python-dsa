# Solution Approaches

#     1. Using 2 queues => O(n) pop operation and O(1) push operation
#     1. Using 2 queues => O(1) pop operation and O(n) push operation
#     1. Using 1 queues => O(n) pop operation and O(1) push operation   --->> Pop operation is not possible
import sys
from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.Q1 = deque()
        self.Q2 = deque()
        self.stack_size = 0
    
    def push(self, element):
        self.Q1.append(element)
        self.stack_size = self.stack_size + 1

    def pop(self):
        if not self.Q1:
            print('Stack underflow!!!')
            return -sys.maxsize
        while len(self.Q1) != 1:
            temp = self.Q1.popleft()
            self.Q2.append(temp)

        stack_top = self.Q1.popleft()
        self.stack_size = self.stack_size - 1
        self.Q1, self.Q2 = self.Q2, self.Q1
        return stack_top
    
    def display(self):
        print(self.Q1)
        
stack = StackUsingQueue()
stack.push(10)
stack.push(20)
stack.push(40)
stack.push(30)
stack.display()
stack.pop()
stack.display()