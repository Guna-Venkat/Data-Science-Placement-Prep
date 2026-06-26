"""
LeetCode Link: https://leetcode.com/problems/powx-n/
Problem Name: Pow(x, n)
Description: Compute x raised to the power n.

Folder: Recursion
File: 181_Powx_n.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary Exponentiation. Compute x^(n/2) and multiply.
# Time Complexity: O(log n)
# Space Complexity: O(log n) recursion stack
def optimal_solution(x: float, n: int) -> float:
    def helper(base, exp):
        if exp == 0:
            return 1.0
        half = helper(base, exp // 2)
        if exp % 2 == 0:
            return half * half
        else:
            return half * half * base

    if n < 0:
        return 1.0 / helper(x, -n)
    return helper(x, n)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert abs(optimal_solution(2.0, 10) - 1024.0) < 1e-9
    assert abs(optimal_solution(2.1, 3) - 9.261) < 1e-9
    assert abs(optimal_solution(2.0, -2) - 0.25) < 1e-9
    print("Done.")
