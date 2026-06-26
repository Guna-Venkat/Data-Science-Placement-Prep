"""
LeetCode Link: https://leetcode.com/problems/single-element-in-a-sorted-array/
Problem Name: Single Element in a Sorted Array
Description: Find the element that appears only once in a sorted array of duplicates.

Folder: Binary_Search
File: 113_Single_element_in_a_Sorted_Array.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Pairs before the single element start at (even, odd) indices.
# Pairs after the single element start at (odd, even) indices.
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    if nums[0] != nums[1]:
        return nums[0]
    if nums[-1] != nums[-2]:
        return nums[-1]
        
    low, high = 1, n - 2
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]
            
        # (even, odd) check
        if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
        ([3, 3, 7, 7, 10, 11, 11], 10)
    ]
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
    print("Done.")
