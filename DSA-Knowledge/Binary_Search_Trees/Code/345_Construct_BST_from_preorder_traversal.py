"""
LeetCode Link: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
Problem Name: Construct BST from Preorder Traversal
Description: Construct a BST from its preorder traversal array.

Folder: Binary_Search_Trees
File: 345_Construct_BST_from_preorder_traversal.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Move index pointers sequentially using an upper bound tracker.
# Time Complexity: O(N)
# Space Complexity: O(H) recursion stack
def optimal_solution(preorder: list[int]) -> TreeNode:
    idx = 0
    
    def build(upper_bound):
        nonlocal idx
        if idx >= len(preorder) or preorder[idx] > upper_bound:
            return None
            
        root_val = preorder[idx]
        root = TreeNode(root_val)
        idx += 1
        
        root.left = build(root_val)
        root.right = build(upper_bound)
        return root

    return build(float('inf'))

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    res = optimal_solution([8, 5, 1, 7, 10, 12])
    assert res.val == 8
    assert res.left.val == 5
    assert res.left.right.val == 7
    print("Done.")
