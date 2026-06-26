"""
LeetCode Link: https://leetcode.com/problems/search-insert-position/
Problem Name: Search Insert Position
Description: Find index where target should be inserted in a sorted array to maintain order.

Folder: Binary_Search
File: 105_Search_insert_position.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Insertion index is exactly the Lower Bound of target.
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    ans = len(nums)
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([1, 3, 5, 6], 5), 2),
        (([1, 3, 5, 6], 2), 1),
        (([1, 3, 5, 6], 7), 4)
    ]
    for idx, ((nums, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, target) == expected, f"Test case {idx} failed"
    print("Done.")
