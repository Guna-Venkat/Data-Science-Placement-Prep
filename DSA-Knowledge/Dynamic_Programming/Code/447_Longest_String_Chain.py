"""
LeetCode Link: https://leetcode.com/problems/longest-string-chain/
Problem Name: Longest String Chain
Description: Longest chain of strings where words[i] can be formed by adding 1 char to words[i-1].

Folder: Dynamic_Programming
File: 447_Longest_String_Chain.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Sort words by length. Use map dp[word] representing chain length ending at word.
# Time Complexity: O(N * L^2) where L is max word length
# Space Complexity: O(N)
def optimal_solution(words: list[str]) -> int:
    words.sort(key=len)
    dp = {}
    max_chain = 1
    for word in words:
        dp[word] = 1
        for i in range(len(word)):
            prev = word[:i] + word[i+1:]
            if prev in dp:
                dp[word] = max(dp[word], dp[prev] + 1)
        max_chain = max(max_chain, dp[word])
    return max_chain

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(["a","b","ba","bca","bda","bdca"]) == 4
    print("Done.")
