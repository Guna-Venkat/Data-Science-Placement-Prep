"""
LeetCode Link: https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1
Problem Name: Matrix Chain Multiplication (Bottom-Up)
Description: Tabulation approach of MCM.

Folder: Dynamic_Programming
File: 451_Matrix_Chain_Multiplication_Bottom_UpDP_49.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
def optimal_solution(arr: list[int]) -> int:
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    
    # l is chain length
    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j]
                dp[i][j] = min(dp[i][j], cost)
                
    return dp[1][n - 1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([40, 20, 30, 10, 30]) == 26000
    print("Done.")
