"""
LeetCode Link: https://leetcode.com/problems/target-sum/
Problem Name: Target Sum
Description: Assign '+' and '-' to elements to sum to target.

Folder: Dynamic_Programming
File: 423_Target_sum.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Equivalent to Count Partitions with Given Difference target = (sum + diff) / 2.
# Time Complexity: O(N * Target)
# Space Complexity: O(Target)
def optimal_solution(nums: list[int], target: int) -> int:
    total = sum(nums)
    if (total + target) % 2 != 0 or total < abs(target):
        return 0
    t = (total + target) // 2
    
    dp = [0] * (t + 1)
    dp[0] = 1
    for num in nums:
        for val in range(t, num - 1, -1):
            dp[val] += dp[val - num]
    return dp[t]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 1, 1, 1, 1], 3) == 5
    print("Done.")
