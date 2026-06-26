"""
LeetCode Link: https://leetcode.com/problems/unique-paths/
Problem Name: Unique Paths
Description: Count unique paths from top-left to bottom-right in m x n grid.

Folder: Dynamic_Programming
File: 411_Grid_Unique_Paths_DP_on_Grids_DP8.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(M * N)
# Space Complexity: O(N)
def optimal_solution(m: int, n: int) -> int:
    prev = [1] * n
    for i in range(1, m):
        curr = [1] * n
        for j in range(1, n):
            curr[j] = curr[j - 1] + prev[j]
        prev = curr
    return prev[-1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(3, 7) == 28
    assert optimal_solution(3, 2) == 3
    print("Done.")
