"""
LeetCode Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
Problem Name: Lowest Common Ancestor of a Binary Tree
Description: Find the LCA of two nodes p and q in a binary tree.

Folder: Binary_Trees
File: 322_LCA_in_BT.py
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
def optimal_solution(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root == p or root == q:
        return root
        
    left = optimal_solution(root.left, p, q)
    right = optimal_solution(root.right, p, q)
    
    if left and right:
        return root
    return left or right

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    p = TreeNode(5)
    q = TreeNode(1)
    root = TreeNode(3, p, q)
    assert optimal_solution(root, p, q) == root
    print("Done.")
