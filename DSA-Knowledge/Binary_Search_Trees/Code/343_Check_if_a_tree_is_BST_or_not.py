"""
LeetCode Link: https://leetcode.com/problems/validate-binary-search-tree/
Problem Name: Validate Binary Search Tree
Description: Check if a binary tree is a valid BST.

Folder: Binary_Search_Trees
File: 343_Check_if_a_tree_is_BST_or_not.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Define a valid range [min_val, max_val] for each node.
# For left child, update max_val to node.val. For right child, update min_val to node.val.
# Time Complexity: O(N)
# Space Complexity: O(H) stack
def optimal_solution(root: TreeNode) -> bool:
    def validate(node, min_val, max_val):
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False
        return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

    return validate(root, -float('inf'), float('inf'))

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    assert optimal_solution(root) == True
    
    invalid = TreeNode(5)
    invalid.left = TreeNode(1)
    invalid.right = TreeNode(4, TreeNode(3), TreeNode(6))
    assert optimal_solution(invalid) == False
    print("Done.")
