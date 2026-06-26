"""
LeetCode Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
Problem Name: Iterative Preorder Traversal
Description: Preorder traversal using stack.

Folder: Binary_Trees
File: 304_Iterative_Preorder_Traversal_of_Binary_Tree.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(H) stack space
def optimal_solution(root: TreeNode) -> list[int]:
    if not root:
        return []
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert optimal_solution(root) == [1, 2, 3]
    print("Done.")
