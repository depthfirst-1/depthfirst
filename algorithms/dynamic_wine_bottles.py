def maximize_profit(wines):
    # Initialize the process
    max_profit = cal_maximum_profit(0, len(wines) - 1, 1, wines)
    return max_profit

# Create a memoization table
memo = {}

def cal_maximum_profit(start, end, year, wines):
    if start > end:
        return 0
    
    key = (start, end)
    if key in memo:
        return memo[key]
    
    # Sell the bottle from the left
    profit_left = (year * wines[start]) + cal_maximum_profit(start + 1, end, year + 1, wines)
    # Sell the bottle from the right
    profit_right = (year * wines[end]) + cal_maximum_profit(start, end - 1, year + 1, wines)
    
    memo[key] = max(profit_left, profit_right)
        
    return memo[key]


wines_bottles = [2, 3, 5, 1, 4]

print("Maximum Profit:", maximize_profit(wines_bottles))
