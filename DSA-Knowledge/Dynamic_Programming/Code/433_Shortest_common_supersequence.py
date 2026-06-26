"""
LeetCode Link: https://leetcode.com/problems/shortest-common-supersequence/
Problem Name: Shortest Common Supersequence
Description: Find shortest supersequence that contains both strings as subsequences.

Folder: Dynamic_Programming
File: 433_Shortest_common_supersequence.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * M)
# Space Complexity: O(N * M) for backtracking matrix
def optimal_solution(str1: str, str2: str) -> str:
    n, m = len(str1), len(str2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
    i, j = n, m
    ans = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            ans.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            ans.append(str1[i - 1])
            i -= 1
        else:
            ans.append(str2[j - 1])
            j -= 1
            
    while i > 0:
        ans.append(str1[i - 1])
        i -= 1
    while j > 0:
        ans.append(str2[j - 1])
        j -= 1
        
    return "".join(ans[::-1])

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("abac", "cab") == "cabac"
    print("Done.")
