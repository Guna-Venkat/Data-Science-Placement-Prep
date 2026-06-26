"""
LeetCode Link: https://www.geeksforgeeks.org/problems/rod-cutting0840/1
Problem Name: Rod Cutting
Description: Cut rod of length N to maximize price. Length price list given.

Folder: Dynamic_Programming
File: 426_Rod_Cutting_Problem_DP_24.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Unbounded knapsack setup where wt[i] = i + 1, capacity = N.
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(price: list[int], n: int) -> int:
    dp = [0] * (n + 1)
    for i in range(n):
        wt = i + 1
        val = price[i]
        for t in range(wt, n + 1):
            dp[t] = max(dp[t], val + dp[t - wt])
    return dp[n]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 5, 8, 9, 10, 17, 17, 20], 8) == 22
    print("Done.")
