"""
LeetCode Link: https://leetcode.com/problems/coin-change-ii/
Problem Name: Coin Change 2
Description: Number of combinations that make up amount. Unlimited reuse.

Folder: Dynamic_Programming
File: 424_Coin_Change_2_DP_22.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(Coins * Amount)
# Space Complexity: O(Amount)
def optimal_solution(amount: int, coins: list[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for t in range(coin, amount + 1):
            dp[t] += dp[t - coin]
    return dp[amount]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(5, [1, 2, 5]) == 4
    print("Done.")
