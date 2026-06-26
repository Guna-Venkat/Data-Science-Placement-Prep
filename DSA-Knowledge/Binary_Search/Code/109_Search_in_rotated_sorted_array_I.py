"""
LeetCode Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
Problem Name: Search in Rotated Sorted Array
Description: Search for target in rotated sorted array of unique elements.

Folder: Binary_Search
File: 109_Search_in_rotated_sorted_array_I.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Identify the sorted half. Check if target lies in that half; else search other half.
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        # Left half sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half sorted
        else:
            if nums[mid] < target <= nums[high]:
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
        (([4, 5, 6, 7, 0, 1, 2], 0), 4),
        (([4, 5, 6, 7, 0, 1, 2], 3), -1)
    ]
    for idx, ((nums, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, target) == expected, f"Test case {idx} failed"
    print("Done.")
