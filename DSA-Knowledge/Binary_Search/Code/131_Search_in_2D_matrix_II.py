"""
LeetCode Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
Problem Name: Search a 2D Matrix II
Description: Search target in a 2D matrix where rows and columns are sorted.

Folder: Binary_Search
File: 131_Search_in_2D_matrix_II.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Start at top-right corner. Move left if target < cell, down if target > cell.
# Time Complexity: O(N + M)
# Space Complexity: O(1)
def optimal_solution(matrix: list[list[int]], target: int) -> bool:
    if not matrix:
        return False
    n, m = len(matrix), len(matrix[0])
    r, c = 0, m - 1
    
    while r < n and c >= 0:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            c -= 1
        else:
            r += 1
            
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22]], 5), True),
        (([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22]], 20), False)
    ]
    for idx, ((mat, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(mat, target) == expected, f"Test case {idx} failed"
    print("Done.")
