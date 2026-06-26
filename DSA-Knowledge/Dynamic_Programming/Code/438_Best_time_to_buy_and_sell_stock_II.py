"""
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Problem Name: Best Time to Buy and Sell Stock II
Description: Maximize profit making unlimited transactions.

Folder: Dynamic_Programming
File: 438_Best_time_to_buy_and_sell_stock_II.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(prices: list[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([7, 1, 5, 3, 6, 4]) == 7
    print("Done.")
