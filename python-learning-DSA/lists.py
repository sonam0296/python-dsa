list = [12.5, 10, 7, 88, 54]
for i in list:
    print('Item: ', i)

# Accessing index
n = len(list)
for i in range(n):
    print('Access list by index: ', list[i])

# Search element in list
ele = int(input('Enter the number to be searched: '))
#  Store a boolean value for found
found = False
for i in range(n):
    if list[i] == ele:
        found = True
        break

if found == True:
    print('Yeyy we found the element')
else:
    print('Element not present in the list!!')    
    
# Sum the elements of the list
#  1. Way 
total = 0
for i in list:
    total += i
print('Total : ', total)

#  2. Using built-in method
print("Built-in sum method : ", sum(list)) 

# =========== + operator on list ============

l1 = [1, 2, 3]
l2 = [4, 5,6]
l3 = l1 + l2
print('+ operator : ',l3)  # we can concat using +. I tried using extend and append but it adds the element to l1 
# l1.extend(l2)
# print('Extend : ', l1)

# =========== * operator on list ============
l4 = l1 * 5 # elements get repeated
print('* Operator : ', l4)