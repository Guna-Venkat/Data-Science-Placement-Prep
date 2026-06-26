"""
LeetCode Link: https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1
Problem Name: Count Subsequences with Sum K
Description: Find total subsequences whose sum equals K.

Folder: Recursion
File: 189_Count_all_subsequences_with_sum_K.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Recursion with pick/non-pick. Return count from sub-calls.
# Time Complexity: O(2^N)
# Space Complexity: O(N) recursion stack
def optimal_solution(arr: list[int], k: int) -> int:
    def solve(idx, target):
        if target == 0:
            return 1
        if idx == len(arr) or target < 0:
            return 0
            
        # pick + non-pick
        pick = solve(idx + 1, target - arr[idx])
        non_pick = solve(idx + 1, target)
        return pick + non_pick

    return solve(0, k)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 1], 2) == 2 # [1, 1] and [2]
    print("Done.")
