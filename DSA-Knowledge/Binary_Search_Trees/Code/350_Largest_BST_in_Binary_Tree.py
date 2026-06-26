"""
LeetCode Link: https://www.geeksforgeeks.org/problems/largest-bst/1
Problem Name: Largest BST in Binary Tree
Description: Given a Binary Tree, find the size of the largest subtree which is a BST.

Folder: Binary_Search_Trees
File: 350_Largest_BST_in_Binary_Tree.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Postorder traversal. Return (is_bst, size, min_val, max_val) from child nodes.
# Time Complexity: O(N)
# Space Complexity: O(H)
def optimal_solution(root: TreeNode) -> int:
    def dfs(node):
        # returns: (is_bst, size, min_val, max_val)
        if not node:
            return True, 0, float('inf'), -float('inf')
            
        left_is_bst, left_size, left_min, left_max = dfs(node.left)
        right_is_bst, right_size, right_min, right_max = dfs(node.right)
        
        if left_is_bst and right_is_bst and left_max < node.val < right_min:
            curr_size = 1 + left_size + right_size
            curr_min = min(node.val, left_min)
            curr_max = max(node.val, right_max)
            return True, curr_size, curr_min, curr_max
            
        return False, max(left_size, right_size), -float('inf'), float('inf')

    return dfs(root)[1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(5)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(4) # invalid BST on right subtree
    
    # Left subtree is a BST of size 3 (nodes 1, 2, 3)
    assert optimal_solution(root) == 3
    print("Done.")
