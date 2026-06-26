"""
LeetCode Link: https://leetcode.com/problems/combination-sum-ii/
Problem Name: Combination Sum II
Description: Find all unique combinations in candidates where elements sum to target.
Each candidate used once.

Folder: Recursion
File: 192_Combination_Sum_II.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Sort candidates. In loop, skip adjacent duplicates to prevent duplicate paths.
# Time Complexity: O(2^N * N)
# Space Complexity: O(N)
def optimal_solution(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    result = []
    
    def backtrack(idx, target, path):
        if target == 0:
            result.append(list(path))
            return
        if target < 0:
            return
            
        for i in range(idx, len(candidates)):
            # skip duplicate elements
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
                
            path.append(candidates[i])
            backtrack(i + 1, target - candidates[i], path)
            path.pop()

    backtrack(0, target, [])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    res = optimal_solution([10, 1, 2, 7, 6, 1, 5], 8)
    assert sorted(res) == sorted([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
    print("Done.")
