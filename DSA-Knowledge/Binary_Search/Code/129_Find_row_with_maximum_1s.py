"""
LeetCode Link: https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1
Problem Name: Row with Max 1s
Description: Find row index with maximum number of 1s in a boolean 2D array.

Folder: Binary_Search
File: 129_Find_row_with_maximum_1s.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Start at top-right corner. Move left if cell is 1, move down if cell is 0.
# Time Complexity: O(N + M)
# Space Complexity: O(1)
def optimal_solution(matrix: list[list[int]]) -> int:
    if not matrix:
        return -1
    n = len(matrix)
    m = len(matrix[0])
    
    r = 0
    c = m - 1
    max_row = -1
    
    while r < n and c >= 0:
        if matrix[r][c] == 1:
            max_row = r
            c -= 1
        else:
            r += 1
            
    return max_row

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        ([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]], 2)
    ]
    for idx, (mat, expected) in enumerate(test_cases, 1):
        assert optimal_solution(mat) == expected, f"Test case {idx} failed"
    print("Done.")
