import unittest

def locate_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
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
