"""
LeetCode Link: https://leetcode.com/problems/longest-common-subsequence/
Problem Name: Longest Common Subsequence
Description: Length of longest common subsequence of two strings.

Folder: Dynamic_Programming
File: 427_Longest_common_subsequence.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * M)
# Space Complexity: O(M) space optimized
def optimal_solution(text1: str, text2: str) -> int:
    m = len(text2)
    dp = [0] * (m + 1)
    
    for c1 in text1:
        next_dp = [0] * (m + 1)
        for j in range(1, m + 1):
            if c1 == text2[j - 1]:
                next_dp[j] = 1 + dp[j - 1]
            else:
                next_dp[j] = max(dp[j], next_dp[j - 1])
        dp = next_dp
    return dp[m]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("abcde", "ace") == 3
    print("Done.")
