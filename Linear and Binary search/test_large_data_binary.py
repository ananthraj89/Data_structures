import unittest
import time

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1  
        elif mid_number > query:
            lo = mid + 1
    
    return -1

def evaluate_test_case(function, test_case):
    input_data = test_case['input']
    expected_output = test_case['output']
    
    start_time = time.time()
    result = function(**input_data)
    end_time = time.time()
    
    passed = result == expected_output
    runtime = (end_time - start_time) * 1000  # Convert to milliseconds
    
    return result, passed, runtime

class TestLocateCard(unittest.TestCase):

    def test_large_case(self):
        large_test = {
            'input': {
                'cards': list(range(10000000, 0, -1)),
                'query': 2
            },
            'output': 9999998
        }
        
        result, passed, runtime = evaluate_test_case(locate_card, large_test)
        self.assertTrue(passed, f"Failed large test case. Expected {large_test['output']} but got {result}.")
        print("Result: {}\nPassed: {}\nExecution Time: {:.2f} ms".format(result, passed, runtime))

if __name__ == '__main__':
    unittest.main()


# Test will execute with the time complexity of 5.65 ms, Ran 1 test in 0.475sec 