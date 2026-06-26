"""
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
Problem Name: Best Time to Buy and Sell Stock with Transaction Fee
Description: Maximize profit with transaction fee per transaction.

Folder: Dynamic_Programming
File: 442_Best_time_to_buy_and_sell_stock_with_transaction_fees.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(prices: list[int], fee: int) -> int:
    # hold: max profit holding stock
    # free: max profit not holding stock
    hold = -prices[0]
    free = 0
    for price in prices[1:]:
        free = max(free, hold + price - fee)
        hold = max(hold, free - price)
    return free

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 3, 2, 8, 4, 9], 2) == 8
    print("Done.")
