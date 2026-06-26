"""
LeetCode Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
Problem Name: Binary Tree Postorder Traversal
Description: Recursive postorder traversal.

Folder: Binary_Trees
File: 302_Postorder_Traversal.py
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
    def postorder(node):
        if not node:
            return
        postorder(node.left)
        postorder(node.right)
        res.append(node.val)
    postorder(root)
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert optimal_solution(root) == [3, 2, 1]
    print("Done.")
