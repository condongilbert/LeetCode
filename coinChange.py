#You are given an integer array coins representing denominations of coins and an integer amount. 
#Return the fewest number of coins needed to make up that amount. If it’s not possible, return -1.

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Example
print(coinChange([1, 2, 5], 11))  # Output: 3