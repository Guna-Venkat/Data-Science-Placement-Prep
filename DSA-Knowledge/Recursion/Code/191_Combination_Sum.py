"""
LeetCode Link: https://leetcode.com/problems/combination-sum/
Problem Name: Combination Sum
Description: Find all unique combinations of candidates where candidates sum to target.
Repeated selection allowed.

Folder: Recursion
File: 191_Combination_Sum.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Backtracking with reuse. Keep index pointer `idx` same for recursive reuse.
# Time Complexity: O(2^T * K) where T is target / min candidate
# Space Complexity: O(T) stack depth
def optimal_solution(candidates: list[int], target: int) -> list[list[int]]:
    result = []
    
    def backtrack(idx, target, path):
        if target == 0:
            result.append(list(path))
            return
        if idx == len(candidates) or target < 0:
            return
            
        # Pick current element
        path.append(candidates[idx])
        backtrack(idx, target - candidates[idx], path)
        path.pop()
        
        # Skip current element
        backtrack(idx + 1, target, path)

    backtrack(0, target, [])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    res = optimal_solution([2, 3, 6, 7], 7)
    assert sorted(res) == sorted([[2, 2, 3], [7]])
    print("Done.")
