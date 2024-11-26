def maxProfit(prices):
    min_price = float('inf')  # Initialize minimum price
    max_profit = 0           # Initialize maximum profit

    for price in prices:
        if price < min_price:
            min_price = price  # Update minimum price
        else:
            max_profit = max(max_profit, price - min_price)  # Calculate and update max profit

    return max_profit