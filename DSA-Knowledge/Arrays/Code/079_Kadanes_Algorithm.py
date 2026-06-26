"""
LeetCode Link: https://leetcode.com/problems/maximum-subarray/
Problem Name: Maximum Subarray Sum (Kadane's Algorithm)
Description: Find the contiguous subarray which has the largest sum.

Folder: Arrays
File: 079_Kadanes_Algorithm.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Accumulate running sum. Reset to 0 if sum drops below 0. Track max.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    max_sum = nums[0]
    curr_sum = 0
    for x in nums:
        curr_sum += x
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
