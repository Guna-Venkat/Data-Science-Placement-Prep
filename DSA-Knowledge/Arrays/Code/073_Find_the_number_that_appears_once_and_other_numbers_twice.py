"""
LeetCode Link: https://leetcode.com/problems/single-number/
Problem Name: Single Number
Description: Given a non-empty array of integers where every element appears twice except for one, find that single one.

Folder: Arrays
File: 073_Find_the_number_that_appears_once_and_other_numbers_twice.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: XORing a number with itself cancels it out (x ^ x = 0). XORing with 0 preserves (x ^ 0 = x).
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    xor = 0
    for num in nums:
        xor ^= num
    return xor

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
