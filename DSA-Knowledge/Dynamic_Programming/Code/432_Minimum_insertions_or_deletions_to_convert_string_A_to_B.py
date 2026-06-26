"""
LeetCode Link: https://leetcode.com/problems/delete-operation-for-two-strings/
Problem Name: Delete Operation for Two Strings (Min Insert/Delete)
Description: Find minimum steps to make two strings identical (insert or delete).

Folder: Dynamic_Programming
File: 432_Minimum_insertions_or_deletions_to_convert_string_A_to_B.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Result is len(s1) + len(s2) - 2 * LCS(s1, s2).
# Time Complexity: O(N * M)
# Space Complexity: O(M)
def optimal_solution(word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)
    dp = [0] * (m + 1)
    for char in word1:
        next_dp = [0] * (m + 1)
        for j in range(1, m + 1):
            if char == word2[j - 1]:
                next_dp[j] = 1 + dp[j - 1]
            else:
                next_dp[j] = max(dp[j], next_dp[j - 1])
        dp = next_dp
    return n + m - 2 * dp[m]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("sea", "eat") == 2
    print("Done.")
