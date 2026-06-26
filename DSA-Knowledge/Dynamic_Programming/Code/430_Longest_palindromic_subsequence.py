"""
LeetCode Link: https://leetcode.com/problems/longest-palindromic-subsequence/
Problem Name: Longest Palindromic Subsequence
Description: Find length of longest palindromic subsequence of string.

Folder: Dynamic_Programming
File: 430_Longest_palindromic_subsequence.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: LCS of string s and its reverse s[::-1].
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(s: str) -> int:
    s_rev = s[::-1]
    n = len(s)
    dp = [0] * (n + 1)
    for char in s:
        next_dp = [0] * (n + 1)
        for j in range(1, n + 1):
            if char == s_rev[j - 1]:
                next_dp[j] = 1 + dp[j - 1]
            else:
                next_dp[j] = max(dp[j], next_dp[j - 1])
        dp = next_dp
    return dp[n]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("bbbab") == 4
    print("Done.")
