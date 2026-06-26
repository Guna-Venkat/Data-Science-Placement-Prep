"""
LeetCode Link: https://www.geeksforgeeks.org/problems/printing-longest-increasing-subsequence/1
Problem Name: Print Longest Increasing Subsequence
Description: Return actual LIS path.

Folder: Dynamic_Programming
File: 444_Print_Longest_Increasing_Subsequence.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(nums: list[int]) -> list[int]:
    n = len(nums)
    dp = [1] * n
    hash_prev = list(range(n))
    max_len = 1
    last_idx = 0
    
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                hash_prev[i] = j
        if dp[i] > max_len:
            max_len = dp[i]
            last_idx = i
            
    # Backtrack
    lis = []
    curr = last_idx
    while hash_prev[curr] != curr:
        lis.append(nums[curr])
        curr = hash_prev[curr]
    lis.append(nums[curr])
    return lis[::-1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([10, 9, 2, 5, 3, 7, 101, 18]) == [2, 3, 7, 18] or optimal_solution([10, 9, 2, 5, 3, 7, 101, 18]) == [2, 5, 7, 18]
    print("Done.")
