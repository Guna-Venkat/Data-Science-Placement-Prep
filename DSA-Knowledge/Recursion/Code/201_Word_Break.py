"""
LeetCode Link: https://leetcode.com/problems/word-break/
Problem Name: Word Break
Description: Check if a string can be segmented into dictionary words.

Folder: Recursion
File: 201_Word_Break.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Backtracking with Memoization.
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(s: str, wordDict: list[str]) -> bool:
    words = set(wordDict)
    memo = {}
    
    def solve(idx):
        if idx == len(s):
            return True
        if idx in memo:
            return memo[idx]
            
        for i in range(idx, len(s)):
            if s[idx:i+1] in words:
                if solve(i + 1):
                    memo[idx] = True
                    return True
        memo[idx] = False
        return False

    return solve(0)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("leetcode", ["leet", "code"]) == True
    assert optimal_solution("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    print("Done.")
