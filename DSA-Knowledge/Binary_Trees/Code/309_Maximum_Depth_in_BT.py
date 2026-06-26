"""
LeetCode Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Problem Name: Maximum Depth of Binary Tree
Description: Find the maximum depth of a binary tree.

Folder: Binary_Trees
File: 309_Maximum_Depth_in_BT.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(H)
def optimal_solution(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(optimal_solution(root.left), optimal_solution(root.right))

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert optimal_solution(root) == 3
    print("Done.")
