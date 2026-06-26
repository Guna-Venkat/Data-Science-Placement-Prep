"""
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
Problem Name: Best Time to Buy and Sell Stock III
Description: Maximize profit making at most 2 transactions.

Folder: Dynamic_Programming
File: 439_Best_time_to_buy_and_sell_stock_III.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(prices: list[int]) -> int:
    # Track min price and max profit for transaction 1 and 2
    cost1, cost2 = float('inf'), float('inf')
    profit1, profit2 = 0, 0
    for price in prices:
        cost1 = min(cost1, price)
        profit1 = max(profit1, price - cost1)
        cost2 = min(cost2, price - profit1) # reinvest profit1
        profit2 = max(profit2, price - cost2)
    return profit2

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([3, 3, 5, 0, 0, 8, 2, 5]) == 19
    print("Done.")
