"""
LeetCode Link: https://leetcode.com/problems/edit-distance/
Problem Name: Edit Distance
Description: Find minimum operations (insert, delete, replace) to convert word1 to word2.

Folder: Dynamic_Programming
File: 435_Edit_distance.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * M)
# Space Complexity: O(M)
def optimal_solution(word1: str, word2: str) -> int:
    m = len(word2)
    dp = list(range(m + 1))
    
    for char in word1:
        next_dp = [0] * (m + 1)
        next_dp[0] = dp[0] + 1
        for j in range(1, m + 1):
            if char == word2[j - 1]:
                next_dp[j] = dp[j - 1]
            else:
                next_dp[j] = 1 + min(dp[j], next_dp[j - 1], dp[j - 1])
        dp = next_dp
    return dp[m]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("horse", "ros") == 3
    print("Done.")
