"""
LeetCode Link: https://leetcode.com/problems/set-matrix-zeroes/
Problem Name: Set Matrix Zeroes
Description: If an element is 0, set its entire row and column to 0.

Folder: Arrays
File: 086_Set_Matrix_Zeroes.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Use first row and first column of matrix as markers. 
# Track if first row/col themselves need to be zeroed using separate boolean flags.
# Time Complexity: O(N * M)
# Space Complexity: O(1)
def optimal_solution(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix:
        return matrix
    n, m = len(matrix), len(matrix[0])
    first_row_zero = False
    first_col_zero = False
    
    # Check if first row/col has zeros
    for j in range(m):
        if matrix[0][j] == 0:
            first_row_zero = True
    for i in range(n):
        if matrix[i][0] == 0:
            first_col_zero = True
            
    # Mark zeros in first row/col
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
                
    # Update cells using markers
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
                
    # Update first row/col if needed
    if first_row_zero:
        for j in range(m):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(n):
            matrix[i][0] = 0
            
    return matrix

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
    ]
    
    for idx, (mat, expected) in enumerate(test_cases, 1):
        # deep copy
        mat_copy = [row[:] for row in mat]
        assert optimal_solution(mat_copy) == expected, f"Test case {idx} failed"
        
    print("Done.")
