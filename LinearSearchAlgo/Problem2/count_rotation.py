def count_rotations_binary(nums):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_number = nums[mid]
        if mid > 0 and mid_number < nums[mid - 1]:
            return mid
        elif mid_number < nums[low]:
            high = mid - 1
        else:
            low = mid + 1
    return 0


test = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}

result = count_rotations_binary(test['input']['nums'])


#  ================= Find Minimum in Rotated Sorted Array  ============================>>>>>>>>

def minimum_element(nums):
    print('nums: ', nums)
    low = 0
    high = len(nums) - 1
    while low <= high:
        print('high: ', high, 'low: ', low)
        # This condition is needed to handle the case when array is not rotated at all
        if low > high:
            return nums[0]
        # If there is only one element left
        if high == low:
            return nums[low]
        mid = (low + high) // 2
        mid_number = nums[mid]
        # print('mid: ', mid, 'low: ', low, 'high: ',
        #       high, 'mid_number: ', mid_number, 'nums[mid + 1]: ', nums[mid + 1], 'nums[mid]: ', nums[mid])
        # Check if element (mid+1) is minimum element. Consider the cases like [3, 4, 5, 1, 2]
        
        if mid > 0 and nums[mid + 1] < mid_number:
            print('nums[mid+1]')
            return nums[mid + 1]
        elif nums[mid] < nums[mid-1]:
            print('nums[mid]')
            return nums[mid]
        if nums[mid] < nums[high]:
            high = mid
        elif nums[mid] < nums[len(nums)-1]:
            print('mid-1')
            high = mid - 1
        else:
            print('mid+1')
            low = mid + 1
    return 0


test1 = {
    'input': {
        'nums': [1,3,3]
    },
    'output': 1
}

# result1 = minimum_element(test1['input']['nums'])
# print('result: ', result1)

tests = [
    {
        'input': {
            'nums': [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
        },
        'output': 3
    },
    {
        'input': {
            'nums': [4, 5, 6, 7, 8, 1, 2, 3]
        },
        'output': 5
    },
    {
        'input': {
            'nums': [1, 2, 3, 4, 5]
        },
        'output': 0
    },
    {
        'input': {
            'nums': [4, 1, 2, 3]
        },
        'output': 1
    },
    {
        'input': {
            'nums': [2, 3, 4, 5, 1]
        },
        'output': 4
    },
    {
        'input': {
            'nums': [1, 2, 3, 4, 5]  # A list that was rotated n times
        },
        'output': 0
    },
    {
        'input': {
            'nums': []
        },
        'output': 0
    },
    {
        'input': {
            'nums': [1]
        },
        'output': 0
    },
    {
        'input': {
            'nums': [3, 4, 5, 1, 2]
        },
        'output': 1
    },
    {
        'input': {
            'nums': [1]
        },
        'output': 1
    },
    {
        'input': {
            'nums': [2, 1]
        },
        'output': 1
    },
    {
        'input': {
            'nums': [1, 3, 3]
        },
        'output': 1
    }
]

for test in tests:
    evaluate_test_caes = count_rotations_binary(test['input']['nums'])
    # evaluate_test_caes_minimum_elements = minimum_element(test['input']['nums'])
    print('Test Cases for count rotations : ', evaluate_test_caes)
    # print('Test Cases for minimum elements : ', evaluate_test_caes_minimum_elements)
    