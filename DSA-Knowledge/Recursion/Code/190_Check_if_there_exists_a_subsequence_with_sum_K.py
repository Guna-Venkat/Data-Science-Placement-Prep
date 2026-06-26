"""
LeetCode Link: https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555635/1
Problem Name: Subset Sum Problem
Description: Check if there exists a subsequence whose sum equals K.

Folder: Recursion
File: 190_Check_if_there_exists_a_subsequence_with_sum_K.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Base cases check. Short circuit evaluations (OR conditions).
# Time Complexity: O(2^N)
# Space Complexity: O(N) recursion stack
def optimal_solution(arr: list[int], k: int) -> bool:
    def solve(idx, target):
        if target == 0:
            return True
        if idx == len(arr) or target < 0:
            return False
            
        # Pick or Don't pick
        return solve(idx + 1, target - arr[idx]) or solve(idx + 1, target)

    return solve(0, k)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 3], 5) == True
    assert optimal_solution([1, 2, 3], 7) == False
    print("Done.")
