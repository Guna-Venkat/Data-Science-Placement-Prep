"""
LeetCode Link: https://leetcode.com/problems/wildcard-matching/
Problem Name: Wildcard Matching
Description: Match string s with pattern p supporting '?' and '*'.

Folder: Dynamic_Programming
File: 436_Wildcard_matching.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * M)
# Space Complexity: O(M)
def optimal_solution(s: str, p: str) -> bool:
    m = len(p)
    dp = [False] * (m + 1)
    dp[0] = True
    for j in range(1, m + 1):
        if p[j - 1] == '*':
            dp[j] = dp[j - 1]
            
    for char in s:
        next_dp = [False] * (m + 1)
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                next_dp[j] = next_dp[j - 1] or dp[j]
            elif p[j - 1] == '?' or char == p[j - 1]:
                next_dp[j] = dp[j - 1]
        dp = next_dp
    return dp[m]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("aa", "*") == True
    assert optimal_solution("cb", "?a") == False
    print("Done.")
