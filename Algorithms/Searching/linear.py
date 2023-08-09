def linear_search(list, key):
    for i in range(len(list)):
        if key == list[i]:
            print('Key found at position: ', i)
            break
    else:
        print('Key not found')

list = [10, 7, 4, 1, 19, 17, 2]
linear_search(list, 4)