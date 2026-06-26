"""
LeetCode Link: https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
Problem Name: Minimum Insertions to Make String Palindrome
Description: Return minimum insertions to make string a palindrome.

Folder: Dynamic_Programming
File: 431_Minimum_insertions_to_make_string_palindrome_DP_29.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Result is len(s) - Longest Palindromic Subsequence(s).
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(s: str) -> int:
    n = len(s)
    rev = s[::-1]
    dp = [0] * (n + 1)
    for char in s:
        next_dp = [0] * (n + 1)
        for j in range(1, n + 1):
            if char == rev[j - 1]:
                next_dp[j] = 1 + dp[j - 1]
            else:
                next_dp[j] = max(dp[j], next_dp[j - 1])
        dp = next_dp
    return n - dp[n]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("zzazz") == 0
    assert optimal_solution("mbadm") == 2
    print("Done.")
