"""
LeetCode Link: https://leetcode.com/problems/burst-balloons/
Problem Name: Burst Balloons
Description: Burst balloons to maximize coins collected.

Folder: Dynamic_Programming
File: 453_Burst_balloons.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: MCM layout. Define subproblem as last balloon to burst in range (i, j).
# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
def optimal_solution(nums: list[int]) -> int:
    arr = [1] + nums + [1]
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    
    for l in range(1, n - 1):
        for i in range(1, n - l):
            j = i + l - 1
            for k in range(i, j + 1):
                coins = arr[i - 1] * arr[k] * arr[j + 1]
                coins += dp[i][k - 1] + dp[k + 1][j]
                dp[i][j] = max(dp[i][j], coins)
                
    return dp[1][n - 2]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([3, 1, 5, 8]) == 167
    print("Done.")
