#In this we shall learn about the knapsack problem in dynamic programming




def max_profit_dp(weights, profits, capacity):
    n = len(weights)
    
    # Create a table to store results of subproblems
    table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the table in a bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(table[i - 1][j], profits[i - 1] + table[i - 1][j - weights[i - 1]])
    
    # The last cell of the table contains the maximum profit
    return table[n][capacity]

weights_1 = [1, 2, 3, 10, 34, 20, 7, 8, 16]
profits_1 = [2, 6, 8, 10, 20, 0, 5, 2, 9]
capacity_1 = 50

example_1 = max_profit_dp(weights_1, profits_1, capacity_1)
print(example_1)
