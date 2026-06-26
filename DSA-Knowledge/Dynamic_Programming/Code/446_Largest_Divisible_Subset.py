"""
LeetCode Link: https://leetcode.com/problems/largest-divisible-subset/
Problem Name: Largest Divisible Subset
Description: Find largest subset where every pair satisfies s[i] % s[j] == 0 or vice versa.

Folder: Dynamic_Programming
File: 446_Largest_Divisible_Subset.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Sort nums first. Standard LIS format where condition is nums[i] % nums[j] == 0.
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(nums: list[int]) -> list[int]:
    if not nums:
        return []
    nums.sort()
    n = len(nums)
    dp = [1] * n
    parent = list(range(n))
    max_len = 1
    last_idx = 0
    
    for i in range(n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
        if dp[i] > max_len:
            max_len = dp[i]
            last_idx = i
            
    res = []
    curr = last_idx
    while parent[curr] != curr:
        res.append(nums[curr])
        curr = parent[curr]
    res.append(nums[curr])
    return res[::-1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 3]) == [1, 2] or optimal_solution([1, 2, 3]) == [1, 3]
    print("Done.")
