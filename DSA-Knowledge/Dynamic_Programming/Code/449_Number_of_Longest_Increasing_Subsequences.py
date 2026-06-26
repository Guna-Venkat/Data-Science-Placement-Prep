"""
LeetCode Link: https://leetcode.com/problems/number-of-longest-increasing-subsequence/
Problem Name: Number of Longest Increasing Subsequences
Description: Count number of LIS possible.

Folder: Dynamic_Programming
File: 449_Number_of_Longest_Increasing_Subsequences.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep dp[i] representing length of LIS ending at i, and count[i] representing total ways.
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(nums: list[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n
    count = [1] * n
    
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    count[i] = count[j]
                elif dp[j] + 1 == dp[i]:
                    count[i] += count[j]
                    
    max_len = max(dp)
    ans = 0
    for i in range(n):
        if dp[i] == max_len:
            ans += count[i]
    return ans

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 3, 5, 4, 7]) == 2
    print("Done.")
