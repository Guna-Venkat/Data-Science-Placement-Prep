"""
LeetCode Link: https://leetcode.com/problems/partition-equal-subset-sum/
Problem Name: Partition Equal Subset Sum
Description: Check if array can be partitioned into two subsets with equal sum.

Folder: Dynamic_Programming
File: 417_Partition_equal_subset_sum.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * Sum/2)
# Space Complexity: O(Sum/2)
def optimal_solution(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    
    dp = [False] * (target + 1)
    dp[0] = True
    if nums[0] <= target:
        dp[nums[0]] = True
        
    for i in range(1, len(nums)):
        next_dp = [False] * (target + 1)
        next_dp[0] = True
        for t in range(1, target + 1):
            non_pick = dp[t]
            pick = dp[t - nums[i]] if t >= nums[i] else False
            next_dp[t] = pick or non_pick
        dp = next_dp
    return dp[target]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 5, 11, 5]) == True
    assert optimal_solution([1, 2, 3, 5]) == False
    print("Done.")
