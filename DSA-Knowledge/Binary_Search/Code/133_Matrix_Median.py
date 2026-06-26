"""
LeetCode Link: https://www.geeksforgeeks.org/problems/matrix-median0728/1
Problem Name: Matrix Median
Description: Find the median of a row-wise sorted matrix of odd dimensions.

Folder: Binary_Search
File: 133_Matrix_Median.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary search on the answer value in range [1, 10^9].
# For a candidate value, count how many elements are <= mid using Upper Bound.
# Time Complexity: O(32 * N * log M)
# Space Complexity: O(1)
def optimal_solution(matrix: list[list[int]]) -> int:
    n = len(matrix)
    m = len(matrix[0])
    
    def count_less_equal(x):
        count = 0
        for r in range(n):
            # Binary search to count elements <= x in row r
            low, high = 0, m - 1
            ans = 0
            while low <= high:
                mid = (low + high) // 2
                if matrix[r][mid] <= x:
                    ans = mid + 1
                    low = mid + 1
                else:
                    high = mid - 1
            count += ans
        return count

    low = 1
    high = int(1e9)
    req = (n * m + 1) // 2
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        if count_less_equal(mid) >= req:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        ([[1, 3, 5], [2, 6, 9], [3, 6, 9]], 5)
    ]
    for idx, (mat, expected) in enumerate(test_cases, 1):
        assert optimal_solution(mat) == expected, f"Test case {idx} failed"
    print("Done.")
