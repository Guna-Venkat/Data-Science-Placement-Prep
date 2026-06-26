"""
LeetCode Link: https://leetcode.com/problems/binary-search/
Problem Name: Binary Search
Description: Find target X in a sorted array. Return index if found, else -1.

Folder: Binary_Search
File: 102_Search_X_in_sorted_array.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
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
        (([-1, 0, 3, 5, 9, 12], 9), 4),
        (([-1, 0, 3, 5, 9, 12], 2), -1)
    ]
    for idx, ((nums, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, target) == expected, f"Test case {idx} failed"
    print("Done.")
