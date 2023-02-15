def maximumProfit(prices):
    # Write your code here.
    n = len(prices)
    min_cost = prices[0]
    max_profit = 0
    for i in range(n):
        fianl_price = prices[i]-min_cost
        max_profit = max(max_profit,fianl_price)
        min_cost = min(min_cost,prices[i])
        
    return max_profit
