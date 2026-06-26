"""
LeetCode Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
Problem Name: Search in Rotated Sorted Array II (with duplicates)
Description: Search target in rotated sorted array when duplicates are present.

Folder: Binary_Search
File: 110_Search_in_rotated_sorted_array_II.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Handle the edge case when nums[low] == nums[mid] == nums[high] by shrinking pointers.
# Time Complexity: O(log N) average, O(N) worst-case
# Space Complexity: O(1)
def optimal_solution(nums: list[int], target: int) -> bool:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
            
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue
            
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
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([2, 5, 6, 0, 0, 1, 2], 0), True),
        (([2, 5, 6, 0, 0, 1, 2], 3), False)
    ]
    for idx, ((nums, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, target) == expected, f"Test case {idx} failed"
    print("Done.")
