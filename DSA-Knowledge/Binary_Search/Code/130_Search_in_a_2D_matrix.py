"""
LeetCode Link: https://leetcode.com/problems/search-a-2d-matrix/
Problem Name: Search a 2D Matrix
Description: Search target in 2D matrix where rows are sorted and first integer of each row is greater than last.

Folder: Binary_Search
File: 130_Search_in_a_2D_matrix.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Treat the 2D matrix as a flattened 1D array of size N * M.
# Time Complexity: O(log(N * M))
# Space Complexity: O(1)
def optimal_solution(matrix: list[list[int]], target: int) -> bool:
    if not matrix:
        return False
    n, m = len(matrix), len(matrix[0])
    low, high = 0, n * m - 1
    
    while low <= high:
        mid = (low + high) // 2
        r = mid // m
        c = mid % m
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), True),
        (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13), False)
    ]
    for idx, ((mat, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(mat, target) == expected, f"Test case {idx} failed"
    print("Done.")
