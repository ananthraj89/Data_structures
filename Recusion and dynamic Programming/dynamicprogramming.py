#This is the best version of the problem which we are trying to solve

def lcs_dp(seq1, seq2):
    n1, n2 = len(seq1),len(seq2)

    table = [[0 for x in range(n2+1)] for x in range(n1+1)]
    for i in range(n1):
        for j in range(n2):
            if seq1[i] == seq2[j]:
                table[i+1][j+1] = 1+table[i][j]
            else:
                table[i+1][j+1] = max(table[i][j+1], table[i+1][j])
    return table[-1][-1]
    

example1 = lcs_dp('analogy', 'alchemy')
example3 = lcs_dp('serendipitious', 'precepitation')

print(example3)
print(example1)
