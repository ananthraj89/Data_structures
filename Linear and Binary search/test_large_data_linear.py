import unittest
import time

# Define the locate_card_linear function
def locate_card_linear(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

# Define a helper function to evaluate the performance and correctness
def evaluate_test_case(function, test_case):
    input_data = test_case['input']
    expected_output = test_case['output']
    
    start_time = time.time()
    result = function(**input_data)
    end_time = time.time()
    
    passed = result == expected_output
    runtime = (end_time - start_time) * 1000  # Convert to milliseconds
    
    return result, passed, runtime

# Define the unit test class
class TestLocateCardLinear(unittest.TestCase):
    
    def test_large_case(self):
        large_test = {
            'input': {
                'cards': list(range(10000000, 0, -1)),
                'query': 2
            },
            'output': 9999998
        }
        
        result, passed, runtime = evaluate_test_case(locate_card_linear, large_test)
        self.assertTrue(passed, f"Failed large test case. Expected {large_test['output']} but got {result}.")
        print("Result: {}\nPassed: {}\nExecution Time: {:.2f} ms".format(result, passed, runtime))

  

if __name__ == '__main__':
    unittest.main()

    
#All the tests got exceuted with the time 2.41 sec / 1892.93 msec