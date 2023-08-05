queue = []

def enqueue_element(limit):
    if len(queue) == limit:
        print('Queue is full!!!')
    else:   
        element = int(input('Enter the element: '))
        queue.append(element)
        print(queue)

def dequeue_element():
    if len(queue) == 0:
        print('Queue is empty!!!!')
    else:
        # pop(0) ===>> remove element from last
        ele = queue.pop(0)
        print("Popped element: ", ele)
        print(queue)

def display():
    print(queue)

limit = int(input('Enter the size of stack: '))
while True:
    print('Choose the option : - 1. Push 2. Pop 3.Display 4.Quit')
    choice = int(input('Enter the choice :'))
    if choice == 1:
        enqueue_element(limit)
    elif choice == 2:
        dequeue_element()
    elif choice == 3:
        display()
    elif choice == 4: 
        break
    else:
        print('Enter the correct option....')