def binary_search(list, key):
    low = 0
    high = len(list) - 1
    found = False
    while low <= high and not found:
        mid = (low + high) // 2
        if key == list[mid]:
            found = True
        elif list[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    if found == True:
        print('Key is found')
    else:
        print('Key not found')

list = [23, 1, 4, 2, 3]
list.sort()
key = int(input('Enter the key: '))
binary_search(list, key)
# print(list, key)