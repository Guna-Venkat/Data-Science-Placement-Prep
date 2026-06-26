"""
LeetCode Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
Problem Name: Binary Tree Inorder Traversal
Description: Recursive inorder traversal.

Folder: Binary_Trees
File: 301_Inorder_Traversal_of_Binary_Tree.py
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
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        res.append(node.val)
        inorder(node.right)
    inorder(root)
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert optimal_solution(root) == [1, 3, 2]
    print("Done.")
