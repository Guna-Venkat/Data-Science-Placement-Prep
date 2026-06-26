"""
LeetCode Link: https://leetcode.com/problems/climbing-stairs/
Problem Name: Climbing Stairs
Description: Find the number of distinct ways to climb to the top of n stairs.

Folder: Dynamic_Programming
File: 405_Climbing_Stairs.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(n: int) -> int:
    if n <= 2:
        return n
    prev2, prev = 1, 2
    for _ in range(3, n + 1):
        curr = prev + prev2
        prev2 = prev
        prev = curr
    return prev

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(3) == 3
    assert optimal_solution(5) == 8
    print("Done.")
