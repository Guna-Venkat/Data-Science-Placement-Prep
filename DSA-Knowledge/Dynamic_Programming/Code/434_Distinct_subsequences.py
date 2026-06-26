"""
LeetCode Link: https://leetcode.com/problems/distinct-subsequences/
Problem Name: Distinct Subsequences
Description: Count number of times string T appears as subsequence in string S.

Folder: Dynamic_Programming
File: 434_Distinct_subsequences.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * M)
# Space Complexity: O(M)
def optimal_solution(s: str, t: str) -> int:
    m = len(t)
    dp = [0] * (m + 1)
    dp[0] = 1 # Empty string t is always a subsequence
    
    for char in s:
        # Backwards iteration to use single row
        for j in range(m, 0, -1):
            if char == t[j - 1]:
                dp[j] = dp[j] + dp[j - 1]
    return dp[m]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("rabbbit", "rabbit") == 3
    print("Done.")
