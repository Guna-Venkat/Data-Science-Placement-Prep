"""
LeetCode Link: https://leetcode.com/problems/minimum-falling-path-sum/
Problem Name: Minimum Falling Path Sum
Description: Minimum sum of falling path from top row to bottom row.

Folder: Dynamic_Programming
File: 413_Minimum_Falling_Path_Sum.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(matrix: list[list[int]]) -> int:
    n = len(matrix)
    prev = list(matrix[0])
    
    for r in range(1, n):
        curr = [0] * n
        for c in range(n):
            val = matrix[r][c]
            mid = prev[c]
            left = prev[c - 1] if c > 0 else float('inf')
            right = prev[c + 1] if c < n - 1 else float('inf')
            curr[c] = val + min(mid, left, right)
        prev = curr
    return min(prev)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    assert optimal_solution(matrix) == 13
    print("Done.")
