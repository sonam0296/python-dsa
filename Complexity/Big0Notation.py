# O(1) ==>> Doesn't matter how much the input size is or data increases the amount if time is same.

# def addItemsToArray(items):
#     array = [2, 3, 4]
#     array.append(items)
#     return array

# print(addItemsToArray([20, 6, 8, 9]))

# O(N) ===>> Linear search 

def linear_search(arr , value):
    position = 0
    while position < len(arr):
        if arr[position] == value:
            return True
        position += 1
    return False

print(linear_search([1,2,3,6,7], 7))

# O(N^2)  ==>> Bubble Sort

# O(logN) ==>> Binary Search