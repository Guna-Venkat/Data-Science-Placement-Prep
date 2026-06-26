"""
LeetCode Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Problem Name: Flatten Binary Tree to Linked List
Description: Flatten a binary tree to a singly linked list in-place.

Folder: Binary_Trees
File: 334_Flatten_Binary_Tree_to_Linked_List.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Traverse reverse postorder (Right, Left, Root) and track prev.
# Time Complexity: O(N)
# Space Complexity: O(H) recursion stack
def optimal_solution(root: TreeNode):
    prev = None
    
    def dfs(node):
        nonlocal prev
        if not node:
            return
        dfs(node.right)
        dfs(node.left)
        node.right = prev
        node.left = None
        prev = node

    dfs(root)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
    optimal_solution(root)
    assert root.val == 1
    assert root.right.val == 2
    assert root.right.right.val == 3
    print("Done.")
