def count_rotations_binary(nums):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        middle_number = nums[mid]
        if mid > 0 and middle_number < nums[mid - 1]:
            return mid
        elif middle_number < nums[low]:
            high = mid - 1
        else:
            low = mid + 1
    return 0


test = {
    'input': {
        'nums': [1, 3, 3]
    },
    'output': 0
}

result1 = count_rotations_binary(test['input']['nums'])
print('result: ', result1)


def search_target_binary(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        middle_number = nums[mid]
        print('mid: ', mid, 'low: ', low, 'high: ',
              high, 'mid_number: ', middle_number, 'target: ', target, 'nums[mid -1]: ', nums[mid - 1])
        if mid >= 0 and middle_number == target:
            return mid
        elif nums[mid - 1] == target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

# Need to check for below test case it is not working as expected
test = {
    'input': {
        'nums': [1,3],
        'target': 3
    },
    'output': 1
}

# test = [{
#     'input': {
#         'nums': [4, 5, 6, 7, 0, 1, 2],
#         'target': 3
#     },
#     'output': -1
# },
#     {'input': {
#         'nums': [3],
#         'target': 3
#     },
#     'output': 0},
# 
# ]
result12 = search_target_binary(test['input']['nums'], test['input']['target'])
print('result12: ', result12)

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
    },
    {
        'input': {
            'nums': [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]
        },
        'output': 6
    }
]

for test in tests:
    evaluate_test_caes = count_rotations_binary(test['input']['nums'])
    # evaluate_test_caes_minimum_elements = minimum_element(test['input']['nums'])
    print('Test Cases for count rotations : ', evaluate_test_caes)
    # print('Test Cases for minimum elements : ', evaluate_test_caes_minimum_elements)
