def best_profit(values):
    least_value = float('inf')
    higher_value = 0

    for value in values:
        if value < least_value:
            least_value = value
        else:
            profit = value - least_value
            if profit > higher_value:
                higher_value = profit
    
    return higher_value


values = [100300,1234000,39907,402876,932187]
print("Maximum Profit = ", best_profit(values))