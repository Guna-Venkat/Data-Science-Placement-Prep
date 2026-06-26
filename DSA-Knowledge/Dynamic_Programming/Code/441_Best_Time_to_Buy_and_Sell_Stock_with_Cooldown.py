"""
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
Problem Name: Best Time to Buy and Sell Stock with Cooldown
Description: Maximize profit with cooldown of 1 day after sell.

Folder: Dynamic_Programming
File: 441_Best_Time_to_Buy_and_Sell_Stock_with_Cooldown.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(prices: list[int]) -> int:
    if not prices:
        return 0
    # State tracking: buy[i], sell[i], cooldown[i]
    # buy: max profit ending with buy (or hold buy)
    # sell: max profit ending with sell
    # cooldown: max profit in cooldown
    buy = -prices[0]
    sell = 0
    cooldown = 0
    for price in prices[1:]:
        prev_sell = sell
        sell = max(sell, buy + price)
        buy = max(buy, cooldown - price)
        cooldown = max(cooldown, prev_sell)
    return sell

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 3, 0, 2]) == 3
    print("Done.")
