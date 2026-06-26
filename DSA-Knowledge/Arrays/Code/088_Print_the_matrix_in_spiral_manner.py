"""
LeetCode Link: https://leetcode.com/problems/spiral-matrix/
Problem Name: Spiral Matrix
Description: Return all elements of the matrix in spiral order.

Folder: Arrays
File: 088_Print_the_matrix_in_spiral_manner.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep track of boundaries: top, bottom, left, right. Traverse boundaries spirally.
# Time Complexity: O(N * M)
# Space Complexity: O(1)
def optimal_solution(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []
        
    n, m = len(matrix), len(matrix[0])
    top, bottom = 0, n - 1
    left, right = 0, m - 1
    result = []
    
    while top <= bottom and left <= right:
        # Traverse Left to Right on Top row
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        
        # Traverse Top to Bottom on Right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Check if rows are exhausted
        if top <= bottom:
            # Traverse Right to Left on Bottom row
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
            
        # Check if columns are exhausted
        if left <= right:
            # Traverse Bottom to Top on Left column
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5])
    ]
    
    for idx, (mat, expected) in enumerate(test_cases, 1):
        assert optimal_solution(mat) == expected, f"Test case {idx} failed"
        
    print("Done.")
