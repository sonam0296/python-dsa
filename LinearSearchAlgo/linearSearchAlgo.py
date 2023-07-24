def locate_cards(cards, query):
    # Create a variable named position and initially its value will be 0
    position = 0

    # Set up loop for repition
    while position < len(cards):
        # Check whether the position index equals query
        if cards[position] == query:
            #  return the position
            return position
        
        # increament the position value by 1
        position += 1

    # ********************* Below code through error list index out of range. ****************** Instead we should check at the starting

        # check if we have reached the end of list
        
        # if position == len(cards):
            # number not found return -1
    return -1
        
test = {
    'input': {
        'cards': [13, 11, 10, 7, 5, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

result = locate_cards(test['input']['cards'], test['input']['query'])
# print(result)

# To test multiple test scenarios
tests = [
    {'cards': [13, 11, 10, 7, 5, 3, 1, 0], 'query': 7},
    {'cards': [13, 11, 10, 7, 5, 3, 1, 0], 'query': 13},
    {'cards': [13, 11, 10, 7, 5, 3, 1, 0], 'query': 0},
    {'cards': [13, 11], 'query': 0},
    {'cards': [13], 'query': 13},
    {'cards': [], 'query': 5},
    {'cards': [13, 13, 13, 11, 11, 10, 7, 5, 3, 1, 0], 'query': 10},
    {'cards': [13, 13, 13, 11, 11, 10, 7, 5, 3, 3, 3, 1, 0], 'query': 3},
]

for test in tests:
    evaluate_tests = locate_cards(test['cards'], test['query'])
    print('evaluate_tests :' , evaluate_tests)


# The above algorithm is Linear Search Algo and its time complexity is O(N) and space complexity is O(1)
