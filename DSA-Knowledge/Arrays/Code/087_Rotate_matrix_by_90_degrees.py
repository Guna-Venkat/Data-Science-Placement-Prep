"""
LeetCode Link: https://leetcode.com/problems/rotate-image/
Problem Name: Rotate Image (Rotate matrix by 90 degrees)
Description: Rotate N x N matrix by 90 degrees clockwise in-place.

Folder: Arrays
File: 087_Rotate_matrix_by_90_degrees.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Transpose the matrix (swap matrix[i][j] with matrix[j][i]), then reverse each row.
# Time Complexity: O(N^2)
# Space Complexity: O(1)
def optimal_solution(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    
    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # Reverse rows
    for i in range(n):
        matrix[i].reverse()
        
    return matrix

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
    ]
    
    for idx, (mat, expected) in enumerate(test_cases, 1):
        mat_copy = [row[:] for row in mat]
        assert optimal_solution(mat_copy) == expected, f"Test case {idx} failed"
        
    print("Done.")
