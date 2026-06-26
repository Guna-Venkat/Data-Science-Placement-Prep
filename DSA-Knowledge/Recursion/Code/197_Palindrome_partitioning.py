"""
LeetCode Link: https://leetcode.com/problems/palindrome-partitioning/
Problem Name: Palindrome Partitioning
Description: Partition a string such that every substring of the partition is a palindrome.

Folder: Recursion
File: 197_Palindrome_partitioning.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Try cutting string at indices. If prefix is palindrome, recursively partition remaining.
# Time Complexity: O(2^N * N)
# Space Complexity: O(N)
def optimal_solution(s: str) -> list[list[str]]:
    result = []
    
    def is_palindrome(val):
        return val == val[::-1]

    def backtrack(idx, path):
        if idx == len(s):
            result.append(list(path))
            return
            
        for i in range(idx, len(s)):
            part = s[idx:i+1]
            if is_palindrome(part):
                path.append(part)
                backtrack(i + 1, path)
                path.pop()

    backtrack(0, [])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    res = optimal_solution("aab")
    assert sorted(res) == sorted([["a", "a", "b"], ["aa", "b"]])
    print("Done.")
