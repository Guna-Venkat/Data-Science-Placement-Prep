"""
LeetCode Link: https://www.geeksforgeeks.org/problems/maximum-sub-array5543/1
Problem Name: Print Subarray with Maximum Subarray Sum
Description: Find and return the actual subarray with the maximum sum.

Folder: Arrays
File: 080_Print_subarray_with_maximum_subarray_sum.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep track of start and end indices of the max subarray window.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> list[int]:
    max_sum = nums[0]
    curr_sum = 0
    start = 0
    temp_start = 0
    end = 0
    
    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i
            
        if curr_sum < 0:
            curr_sum = 0
            temp_start = i + 1
            
    return nums[start:end+1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], [4, -1, 2, 1]),
        ([1], [1])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
