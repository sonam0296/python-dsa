def count_rotations_linear(nums):
    position = 0        # Initial value for position will be 0 
    while position < len(nums):
        # Check whether position is greater than 0 and also the current number is smaller than previous number than return position
        if position > 0 and nums[position] < nums[position - 1]:
            return position
        position += 1
    return 0              #If none of positions passed

test = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}

result = count_rotations_linear(test['input']['nums'])
print('Number of times list rotated: ' ,result)

if result == test['output']:
    test_passed ='Passed'
else:
    test_passed = 'Failed'

print('Test Case : ', test_passed)

tests = [
    {
    'input': {
        'nums': [8,9,10,1,2,3,4,5,6,7]
    },
    'output': 3
    },
    {
    'input': {
        'nums': [4,5,6,7,8,1,2,3]
    },
    'output': 5
    },
    {
    'input': {
        'nums': [1,2,3,4,5]
    },
    'output': 0
    },
    {
    'input': {
        'nums': [4,1,2,3]
    },
    'output': 1
    },
    {
    'input': {
        'nums': [2,3,4,5,1]
    },
    'output': 4
    },
    {
    'input': {
        'nums': [1,2,3,4,5]  # A list that was rotated n times 
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
    }
]

for test in tests:
    evaluate_test_caes = count_rotations_linear(test['input']['nums'])
    print('Test Cases: ', evaluate_test_caes)