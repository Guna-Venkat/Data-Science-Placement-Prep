"""
LeetCode Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Problem Name: Find Minimum in Rotated Sorted Array
Description: Find the minimum element in a rotated sorted array.

Folder: Binary_Search
File: 111_Find_minimum_in_Rotated_Sorted_Array.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: If left half sorted, nums[low] is potential min. Move search space to right half.
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    low, high = 0, len(nums) - 1
    ans = float('inf')
    while low <= high:
        mid = (low + high) // 2
        # Optimization: Entire segment sorted
        if nums[low] <= nums[high]:
            ans = min(ans, nums[low])
            break
        # Left half sorted
        if nums[low] <= nums[mid]:
            ans = min(ans, nums[low])
            low = mid + 1
        # Right half sorted
        else:
            ans = min(ans, nums[mid])
            high = mid - 1
    return ans

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0)
    ]
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
    print("Done.")
