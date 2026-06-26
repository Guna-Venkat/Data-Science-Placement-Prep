"""
LeetCode Link: https://leetcode.com/problems/subsets/
Problem Name: Subsequences Theory
Description: Explain and demonstrate picking/non-picking recursion patterns.

Folder: Recursion
File: 188_Learn_All_Patterns_of_Subsequences_Theory.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(2^N)
# Space Complexity: O(N) recursion stack
def optimal_solution(arr: list[int]) -> list[list[int]]:
    subsequences = []
    
    def dfs(idx, curr):
        if idx == len(arr):
            subsequences.append(list(curr))
            return
            
        # Pick
        curr.append(arr[idx])
        dfs(idx + 1, curr)
        curr.pop()
        
        # Don't pick
        dfs(idx + 1, curr)

    dfs(0, [])
    return subsequences

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert len(optimal_solution([1, 2, 3])) == 8
    print("Done.")
