def minmax(data):
    return min(data), max(data) # Return the value in form of tuple

print(minmax([1,3,5,8,10]))

# Example 1 

def findSquare(num):
    return num * num

num = int(input('Enter number: '))
print(f"Square of number: {findSquare(num)}")

# Write a function to get maximum number from the given input
def findLargestNum(a, b, c):
    if a > b and a > c:
        big = a
    elif b > a and b > c:
        big = b
    else:
        big = c
    return big

x = int(input('Enter 1st num: '))
y = int(input('Enter 2nd num: '))
z = int(input('Enter 3rd num: '))

print(findLargestNum(x, y, z))

# Function to get largest and smallest value from the array

def findLargestSmallestNum(arr):
    #  To find maximum number we have multiple approach like ---
        # 1. Iterative Approach ===>>>> Time complexity - O(N) & Space - O(1)
        # 2. Python library ====>>>> Time complexity - O(N) & Space - O(1) -------- max() and min()
        # 3. Recursive Approach ===>>>> Time complexity - O(N) & Space - O(N)
        # 4. Sort the array and last ele and 1st ele will be max and min value
    max = arr[0]
    min = arr[0]
    n = len(arr)
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    return max, min

array = []
n = int(input("Enter the number of elements: "))
for i in range(n):  # Loop till number of elements
    element = int(input("Enter element: "))
    array.append(element)

print(array)

# array = input("Enter space-separated elements: ").split()
print(findLargestSmallestNum(array))



#  ------------------- We can take array as input using the below methods

#  1.) Loop and append the multiple values
        # array = []
        # n = int(input("Enter the number of elements: "))
        # for i in range(n):  # Loop till number of elements
        #     element = int(input("Enter element: "))
        #     array.append(element)

        # print(array)

# # 2.) Using split
        # list = input("Enter space-separated elements: ").split()  

#  Factorial Function

# Iterative way
def factorialFunc(num):
    fact = 1
    for i in range(1, num+1): # start from 1 till num + 1 b'coz we need the factorial till that number
        fact = fact * i
    return fact


# Recursive way
def recursiveFact(num):
    # base condition
    if num==0 or num==1:
        return 1
    else:
        return num * recursiveFact(num-1)

print(recursiveFact(int(input('Enter number: '))))


# ------------- RECURSION ===>>>>  Recursion is technique where function calls itself directly or indirectly --------------------
#  Two main  components -->>>
#       1. Base Case  -- Terminate the recursive
#       2. Recursive Case -- Func calls itself to solve the bigger problem in smaller way
# 