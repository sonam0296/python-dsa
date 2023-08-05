def createStack():
    stack = []
    return stack


def length_of_stack(stack):
    return len(stack)


def isEmpty(stack):
    if length_of_stack(stack) == 0:
        print('Stack is empty!!!')
        return True


def push(stack, ele):
    stack.append(ele)


def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()


def reverse(string):
    n = len(string)

    # create a stack
    stack = createStack()
    # Loop through the string and push the elements
    for i in range(0, n, 1):
        push(stack, string[i])

# Making the string empty since all
    # characters are saved in stack
    string = ""

    for i in range(0, n, 1):

        string += pop(stack)

    return string


def reverse_num(n):
    stack = createStack()
    while n > 0:
        stack.append(n%10)
        n = int(n/10)
    # we will store the reverse number into this variable
    ans = 0
    # intializing to multiply with the power of 10
    i = 1
    while len(stack) > 0:
        val = stack.pop()
        ans = ans + val*i
        i = i *10
    print(ans)

string = 123456
string = reverse_num(string)
print("Reversed string is " + string)
