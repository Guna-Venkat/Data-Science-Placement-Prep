"""
LeetCode Link: https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555635/1
Problem Name: Subset Sum Equal to Target
Description: Check if subset exists with sum equal to target.

Folder: Dynamic_Programming
File: 416_Subset_sum_equal_to_target_DP_14.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * Target)
# Space Complexity: O(Target)
def optimal_solution(arr: list[int], target: int) -> bool:
    dp = [False] * (target + 1)
    dp[0] = True
    if arr[0] <= target:
        dp[arr[0]] = True
        
    for i in range(1, len(arr)):
        next_dp = [False] * (target + 1)
        next_dp[0] = True
        for t in range(1, target + 1):
            non_pick = dp[t]
            pick = dp[t - arr[i]] if t >= arr[i] else False
            next_dp[t] = pick or non_pick
        dp = next_dp
    return dp[target]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 3, 4], 6) == True
    assert optimal_solution([1, 2, 3, 4], 11) == False
    print("Done.")
