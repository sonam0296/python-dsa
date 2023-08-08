
# Selection Sort Algo: ----------
#   1. Using built-in method i.e. min() 
#   2. Manual algorithm ===>>>
#       a.) Start from 1st element and search for smallest/largest value in the list
#       b.) Swap minimum/ maximum value with 1st element
#       c.) Recursively repeat the above steps with the unsorted list till we get the sorted list 
#  

# 1. Using built-in method i.e. min() ==============================>>>>>>>>>

# Non duplicate numbers
list = [56, 3, 2, 7, 16, 4, 45, 0]

print('Original List: --', list)
for i in range(len(list)-1):
    # i: it will consider the list according to i value
    min_val = min(list[i:])
    min_indes = list.index(min_val)
    if list[i] != list[min_indes]:
        list[i], list[min_indes] = list[min_indes], list[i]
print('Sorted List: --', list)

# Duplicate values
list1 = [56, 3, 0, 2, 7, 16, 4, 2, 45, 0]
print('Original List: --', list1)
for i in range(len(list1)-1):
    # i: it will consider the list1 according to i value
    min_val = min(list1[i:])
    min_indes = list1.index(min_val, i)
    # Check condition if we are swaping same numbers
    if list1[i] != list1[min_indes]:
        list1[i], list1[min_indes] = list1[min_indes], list1[i]
print('Sorted List1: --', list1)


#  2. Manual algorithm ===>>>
num = int(input('How many numbers you want to enter??? '))
user_list = [int(input("Enter number: ")) for x in range(num)]
print('Unsorted list: ', user_list)
for i in range(len(user_list)-1):
    # min_value = user_list[i]
    # Consider user_list[i] is the minimum value and we will find the index and then the valye
    min_index = i
    # loop the list from i+1 to length of user_list
    for j in range(i+1, len(user_list)):
        # Eg: user_list[j] is 3 and min_val = 56 so we will check
        if user_list[j] < user_list[min_index]:
            min_index = j
    # min_indes = user_list.index(min_val, i)
    # Check condition if we are swaping same numbers
    if user_list[i] != user_list[min_index]:
        user_list[i], user_list[min_index] = user_list[min_index], user_list[i]
     
print('Without using built-in method: --', user_list)