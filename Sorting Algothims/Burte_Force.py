#Bubble sort

#Iterate over the list of numbers starting from left
#Compare each number with the number that follows it.
#If the number is greater than the one that follows it, swap the two elements.
#Repeat the above steps until the elements are completely sorted.


def bubble_sort(nums):
    #create a copy of the list of elements to avaoid the changing.
    nums = list(nums)

    #repeat the above process (n-1) times
    for i in range(len(nums)-1):

        #Iterate over the list of numbers
        for j in range(len(nums)-1):

            #compare
            if nums[j] > nums[j+1]:

                #swap them
                nums[j], nums[j+1] = nums[j+1], nums[j]

    #return sorted list
    return nums




input = [25, 30, 1, 100, -500, -23, 8]
output = [-500, -23, 1, 8, 25,  30, 100]
result = bubble_sort(input)

print(result)
print(output == result)

 
