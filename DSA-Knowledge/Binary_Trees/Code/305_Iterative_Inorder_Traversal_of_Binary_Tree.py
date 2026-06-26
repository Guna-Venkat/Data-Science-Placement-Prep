"""
LeetCode Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
Problem Name: Iterative Inorder Traversal
Description: Inorder traversal using stack.

Folder: Binary_Trees
File: 305_Iterative_Inorder_Traversal_of_Binary_Tree.py
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
    res = []
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert optimal_solution(root) == [1, 3, 2]
    print("Done.")
