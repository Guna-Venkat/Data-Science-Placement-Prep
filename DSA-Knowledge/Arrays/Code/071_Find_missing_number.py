"""
LeetCode Link: https://leetcode.com/problems/missing-number/
Problem Name: Missing Number
Description: Find the single missing number in the range [0, N] from an array of size N.

Folder: Arrays
File: 071_Find_missing_number.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Calculate expected sum of [0, N] and subtract the array sum.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([3, 0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
