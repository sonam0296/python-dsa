# BASIC STEPS OR ALGORITHM FOR MERGE SORT =========>>>>>>
    # 1. Divide the array in to two halves.
    # 2. Recursively sort each half
    # 3. Merge both the halves

# DEMO ---->> Given two sorted subarrays a[lo] to a[mid] and a[mid+1] to a[hi], replace with sorted subarray a[lo] to a[hi].

# array = ['E', 'E', 'G', 'M', 'R', 'A', 'C', 'E', 'R', 'T']

def merge_sort(list):
    # Base case i.e stopping condition
    # Dividing is done 
    if len(list) > 1:
        mid = len(list) // 2
        # :mid and mid: meaning 0 to mid and mid to end if we don't mention any number
        leftSublist = list[:mid]
        rightSublist = list[mid:]
        merge_sort(leftSublist)
        merge_sort(rightSublist)
    # Compare the elements and merge them
    # i is index of leftlist, j is index of rightlist and k is index of list
        i = 0 
        j= 0 
        k = 0
        # 
        while i < len(leftSublist) and j < len(rightSublist) :
            if leftSublist[i] < rightSublist[j]:
                list[k] = leftSublist[i]
                i += 1
                k += 1
            else:
                list[k] = rightSublist[j]
                j += 1
                k += 1
        # If any value is left out at the last
        while i < len(leftSublist):
            list[k] = leftSublist[i]
            i += 1
            k += 1
        while j < len(rightSublist):
            list[k] = rightSublist[j]
            j += 1
            k += 1


num = int(input("How many elements we need in the list"))
list = [int(input('Enter the numbers: ')) for i in range(num)]
merge_sort(list)
print(list)
