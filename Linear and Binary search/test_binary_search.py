import unittest

def failed_test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, ", mid_number:", mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'



def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    
    while lo <= hi:
        print("lo:", lo, ", hi:", hi)
        mid = (lo + hi) // 2
        result = failed_test_location(cards, query, mid)
        
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

class TestLocateCard(unittest.TestCase):

    def test_query_in_middle(self):
        self.assertEqual(locate_card([13, 11, 10, 7, 4, 3, 1, 0], 7), 3)

    def test_query_towards_end(self):
        self.assertEqual(locate_card([13, 11, 10, 7, 4, 3, 1, 0], 1), 6)

    def test_query_first_element(self):
        self.assertEqual(locate_card([4, 2, 1, -1], 4), 0)

    def test_query_last_element(self):
        self.assertEqual(locate_card([3, -1, -9, -127], -127), 3)

    def test_single_element(self):
        self.assertEqual(locate_card([6], 6), 0)

    def test_query_not_present(self):
        self.assertEqual(locate_card([9, 7, 5, 2, -9], 4), -1)

    def test_empty_list(self):
        self.assertEqual(locate_card([], 7), -1)

    def test_repeating_numbers(self):
        self.assertEqual(locate_card([8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 3), 7)

    def test_query_multiple_times(self):
        self.assertEqual(locate_card([8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 6), 2)

if __name__ == '__main__':
    unittest.main()
