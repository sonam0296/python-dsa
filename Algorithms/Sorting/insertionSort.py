def insertion_sort(list):
    # We start from 1 index because 0th index will be the sorted part
    for i in range(1, len(list)):
        current_element = list[i]
        position = i 
        while current_element < list[position - 1] and position > 0:
            list[position] = list[position - 1]
            position -= 1
        # If current element is greater than do nothing
        list[position] = current_element

list = [10, 4, 5, 25, 1, 5]
insertion_sort(list)
print(list)
 