"""
LeetCode Link: https://leetcode.com/problems/longest-increasing-subsequence/
Problem Name: Longest Increasing Subsequence (Binary Search)
Description: Compute LIS in O(N log N) time using binary search (piles / patience sorting).

Folder: Dynamic_Programming
File: 445_Longest_Increasing_Subsequence_DP_43.py
"""

import bisect

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N log N)
# Space Complexity: O(N)
def optimal_solution(nums: list[int]) -> int:
    sub = []
    for num in nums:
        idx = bisect.bisect_left(sub, num)
        if idx == len(sub):
            sub.append(num)
        else:
            sub[idx] = num
    return len(sub)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    print("Done.")
