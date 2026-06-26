"""
LeetCode Link: https://www.geeksforgeeks.org/problems/predecessor-and-successor/1
Problem Name: Inorder Predecessor and Successor
Description: Find the inorder predecessor and successor of a given key in BST.

Folder: Binary_Search_Trees
File: 346_Inorder_Successor_Predecessor_in_BST.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: 
# - Successor: Smallest value strictly greater than key. If curr.val > key, 
#   curr is potential successor, move to left child. Else move to right.
# - Predecessor: Largest value strictly less than key. If curr.val < key,
#   curr is potential predecessor, move to right child. Else move to left.
# Time Complexity: O(H)
# Space Complexity: O(1)
def find_pre_suc(root: TreeNode, key: int) -> tuple[int, int]:
    pre = -1
    suc = -1
    
    # Successor search
    curr = root
    while curr:
        if curr.val > key:
            suc = curr.val
            curr = curr.left
        else:
            curr = curr.right
            
    # Predecessor search
    curr = root
    while curr:
        if curr.val < key:
            pre = curr.val
            curr = curr.right
        else:
            curr = curr.left
            
    return pre, suc

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(8)
    root.left = TreeNode(4, TreeNode(2), TreeNode(6))
    root.right = TreeNode(12, TreeNode(10), TreeNode(14))
    
    pre, suc = find_pre_suc(root, 8)
    assert pre == 6 and suc == 10
    print("Done.")
