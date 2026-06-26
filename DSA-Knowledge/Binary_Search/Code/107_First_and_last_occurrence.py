"""
LeetCode Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Problem Name: Find First and Last Position of Element in Sorted Array
Description: Find the starting and ending index of a given target value in sorted array.

Folder: Binary_Search
File: 107_First_and_last_occurrence.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int], target: int) -> list[int]:
    def find_first():
        low, high = 0, len(nums) - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first

    def find_last():
        low, high = 0, len(nums) - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last

    return [find_first(), find_last()]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([5, 7, 7, 8, 8, 10], 8), [3, 4]),
        (([5, 7, 7, 8, 8, 10], 6), [-1, -1])
    ]
    for idx, ((nums, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, target) == expected, f"Test case {idx} failed"
    print("Done.")
