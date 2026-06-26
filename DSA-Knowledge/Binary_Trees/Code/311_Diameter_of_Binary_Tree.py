"""
LeetCode Link: https://leetcode.com/problems/diameter-of-binary-tree/
Problem Name: Diameter of Binary Tree
Description: Find the length of the longest path between any two nodes.

Folder: Binary_Trees
File: 311_Diameter_of_Binary_Tree.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Return height, update global max diameter with (left_height + right_height).
# Time Complexity: O(N)
# Space Complexity: O(H)
def optimal_solution(root: TreeNode) -> int:
    diameter = 0
    
    def dfs(node):
        nonlocal diameter
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)

    dfs(root)
    return diameter

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert optimal_solution(root) == 3
    print("Done.")
