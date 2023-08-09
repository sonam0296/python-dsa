# To get the original position of pivot element
#
    # It takes 3 parameters list, first index and last index
#
# Here we will take 1st element as the pivot element

# There are 3 conditions we need to check for ascending order. Same for descending just change the sign in 2nd & 3rd step
#   1. left <= right  #
#   2. list[left] <= pivot  #
#   3. list[right] >= pivot  #

#
def pivot_position(list, first, last):
    pivot = list[first]   # If pivot is last element then ====>>>> pivot = list[last]
    left = first + 1 # If pivot is last element then ====>>>> left = first
    right = last # If pivot is last element then ====>>>> right = last = 1
    while True: 
        while left <= right and list[left] <= pivot:
            left += 1
        while left <= right and list[right] >= pivot:
            right -= 1
        # When right gets smaller than left we need to stop execution and swap the values
        if right<left:
            break
        else:
            list[left], list[right] = list[right], list[left]
    # We want to swap the values or elements in the list that's why we are using list[first] not pivot
    list[first], list[right] = list[right], list[first]   # If pivot is last element then ====>>>>   list[last], list[left] = list[left], list[last]
    # we will swap the first value i.e pivot value with right index which will give us the position of pivot
    return right  # If pivot is last element then ====>>>>   return left

# Divide the list and recursively sort the sub-list

def quick_sort(list, first, last):
    # Stopping condition if first and last index is same 
    if first < last:
        p = pivot_position(list, first, last)
        # Recusrively call the function
        quick_sort(list, first, p-1) # p-1 i.e pivot index - 1 will give us the last index for left sub-list
        quick_sort(list, p+1, last) # p+1 i.e pivot index + 1 will give us the first index for right sub-list

# main

input = [56, 26, 3, 17, 31, 44]
quick_sort(input, 0, len(input)-1)
print(input)


# ===============>>>>>>>>>> RANDOM PIVOT ELEMENT <<<<<<<<<<<=====================

import random
def pivot_place_random(list, first, last):
    # Generate random index 
    rindex = random.randint(first, last)
    # Swap that rindex to the last or first index to make it easier
    list[rindex], list[last] = last[last], list[rindex]

##
# 
#  Rest is same 
# 
# 
# #

# ===============>>>>>>>>>> PIVOT AS MEDIAN OF THREE VALUES (first, middle, last) <<<<<<<<<<<=====================
import statistics

def pivot_median(list, first, last):
    low = list[first]
    high = list[last]
    mid = (first + last) // 2
    # Find the median
    pivot_val = statistics.median([low, list[mid], high])
    # Get the index of pivot_val
    if pivot_val == low:
        pindex = first
    elif pivot_val == high:
        pindex = last
    else:
        pindex = mid

    # Copy / Swap to last or first index
    list[pindex], list[last] = last[last], list[pindex]
    ##
# 
#  Rest is same 
# 
# 
# #