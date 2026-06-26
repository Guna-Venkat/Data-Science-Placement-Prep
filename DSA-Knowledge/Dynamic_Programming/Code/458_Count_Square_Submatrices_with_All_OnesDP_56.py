"""
LeetCode Link: https://leetcode.com/problems/count-square-submatrices-with-all-ones/
Problem Name: Count Square Submatrices with All Ones
Description: Count total square submatrices that have all ones.

Folder: Dynamic_Programming
File: 458_Count_Square_Submatrices_with_All_OnesDP_56.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: dp[r][c] represents size of largest square ending at (r, c).
# dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) if matrix[r][c] == 1.
# Total count is sum of all values in dp table.
# Time Complexity: O(R * C)
# Space Complexity: O(C) space optimized
def optimal_solution(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    dp = [0] * cols
    total_squares = 0
    prev_diag = 0 # stores dp[r-1][c-1]
    
    for r in range(rows):
        for c in range(cols):
            temp = dp[c]
            if matrix[r][c] == 1:
                if r == 0 or c == 0:
                    dp[c] = 1
                else:
                    dp[c] = 1 + min(dp[c], dp[c - 1], prev_diag)
                total_squares += dp[c]
            else:
                dp[c] = 0
            prev_diag = temp
    return total_squares

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
    assert optimal_solution(matrix) == 15
    print("Done.")
