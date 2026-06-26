"""
LeetCode Link: https://www.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1
Problem Name: Print Longest Common Subsequence
Description: Return the actual string representing the LCS.

Folder: Dynamic_Programming
File: 428_Print_Longest_Common_Subsequence_DP_26.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
def optimal_solution(text1: str, text2: str) -> str:
    n, m = len(text1), len(text2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    # Backtrack
    i, j = n, m
    lcs = []
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(lcs[::-1])

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("abcde", "ace") == "ace"
    print("Done.")
