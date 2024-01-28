# Array is a container which can hold a fix number of items & these items should be of same type.
# Element and index
# <<<<==== Types of Array ===>>> #
#   1. 1D Array #
#   1. 2D Array #
# <<<<===1D Array creattion===>>>>>
#    1) Import array from array module
#    2) use array with array(typeCode, [initializer])

from array import *

arrayList = array("i", [1, 2, 3, 4])
# Display items from array
for i in arrayList:
    print('Item : ', i )

# Accessing array elements 
print('Accessing array element : ', arrayList[2])

# Search operation
print("Index of num: ",arrayList.index(4))

# Insertion array
arrayList.append(20)
arrayList.extend([25, 12, 50])
print('After insertion : ', arrayList)

# Deletion operation
arrayList.remove(25)
print('After deletion : ', arrayList)

# Updating 
arrayList[2] = 100
print('After updating : ', arrayList)


# 2D Array

#  Accessing array
array2D = [[11, 12, 14], [1, 2, 3, 4], [7, 2, 4]]
print('2D array : ',array2D[0], array2D[1][2])

# Insertion in 2D array
# ********************IMP POINT +++>>>> using append & extend we can't insert elements to array in 2D ***************
array2D.insert(3, [8, 0, 15, 17])
print('After insertion : ', array2D)

# Deletion operation
del array2D[2]
print('After deletion : ', array2D)

# Update Opertion
array2D[0] = [1, 5, 9]
print('After updating : ', array2D)