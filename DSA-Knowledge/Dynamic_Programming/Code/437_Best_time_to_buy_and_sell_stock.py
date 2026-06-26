"""
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Problem Name: Best Time to Buy and Sell Stock I
Description: Find maximum profit making at most 1 transaction.

Folder: Dynamic_Programming
File: 437_Best_time_to_buy_and_sell_stock.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(prices: list[int]) -> int:
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([7, 1, 5, 3, 6, 4]) == 5
    print("Done.")
