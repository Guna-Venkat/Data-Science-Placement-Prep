"""
LeetCode Link: https://www.geeksforgeeks.org/problems/longest-common-substring1452/1
Problem Name: Longest Common Substring
Description: Find length of longest common substring of two strings.

Folder: Dynamic_Programming
File: 429_Longest_common_substring.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * M)
# Space Complexity: O(M)
def optimal_solution(s1: str, s2: str) -> int:
    m = len(s2)
    dp = [0] * (m + 1)
    max_len = 0
    for char in s1:
        next_dp = [0] * (m + 1)
        for j in range(1, m + 1):
            if char == s2[j - 1]:
                next_dp[j] = 1 + dp[j - 1]
                max_len = max(max_len, next_dp[j])
        dp = next_dp
    return max_len

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("ABCDGH", "ACDGHR") == 4 # "CDGH"
    print("Done.")
