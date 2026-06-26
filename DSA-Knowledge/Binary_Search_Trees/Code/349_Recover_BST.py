"""
LeetCode Link: https://leetcode.com/problems/recover-binary-search-tree/
Problem Name: Recover Binary Search Tree
Description: Recover a BST where exactly two nodes were swapped.

Folder: Binary_Search_Trees
File: 349_Recover_BST.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Inorder traversal. Keep track of current, previous, and violating elements.
# Swap values of the two elements violating order.
# Time Complexity: O(N)
# Space Complexity: O(H) recursion stack
def optimal_solution(root: TreeNode) -> TreeNode:
    first = None
    middle = None
    last = None
    prev = TreeNode(-float('inf'))
    
    def inorder(node):
        nonlocal first, middle, last, prev
        if not node:
            return
            
        inorder(node.left)
        
        # Check violation
        if node.val < prev.val:
            if not first:
                first = prev
                middle = node
            else:
                last = node
                
        prev = node
        inorder(node.right)

    inorder(root)
    
    if first and last:
        first.val, last.val = last.val, first.val
    elif first and middle:
        first.val, middle.val = middle.val, first.val
        
    return root

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    # Swapped 1 and 3 in standard BST [1, 2, 3]
    root = TreeNode(1)
    root.left = TreeNode(3, None, TreeNode(2))
    
    recovered = optimal_solution(root)
    assert recovered.val == 3
    assert recovered.left.val == 1
    print("Done.")
