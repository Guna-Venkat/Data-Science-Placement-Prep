"""
LeetCode Link: https://leetcode.com/problems/balanced-binary-tree/
Problem Name: Balanced Binary Tree
Description: Check if a binary tree is height-balanced (height difference of left and right subtrees <= 1).

Folder: Binary_Trees
File: 310_Check_for_balanced_binary_tree.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Bottom-up height check. Return -1 if unbalanced, otherwise return tree height.
# Time Complexity: O(N)
# Space Complexity: O(H)
def optimal_solution(root: TreeNode) -> bool:
    def check(node):
        if not node:
            return 0
        left = check(node.left)
        if left == -1: return -1
        right = check(node.right)
        if right == -1: return -1
        
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) != -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert optimal_solution(root) == True
    
    unbalanced = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert optimal_solution(unbalanced) == False
    print("Done.")
