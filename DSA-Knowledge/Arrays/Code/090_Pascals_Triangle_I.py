"""
LeetCode Link: https://leetcode.com/problems/pascals-triangle/
Problem Name: Pascal's Triangle
Description: Generate the first numRows of Pascal's triangle.

Folder: Arrays
File: 090_Pascals_Triangle_I.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Each element of a row is the sum of the two elements directly above it.
# Time Complexity: O(numRows^2)
# Space Complexity: O(numRows^2) for the output triangle structure
def optimal_solution(numRows: int) -> list[list[int]]:
    triangle = []
    for r in range(numRows):
        row = [1] * (r + 1)
        for j in range(1, r):
            row[j] = triangle[r - 1][j - 1] + triangle[r - 1][j]
        triangle.append(row)
    return triangle

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]])
    ]
    
    for idx, (numRows, expected) in enumerate(test_cases, 1):
        assert optimal_solution(numRows) == expected, f"Test case {idx} failed"
        
    print("Done.")
