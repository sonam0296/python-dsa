def shell_sort(list):
    gap = len(list) // 2
    while gap > 0:
        # In insertion sort algorithm we have taken range from 1 to the length of list b'coz we were comparing adjacent element
        #  but here we need to take from the gap i.e compare the elements between the gap
        for i in range(gap, len(list)):
            current_element = list[i]
            position = i
            while current_element < list[position - gap] and position >= gap:
                list[position] = list[position - gap]
                position = position - gap
            list[position] = current_element
        gap = gap // 2

num = int(input('How many elements ?? '))
list = [int(input('Enter the numbers: ')) for i in range(num)]
shell_sort(list)
print(list)