"""
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Problem Name: Stock Buy and Sell
Description: Maximize single transaction profit.

Folder: Arrays
File: 081_Stock_Buy_and_Sell.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep minimum price seen, check profit on selling at current day.
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
    
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
