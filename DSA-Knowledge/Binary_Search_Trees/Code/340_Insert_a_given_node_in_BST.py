"""
LeetCode Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/
Problem Name: Insert into a Binary Search Tree
Description: Insert a value into the BST and return the root of the modified BST.

Folder: Binary_Search_Trees
File: 340_Insert_a_given_Node_in_BST.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Move down the tree. If val < curr.val, go left; else go right.
# Insert at the first encountered None location.
# Time Complexity: O(H)
# Space Complexity: O(1)
def optimal_solution(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)
    curr = root
    while True:
        if val < curr.val:
            if curr.left is None:
                curr.left = TreeNode(val)
                break
            else:
                curr = curr.left
        else:
            if curr.right is None:
                curr.right = TreeNode(val)
                break
            else:
                curr = curr.right
    return root

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7)
    
    new_root = optimal_solution(root, 5)
    assert new_root.right.left.val == 5
    print("Done.")
