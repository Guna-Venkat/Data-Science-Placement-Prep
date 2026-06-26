"""
LeetCode Link: https://www.geeksforgeeks.org/problems/minimal-cost/1
Problem Name: Frog Jump with K Distance
Description: Frog can jump at most K steps. Find minimal energy loss.

Folder: Dynamic_Programming
File: 407_Frog_Jump_with_K_Distance.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * K)
# Space Complexity: O(N)
def optimal_solution(heights: list[int], k: int) -> int:
    n = len(heights)
    dp = [0] * n
    for i in range(1, n):
        min_steps = float('inf')
        for j in range(1, min(i, k) + 1):
            min_steps = min(min_steps, dp[i - j] + abs(heights[i] - heights[i - j]))
        dp[i] = min_steps
    return dp[-1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([10, 30, 40, 50, 20], 3) == 30
    print("Done.")
