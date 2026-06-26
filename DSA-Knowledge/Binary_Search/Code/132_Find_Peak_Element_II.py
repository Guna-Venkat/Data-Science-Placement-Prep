"""
LeetCode Link: https://leetcode.com/problems/find-a-peak-element-ii/
Problem Name: Find a Peak Element II (2D Peak)
Description: Find a peak element in a 2D grid.

Folder: Binary_Search
File: 132_Find_Peak_Element_II.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary search on columns. Find row with max element in the column.
# Compare with neighbors on left and right columns.
# Time Complexity: O(M * log N) where M is row count and N is col count.
# Space Complexity: O(1)
def optimal_solution(mat: list[list[int]]) -> list[int]:
    n = len(mat)
    m = len(mat[0])
    low = 0
    high = m - 1
    
    while low <= high:
        mid_col = (low + high) // 2
        
        # Find row with max element in mid_col
        max_row = 0
        for r in range(n):
            if mat[r][mid_col] > mat[max_row][mid_col]:
                max_row = r
                
        left_val = mat[max_row][mid_col - 1] if mid_col > 0 else -1
        right_val = mat[max_row][mid_col + 1] if mid_col < m - 1 else -1
        
        if mat[max_row][mid_col] > left_val and mat[max_row][mid_col] > right_val:
            return [max_row, mid_col]
        elif mat[max_row][mid_col] < left_val:
            high = mid_col - 1
        else:
            low = mid_col + 1
            
    return [-1, -1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        ([[1, 4], [3, 2]], [0, 1]), # 4 is a peak
        ([[10, 20, 15], [21, 30, 14], [7, 16, 32]], [1, 1]) # 30 is a peak
    ]
    for idx, (mat, expected) in enumerate(test_cases, 1):
        assert optimal_solution(mat) == expected, f"Test case {idx} failed"
    print("Done.")
