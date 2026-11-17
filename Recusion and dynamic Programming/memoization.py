#this is the advanced version of the recursive because of its time and space complexity it can be widely used.


def lcs_memo(seq1, seq2):
    memo = {}
    def recursive(counter1 = 0, counter2 = 0):
        key = (counter1, counter2)
        if key in memo:
            return memo[key]
        elif counter1 == len(seq1) or counter2 == len(seq2):
            memo[key] = 0   #storing result in a dic
        elif seq1[counter1] == seq2[counter2]:
            memo[key] = 1 + recursive(counter1+1, counter2+1)
        else:
            memo[key] = max(recursive(counter1+1, counter2), recursive(counter1, counter2+1))
        return memo[key]
        
    return recursive()
    
example1 = lcs_memo('analogy', 'alchemy')
print(example1)
