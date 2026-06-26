"""
LeetCode Link: https://leetcode.com/problems/fibonacci-number/
Problem Name: Introduction to DP (Fibonacci)
Description: Compute Fibonacci number using memoization and space-optimized tabulation.

Folder: Dynamic_Programming
File: 404_Introduction_to_DP.py
"""

# ============================================
# OPTIMAL APPROACH (Space Optimized)
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(n: int) -> int:
    if n <= 1:
        return n
    prev2, prev = 0, 1
    for _ in range(2, n + 1):
        curr = prev + prev2
        prev2 = prev
        prev = curr
    return prev

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(5) == 5
    assert optimal_solution(10) == 55
    print("Done.")
