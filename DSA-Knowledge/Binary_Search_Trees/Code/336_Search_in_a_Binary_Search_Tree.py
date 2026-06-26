"""
LeetCode Link: https://leetcode.com/problems/search-in-a-binary-search-tree/
Problem Name: Search in a Binary Search Tree
Description: Find the node in the BST that the node's value equals val and return that subtree.

Folder: Binary_Search_Trees
File: 336_Search_in_a_Binary_Search_Tree.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: If val < root.val, search left; if val > root.val, search right.
# Time Complexity: O(H) where H is height of the tree.
# Space Complexity: O(1) iterative
def optimal_solution(root: TreeNode, val: int) -> TreeNode:
    curr = root
    while curr is not None and curr.val != val:
        if val < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    return curr

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    # Tree:
    #      4
    #     /     #    2   7
    #   /     #  1   3
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7)
    
    res = optimal_solution(root, 2)
    assert res is not None and res.val == 2
    assert res.left.val == 1
    
    res_none = optimal_solution(root, 5)
    assert res_none is None
    print("Done.")
