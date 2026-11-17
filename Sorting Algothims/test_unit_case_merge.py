import unittest
import random


def merge_sort(nums):
    
    #Terminating condition (list 0 or 1 element)
    if len(nums) <= 1:
        return nums
    
    #Get mid point
    mid =len(nums)//2

    #spilt the list
    left_list = nums[:mid]
    right_list = nums[mid:]

    #solve the list recursively
    left_sorted_list, right_sorted_list = merge_sort(left_list), merge_sort(right_list)

    #combine the result of the two halves
    sorted_list = merge(left_sorted_list, right_sorted_list)
    return sorted_list



#helper function
def merge(nums1, nums2):
    #list to be sorted
    merged = []

    #indices for iterations
    i,j = 0, 0

    #Loop over two lists
    while i < len(nums1) and j < len(nums2):
        #include smaller element in the list and move to the next element
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i+=1
        else:
            merged.append(nums2[j])
            j+=1
        
    #Get the remaining parts
    numbers1_tail = nums1[i:]
    numbers2_tail = nums1[j:]
     
    #return the final array
    return merged + numbers1_tail + numbers2_tail


# List of numbers in random order
test0 = {
    'input': {
        'nums': [4, 2, 6, 3, 4, 6, 2, 1]
    },
    'output': [1, 2, 2, 3, 4, 4, 6, 6]
}

# List of numbers in random order
test1 = {
    'input': {
        'nums': [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
    },
    'output': [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]
}

# A list that's already sorted
test2 = {
    'input': {
        'nums': [3, 5, 6, 8, 9, 10, 99]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}

# A list that's sorted in descending order
test3 = {
    'input': {
        'nums': [99, 10, 9, 8, 6, 5, 3]
    },
    'output': [3, 5, 6, 8, 9, 10, 99]
}

# A list containing repeating elements
test4 = {
    'input': {
        'nums': [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
    },
    'output': [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]
}

# An empty list 
test5 = {
    'input': {
        'nums': []
    },
    'output': []
}


# A list containing just one element
test6 = {
    'input': {
        'nums': [23]
    },
    'output': [23]
}

# A list containing one element repeated many times
test7 = {
    'input': {
        'nums': [42, 42, 42, 42, 42, 42, 42]
    },
    'output': [42, 42, 42, 42, 42, 42, 42]
}



in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test8 = {
    'input': {
        'nums': in_list
    },
    'output': out_list
}


tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8]


class TestMergeSort(unittest.TestCase):
    def test_cases(self):
        for i, test in enumerate(tests):
            with self.subTest(test=i):
                input_data = test['input']['nums']
                expected_output = test['output']
                self.assertEqual(merge_sort(input_data), expected_output)



if __name__ == '__main__':
    unittest.main()