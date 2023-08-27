# #
#  We can solve this using linear approach but time complexity --->>> O(nlogN)
#  So the efficient way is to use hash map
# #
def twoSum(num, target):
    prevMap = {} # stores value in key: value ===>>> value: index
    #Loop through the list
    for i,n in enumerate(num):   # As we need to return index and the value we use enumerate in python
        diff = target - n
        # check if diff is there in hashmap
        if diff in prevMap:
            # retrurn the index 1st from hashmap and the index
            return [prevMap[diff], i]
        # update the hashmap
        prevMap[n] = i
    return

nums = [2,7,11,15]
target = 13
print(twoSum(nums, target))