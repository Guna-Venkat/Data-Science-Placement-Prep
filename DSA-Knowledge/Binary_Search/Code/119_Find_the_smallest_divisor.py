"""
LeetCode Link: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
Problem Name: Find the Smallest Divisor Given a Threshold
Description: Find smallest divisor such that sum of division results is <= threshold.

Folder: Binary_Search
File: 119_Find_the_smallest_divisor.py
"""

import math

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary Search on divisor from 1 to max(nums).
# Time Complexity: O(N * log(max(nums)))
# Space Complexity: O(1)
def optimal_solution(nums: list[int], threshold: int) -> int:
    def get_sum(div):
        total = 0
        for x in nums:
            total += math.ceil(x / div)
        return total

    low, high = 1, max(nums)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if get_sum(mid) <= threshold:
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
        (([1, 2, 5, 9], 6), 5),
        (([44, 22, 33, 11, 1], 5), 44)
    ]
    for idx, ((nums, threshold), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, threshold) == expected, f"Test case {idx} failed"
    print("Done.")
