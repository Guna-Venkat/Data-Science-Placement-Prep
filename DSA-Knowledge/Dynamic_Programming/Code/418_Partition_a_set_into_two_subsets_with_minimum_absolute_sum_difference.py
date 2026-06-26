"""
LeetCode Link: https://leetcode.com/problems/last-stone-weight-ii/
Problem Name: Partition set with minimum absolute sum difference
Description: Partition set into two subsets with minimum absolute sum difference.

Folder: Dynamic_Programming
File: 418_Partition_a_set_into_two_subsets_with_minimum_absolute_sum_difference.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * TotalSum)
# Space Complexity: O(TotalSum)
def optimal_solution(nums: list[int]) -> int:
    total_sum = sum(nums)
    target = total_sum // 2
    
    dp = [False] * (target + 1)
    dp[0] = True
    if nums[0] <= target:
        dp[nums[0]] = True
        
    for i in range(1, len(nums)):
        for t in range(target, nums[i] - 1, -1):
            dp[t] = dp[t] or dp[t - nums[i]]
            
    # Find maximum sum s1 <= target that is achievable
    s1 = 0
    for t in range(target, -1, -1):
        if dp[t]:
            s1 = t
            break
            
    s2 = total_sum - s1
    return abs(s1 - s2)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 6, 11, 5]) == 1 # subsets {1, 5, 6}=12 and {11}=11
    print("Done.")
