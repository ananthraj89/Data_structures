#In this we shall learn about the knapscak recursive function

def max_profit_recursive(weights, profits, capacity, counter = 0):
    if counter == len(weights):
        return 0 
    elif weights[counter] > capacity:
        return max_profit_recursive(weights, profits, capacity, counter+1)
    else:
        option1 = max_profit_recursive(weights, profits, capacity, counter+1)
        option2 = profits[counter] + max_profit_recursive(weights, profits, capacity - weights[counter], counter + 1)
    
    return max(option1, option2)


weights_1 = [1, 2, 3, 10, 34, 20, 7, 8, 16]
profits_1 = [2, 6, 8, 10, 20, 0, 5, 2, 9]
capacity_1 = 50

example_1 = max_profit_recursive(weights_1, profits_1, capacity_1)
print(example_1)
