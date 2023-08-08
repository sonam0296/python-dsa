# <<<<<<<<<<<<===================== BUBBLE SORT =====================>>>>>>>>>>>>>


list = []
num = int(input('How many number of elements you want??'))
for i in range(num):
    list.append(int(input('Enter the elements: ')))

# This is in ascending order 
print('Unsorted List: ', list)
for i in range(len(list)-1):
    for j in range(len(list)-1-i):
        # If changing the sign we get the descending order
        if list[j] > list[j+1]:  
            list[j], list[j+1] = list[j+1], list[j]

print('Sorted List in ascending order: ', list)