"""
LeetCode Link: https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1
Problem Name: Count Subsets with Sum K
Description: Count number of subsets that sum to K.

Folder: Dynamic_Programming
File: 419_Count_subsets_with_sum_K.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * K)
# Space Complexity: O(K)
def optimal_solution(arr: list[int], k: int) -> int:
    dp = [0] * (k + 1)
    dp[0] = 1
    
    for num in arr:
        for t in range(k, num - 1, -1):
            dp[t] += dp[t - num]
    return dp[k]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 2, 3], 3) == 3
    print("Done.")
