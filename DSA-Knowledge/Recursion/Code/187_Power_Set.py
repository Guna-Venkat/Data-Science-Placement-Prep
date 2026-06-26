"""
LeetCode Link: https://leetcode.com/problems/subsets/
Problem Name: Subsets (Power Set)
Description: Generate all subsets of a set of unique elements.

Folder: Recursion
File: 187_Power_Set.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Recursive backtracking with pick/non-pick choices.
# Time Complexity: O(2^N * N)
# Space Complexity: O(N) recursion stack
def optimal_solution(nums: list[int]) -> list[list[int]]:
    result = []
    
    def backtrack(idx, path):
        if idx == len(nums):
            result.append(path[:])
            return
            
        # Don't pick
        backtrack(idx + 1, path)
        # Pick
        path.append(nums[idx])
        backtrack(idx + 1, path)
        path.pop()

    backtrack(0, [])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    res = optimal_solution([1, 2])
    assert sorted(res) == sorted([[], [1], [2], [1, 2]])
    print("Done.")
