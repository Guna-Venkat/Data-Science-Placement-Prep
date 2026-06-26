"""
LeetCode Link: https://www.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1
Problem Name: Boundary Traversal of Binary Tree
Description: Return boundary elements of a binary tree in anti-clockwise order.

Folder: Binary_Trees
File: 315_Boundary_Traversal.py
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
# 1. Left boundary (excluding leaves).
# 2. Leaf nodes.
# 3. Right boundary in reverse (excluding leaves).
# Time Complexity: O(N)
# Space Complexity: O(H) stack depth
def is_leaf(node):
    return not node.left and not node.right

def add_left_boundary(root, res):
    curr = root.left
    while curr:
        if not is_leaf(curr):
            res.append(curr.val)
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right

def add_leaves(node, res):
    if not node:
        return
    if is_leaf(node):
        res.append(node.val)
        return
    add_leaves(node.left, res)
    add_leaves(node.right, res)

def add_right_boundary(root, res):
    curr = root.right
    temp = []
    while curr:
        if not is_leaf(curr):
            temp.append(curr.val)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    res.extend(temp[::-1])

def optimal_solution(root: TreeNode) -> list[int]:
    if not root:
        return []
    res = []
    if not is_leaf(root):
        res.append(root.val)
    add_left_boundary(root, res)
    add_leaves(root, res)
    add_right_boundary(root, res)
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3), TreeNode(4)))
    # root (1) -> left boundary (none) -> leaves (3, 4) -> right boundary (2)
    assert optimal_solution(root) == [1, 3, 4, 2]
    print("Done.")
