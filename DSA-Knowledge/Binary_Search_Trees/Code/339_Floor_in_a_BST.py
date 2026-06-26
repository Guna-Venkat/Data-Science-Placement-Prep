"""
LeetCode Link: https://www.geeksforgeeks.org/problems/floor-in-bst/1
Problem Name: Floor in BST
Description: Find floor of X (largest node value <= X) in a BST.

Folder: Binary_Search_Trees
File: 339_Floor_in_a_BST.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: If root.val <= X, root is a potential floor. Move to right child.
# If root.val > X, move to left child.
# Time Complexity: O(H)
# Space Complexity: O(1)
def find_floor(root: TreeNode, x: int) -> int:
    floor = -1
    curr = root
    while curr:
        if curr.val == x:
            return curr.val
        if curr.val < x:
            floor = curr.val
            curr = curr.right
        else:
            curr = curr.left
    return floor

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(8)
    root.left = TreeNode(4, TreeNode(2), TreeNode(6))
    root.right = TreeNode(12, TreeNode(10), TreeNode(14))
    
    assert find_floor(root, 11) == 10
    assert find_floor(root, 3) == 2
    assert find_floor(root, 1) == -1
    print("Done.")
