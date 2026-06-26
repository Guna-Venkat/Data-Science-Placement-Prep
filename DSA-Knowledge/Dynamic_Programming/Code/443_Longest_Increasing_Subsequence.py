"""
LeetCode Link: https://leetcode.com/problems/longest-increasing-subsequence/
Problem Name: Longest Increasing Subsequence
Description: Length of longest strictly increasing subsequence.

Folder: Dynamic_Programming
File: 443_Longest_Increasing_Subsequence.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(nums: list[int]) -> int:
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    print("Done.")
