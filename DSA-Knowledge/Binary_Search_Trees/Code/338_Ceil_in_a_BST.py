"""
LeetCode Link: https://www.geeksforgeeks.org/problems/implementing-ceil-in-bst/1
Problem Name: Ceil in BST
Description: Find ceil of X (smallest node value >= X) in a BST.

Folder: Binary_Search_Trees
File: 338_Ceil_in_a_BST.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: If root.val >= X, root is a potential ceil. Move to left child.
# If root.val < X, move to right child.
# Time Complexity: O(H)
# Space Complexity: O(1)
def find_ceil(root: TreeNode, x: int) -> int:
    ceil = -1
    curr = root
    while curr:
        if curr.val == x:
            return curr.val
        if curr.val > x:
            ceil = curr.val
            curr = curr.left
        else:
            curr = curr.right
    return ceil

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(8)
    root.left = TreeNode(4, TreeNode(2), TreeNode(6))
    root.right = TreeNode(12, TreeNode(10), TreeNode(14))
    
    assert find_ceil(root, 11) == 12
    assert find_ceil(root, 3) == 4
    assert find_ceil(root, 15) == -1
    print("Done.")
