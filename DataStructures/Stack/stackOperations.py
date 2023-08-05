stack = []
def push_element(limit):
    if len(stack) == limit:
        print('List is full')
    else:
        element = input('Enter the element: ')
        stack.append(element)
        print(stack)

def pop_element():
    if len(stack) == 0:
        print('Stack is empty!!!')
    else:
        element = stack.pop()
        print('Removed element: ', element)
        print(stack)

limit = int(input('Enter the size of stack: '))
while True:
    print('Choose the option : - 1. Push 2. Pop 3.Quit')
    choice = int(input('Enter the choice :'))
    if choice == 1:
        push_element(limit)
    elif choice == 2:
        pop_element()
    elif choice == 3: 
        break
    else:
        print('Enter the correct option....')