"""
LeetCode Link: https://www.geeksforgeeks.org/problems/introduction-to-trees/1
Problem Name: Introduction to Trees
Description: Given level i of a binary tree, find the maximum number of nodes possible at that level.

Folder: Binary_Trees
File: 297_Introduction_to_Trees.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Number of nodes at level i is 2^(i-1) if level is 1-indexed.
# Time Complexity: O(1)
# Space Complexity: O(1)
def optimal_solution(i: int) -> int:
    if i <= 0:
        return 0
    return 2 ** (i - 1)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(5) == 16
    assert optimal_solution(1) == 1
    print("Done.")
