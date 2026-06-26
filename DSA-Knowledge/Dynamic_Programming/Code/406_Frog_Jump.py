"""
LeetCode Link: https://www.codingninjas.com/studio/problems/frog-jump_3621012
Problem Name: Frog Jump
Description: Find minimum energy lost by a frog jumping 1 or 2 steps.

Folder: Dynamic_Programming
File: 406_Frog_Jump.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(heights: list[int]) -> int:
    n = len(heights)
    if n <= 1:
        return 0
    prev2, prev = 0, abs(heights[1] - heights[0])
    for i in range(2, n):
        jump1 = prev + abs(heights[i] - heights[i-1])
        jump2 = prev2 + abs(heights[i] - heights[i-2])
        curr = min(jump1, jump2)
        prev2 = prev
        prev = curr
    return prev

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([10, 20, 30, 10]) == 20
    print("Done.")
