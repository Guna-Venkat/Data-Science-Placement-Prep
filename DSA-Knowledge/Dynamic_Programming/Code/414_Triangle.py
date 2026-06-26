"""
LeetCode Link: https://leetcode.com/problems/triangle/
Problem Name: Triangle Minimum Path Sum
Description: Find minimum path sum from top to bottom of triangle grid.

Folder: Dynamic_Programming
File: 414_Triangle.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N^2)
# Space Complexity: O(N) bottom-up
def optimal_solution(triangle: list[list[int]]) -> int:
    n = len(triangle)
    dp = list(triangle[-1])
    for r in range(n - 2, -1, -1):
        for c in range(r + 1):
            dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])
    return dp[0]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    assert optimal_solution(triangle) == 11
    print("Done.")
