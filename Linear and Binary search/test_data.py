def locate_card(cards, query):
    try:
        return cards.index(query)
    except ValueError:
        return -1

# Testing framework
def run_tests():
    tests = []

    # Query occurs in the middle
    tests.append({
        'input': { 
            'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
            'query': 7
        },
        'output': 3
    })

    # Query occurs towards the end
    tests.append({
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 1
        },
        'output': 6
    })

    # Query is the first element
    tests.append({
        'input': {
            'cards': [4, 2, 1, -1],
            'query': 4
        },
        'output': 0
    })

    # Query is the last element
    tests.append({
        'input': {
            'cards': [3, -1, -9, -127],
            'query': -127
        },
        'output': 3
    })

    # Cards contains just one element, query
    tests.append({
        'input': {
            'cards': [6],
            'query': 6
        },
        'output': 0 
    })

    # Cards does not contain query 
    tests.append({
        'input': {
            'cards': [9, 7, 5, 2, -9],
            'query': 4
        },
        'output': -1
    })

    # Cards is empty
    tests.append({
        'input': {
            'cards': [],
            'query': 7
        },
        'output': -1
    })

    # Numbers can repeat in cards
    tests.append({
        'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'query': 3
        },
        'output': 7
    })

    # Query occurs multiple times
    tests.append({
        'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'query': 6
        },
        'output': 2
    })

    # Run the tests
    for i, test in enumerate(tests):
        result = locate_card(test['input']['cards'], test['input']['query'])
        if result == test['output']:
            print(f"Test case {i + 1} passed.")
        else:
            print(f"Test case {i + 1} failed: expected {test['output']}, got {result}.")

run_tests()
