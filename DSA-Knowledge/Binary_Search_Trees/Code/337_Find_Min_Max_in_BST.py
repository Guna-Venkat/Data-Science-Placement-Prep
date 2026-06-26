"""
LeetCode Link: https://www.geeksforgeeks.org/problems/minimum-element-in-bst/1
Problem Name: Minimum and Maximum in BST
Description: Find the minimum and maximum elements in a BST.

Folder: Binary_Search_Trees
File: 337_Find_Min_Max_in_BST.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep moving left to find the minimum; keep moving right to find the maximum.
# Time Complexity: O(H)
# Space Complexity: O(1)
def find_min(root: TreeNode) -> int:
    if root is None:
        return -1
    curr = root
    while curr.left is not None:
        curr = curr.left
    return curr.val

def find_max(root: TreeNode) -> int:
    if root is None:
        return -1
    curr = root
    while curr.right is not None:
        curr = curr.right
    return curr.val

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(1), TreeNode(4))
    root.right = TreeNode(8, TreeNode(6), TreeNode(9))
    
    assert find_min(root) == 1
    assert find_max(root) == 9
    print("Done.")
