"""
LeetCode Link: https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1
Problem Name: Matrix Chain Multiplication (MCM)
Description: Find minimal cost to multiply matrices.

Folder: Dynamic_Programming
File: 450_Matrix_chain_multiplication.py
"""

# ============================================
# OPTIMAL APPROACH (Memoized Top-Down)
# ============================================
# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
def optimal_solution(arr: list[int]) -> int:
    n = len(arr)
    memo = {}
    
    def solve(i, j):
        if i == j:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
            
        min_cost = float('inf')
        for k in range(i, j):
            cost = solve(i, k) + solve(k + 1, j) + arr[i-1] * arr[k] * arr[j]
            min_cost = min(min_cost, cost)
            
        memo[(i, j)] = min_cost
        return min_cost

    return solve(1, n - 1)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([40, 20, 30, 10, 30]) == 26000
    print("Done.")
