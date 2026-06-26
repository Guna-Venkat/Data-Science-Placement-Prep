"""
LeetCode Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
Problem Name: Binary Tree Preorder Traversal
Description: Recursive preorder traversal.

Folder: Binary_Trees
File: 300_Preorder_Traversal.py
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
def optimal_solution(root: TreeNode) -> list[int]:
    res = []
    def preorder(node):
        if not node:
            return
        res.append(node.val)
        preorder(node.left)
        preorder(node.right)
    preorder(root)
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert optimal_solution(root) == [1, 2, 3]
    print("Done.")
