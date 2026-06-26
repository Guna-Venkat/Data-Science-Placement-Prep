"""
LeetCode Link: https://leetcode.com/problems/coin-change/
Problem Name: Coin Change (Minimum Coins)
Description: Fewest number of coins needed to make up amount.

Folder: Dynamic_Programming
File: 422_Minimum_Coins_DP_20.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(Coins * Amount)
# Space Complexity: O(Amount)
def optimal_solution(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for t in range(coin, amount + 1):
            dp[t] = min(dp[t], 1 + dp[t - coin])
    return dp[amount] if dp[amount] != float('inf') else -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 5], 11) == 3
    assert optimal_solution([2], 3) == -1
    print("Done.")
