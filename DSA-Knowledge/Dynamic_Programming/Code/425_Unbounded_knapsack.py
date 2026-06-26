"""
LeetCode Link: https://www.geeksforgeeks.org/problems/unbounded-knapsack5444/1
Problem Name: Unbounded Knapsack
Description: Pick items to maximize profit within capacity. Unlimited repetitions.

Folder: Dynamic_Programming
File: 425_Unbounded_knapsack.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * W)
# Space Complexity: O(W)
def optimal_solution(val: list[int], wt: list[int], w: int) -> int:
    dp = [0] * (w + 1)
    for i in range(len(val)):
        for t in range(wt[i], w + 1):
            dp[t] = max(dp[t], val[i] + dp[t - wt[i]])
    return dp[w]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 1], [2, 1], 3) == 3
    print("Done.")
