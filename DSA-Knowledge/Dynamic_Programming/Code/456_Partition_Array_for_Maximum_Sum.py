"""
LeetCode Link: https://leetcode.com/problems/partition-array-for-maximum-sum/
Problem Name: Partition Array for Maximum Sum
Description: Partition array into subarrays of at most length k. Maximize sum of elements.

Folder: Dynamic_Programming
File: 456_Partition_Array_for_Maximum_Sum.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * K)
# Space Complexity: O(N)
def optimal_solution(arr: list[int], k: int) -> int:
    n = len(arr)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        curr_max = 0
        for j in range(1, min(i, k) + 1):
            curr_max = max(curr_max, arr[i - j])
            dp[i] = max(dp[i], dp[i - j] + curr_max * j)
            
    return dp[n]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 15, 7, 9, 2, 5, 10], 3) == 84
    print("Done.")
