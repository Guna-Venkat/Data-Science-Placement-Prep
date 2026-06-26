"""
LeetCode Link: https://leetcode.com/problems/unique-paths-ii/
Problem Name: Unique Paths II
Description: Unique paths with obstacles (denoted as 1).

Folder: Dynamic_Programming
File: 412_Unique_paths_II.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(M * N)
# Space Complexity: O(N)
def optimal_solution(obstacleGrid: list[list[int]]) -> int:
    if not obstacleGrid or obstacleGrid[0][0] == 1:
        return 0
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [0] * n
    dp[0] = 1
    
    for r in range(m):
        for c in range(n):
            if obstacleGrid[r][c] == 1:
                dp[c] = 0
            elif c > 0:
                dp[c] += dp[c - 1]
    return dp[-1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert optimal_solution(grid) == 2
    print("Done.")
