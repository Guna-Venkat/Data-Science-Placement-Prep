"""
LeetCode Link: https://leetcode.com/problems/palindrome-partitioning-ii/
Problem Name: Palindrome Partitioning II
Description: Find minimal cuts needed for palindrome partitioning of a string.

Folder: Dynamic_Programming
File: 455_Palindrome_partitioning_II.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
def optimal_solution(s: str) -> int:
    n = len(s)
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
        is_pal[i][i] = True
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if length == 2:
                is_pal[i][j] = (s[i] == s[j])
            else:
                is_pal[i][j] = (s[i] == s[j] and is_pal[i+1][j-1])
                
    cuts = [0] * n
    for i in range(n):
        if is_pal[0][i]:
            cuts[i] = 0
        else:
            min_cut = float('inf')
            for j in range(i):
                if is_pal[j + 1][i]:
                    min_cut = min(min_cut, cuts[j] + 1)
            cuts[i] = min_cut
    return cuts[-1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("aab") == 1
    print("Done.")
