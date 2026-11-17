# Merger Sort:

# if input list is empty or just contains just one element its already sorted.
# if not didvide the list in to two numbers roughly equal parts.
# sort each part recursively using merge sort algorithm.
# Manage the two sorted lists and get the single sorted list.

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

input = merge([1,4,7,9,11], [-1,0,2,3,8])
output = [-1,0, 1, 2, 3, 4, 7, 8, 9, 11]
print(input == output)

input2 = [25, 30, 1, 100, -500, -23, 8]
output2 = [-500, -23, 1, 8, 25,  30, 100]
result = merge_sort(input2)

print(result)
print(output2 == result)