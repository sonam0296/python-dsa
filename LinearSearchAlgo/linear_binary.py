
# Linear search
def locate_cards_linear(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

large_test = {
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998
}

print('Linear search with large data: ',locate_cards_linear(large_test['input']['cards'], large_test['input']['query']))

# Binary search

def binary_search(low, high, condition):
    while low <= high:
        mid = (low + high) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            high = mid - 1
        else:
            low = mid + 1
    return -1

def locate_cards_binary(cards, query):
    # function inside function is called closures
    def condition(mid):
        if cards[mid] == query:
            if mid -1 > 0 and cards[mid - 1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else: 
            return 'right'
    return binary_search(0, len(cards) - 1, condition)

print('Binary search with large data: ',locate_cards_binary(large_test['input']['cards'], large_test['input']['query']))