#problem on least common subsequence(lcs) we can replace counter by index idx1 or idx2 

#The following program to find the length of longest common sub-sequence 

def lcs_recursive(seq1, seq2, counter1 = 0, counter2 = 0):
    if counter1 == len(seq1) or counter2 == len(seq2):
        return 0 
    elif seq1[counter1] == seq2[counter2]:
        return 1+lcs_recursive(seq1, seq2, counter1+1, counter2+1)
    else:
        option1 =lcs_recursive(seq1, seq2, counter1+1, counter2)
        option2 = lcs_recursive(seq1, seq2, counter1, counter2+1)
        return max(option1, option2)
    

#instances
example1 = lcs_recursive('analogy', 'alchemy')
example2 = lcs_recursive([1,2,3,4,5,6], [2,3,4,-20,10])
example3 = lcs_recursive('serendipitious', 'precepitation')

print(example3)
print(example2)
print(example1)