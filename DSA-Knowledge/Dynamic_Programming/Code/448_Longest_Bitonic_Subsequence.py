"""
LeetCode Link: https://www.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1
Problem Name: Longest Bitonic Subsequence
Description: Longest bitonic subsequence (strictly increasing then strictly decreasing).

Folder: Dynamic_Programming
File: 448_Longest_Bitonic_Subsequence.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Find LIS from front (dp1) and LIS from back (dp2).
# Maximize (dp1[i] + dp2[i] - 1).
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(nums: list[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    dp1 = [1] * n # increasing
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp1[i] = max(dp1[i], dp1[j] + 1)
                
    dp2 = [1] * n # decreasing
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if nums[i] > nums[j]:
                dp2[i] = max(dp2[i], dp2[j] + 1)
                
    max_len = 0
    for i in range(n):
        if dp1[i] > 1 and dp2[i] > 1: # Strict bitonic requires both increasing and decreasing parts
            max_len = max(max_len, dp1[i] + dp2[i] - 1)
    # If no bitonic found, return max LIS (or 0 per GFG strict testcases)
    return max_len if max_len > 0 else max(max(dp1), max(dp2))

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 5, 3, 2]) == 5
    print("Done.")
