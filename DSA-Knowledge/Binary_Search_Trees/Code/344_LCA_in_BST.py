"""
LeetCode Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Problem Name: Lowest Common Ancestor of a Binary Search Tree
Description: Find the LCA of two given nodes in the BST.

Folder: Binary_Search_Trees
File: 344_LCA_in_BST.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Since it is a BST, if p and q are both smaller than root, LCA is in left subtree.
# If both are larger, LCA is in right subtree. Otherwise, root itself is the split point (LCA).
# Time Complexity: O(H)
# Space Complexity: O(1) iterative
def optimal_solution(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    curr = root
    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr
    return None

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    p = TreeNode(2)
    q = TreeNode(8)
    root = TreeNode(6)
    root.left = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
    root.right = TreeNode(8, TreeNode(7), TreeNode(9))
    
    lca = optimal_solution(root, root.left, root.right)
    assert lca.val == 6
    print("Done.")
