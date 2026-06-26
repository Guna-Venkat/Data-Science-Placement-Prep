"""
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
Problem Name: Best Time to Buy and Sell Stock IV
Description: Maximize profit making at most K transactions.

Folder: Dynamic_Programming
File: 440_Best_time_to_buy_and_sell_stock_IV.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * K)
# Space Complexity: O(K)
def optimal_solution(k: int, prices: list[int]) -> int:
    if not prices:
        return 0
    costs = [float('inf')] * k
    profits = [0] * k
    for price in prices:
        for i in range(k):
            prev_profit = profits[i - 1] if i > 0 else 0
            costs[i] = min(costs[i], price - prev_profit)
            profits[i] = max(profits[i], price - costs[i])
    return profits[-1] if k > 0 else 0

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(2, [3, 2, 6, 5, 0, 3]) == 7
    print("Done.")
