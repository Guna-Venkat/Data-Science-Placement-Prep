"""
LeetCode Link: https://leetcode.com/problems/find-peak-element/
Problem Name: Find Peak Element
Description: Find any peak element in array (strictly greater than neighbors).

Folder: Binary_Search
File: 114_Find_peak_element.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: If arr[mid] < arr[mid+1], a peak must lie on right side. Else on left.
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[-1] > nums[-2]:
        return n - 1
        
    low, high = 1, n - 2
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid] < nums[mid + 1]:
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
        ([1, 2, 3, 1], 2),
        ([1, 2, 1, 3, 5, 6, 4], 5) # index 5 has value 6
    ]
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
    print("Done.")
