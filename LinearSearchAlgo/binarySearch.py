# Optimise solution for the problem

def test_location(cards, query, mid):
    # find the mid number from the cards
    mid_number = cards[mid]

#  check if mid num equals query
    if mid_number == query:
        # Check mid num is greater as it can give error and also check if card of mid number -1 eqauls query than it show go on in left
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    # set the variables low and high
    low, high = 0, len(cards) - 1
    # Check whether low <= high
    print('cards: ', cards, 'query: ', query)
    while low <= high:
        # we did // as it will return the quotient i.e integer
        middle = (low + high) // 2
        result = test_location(cards, query, middle)

        # print('low: ', low, 'high: ', high, 'middle: ',
        #       middle, 'middle_num', result)
        if result == 'found':
            return middle
        elif result == 'left':
            high = middle - 1
        elif result == 'right':
            low = middle + 1
    return -1

# single test case
test = {
    'input': {
        'cards': [13, 11, 10, 7, 5, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

result = locate_card(test['input']['cards'], test['input']['query'])
print(result)

# To test multiple test scenarios

tests = [
    {
        'input': {
            'cards': [13, 11, 10, 7, 5, 3, 1, 0],
            'query': 7
        },
        'output': 3
    }, {
        'input': {
            'cards': [13, 11, 10, 7, 5, 3, 1, 0],
            'query':13
        },
        'output': 0
    },
    {
        'input': {
            'cards': [13, 11, 10, 7, 5, 3, 1, 0],
            'query': 0
        },
        'output': 7
    }, {
        'input': {
            'cards': [13, 11],
            'query': 0
        },
        'output': -1
    },
    {
        'input': {
            'cards': [13],
            'query': 13
        },
        'output': 0
    }, {
        'input': {
            'cards': [],
            'query':1
        },
        'output': -1
    },
    {
        'input': {
            'cards': [13, 13, 13, 11, 11, 10, 7, 5, 3, 1, 0],
            'query': 10
        },
        'output': 5
    }, {
        'input': {
            'cards': [13, 13, 13, 11, 11, 10, 7, 5, 3, 3, 3, 1, 0], 'query': 3},
        'output': 8
    }

]

for test in tests:
    print('test: ', test)
    evaluate_tests = locate_card(
        test['input']['cards'], test['input']['query'])
    print('evaluate_tests :', evaluate_tests)

#  Here we are getting different output for the last test case so we need to find the different solution

# 'input': {
#             'cards': [13, 13, 13, 11, 11, 10, 7, 5, 3, 3, 3, 1, 0], 'query': 3},
#         'output': 8

# As we are using binary search so it is considering whichever query comes first 
#  We have defined a test_location function to check the position of query with the query occurs more than once


