"""
LeetCode Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
Problem Name: Iterative Postorder Traversal using 2 Stacks
Description: Postorder traversal using two stacks.

Folder: Binary_Trees
File: 306_Post_order_Traversal_of_Binary_Tree_using_2_stack.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Push root to stack1. Pop stack1, push to stack2.
# Push left child, then right child to stack1.
# Pop all from stack2.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(root: TreeNode) -> list[int]:
    if not root:
        return []
    res = []
    s1 = [root]
    s2 = []
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left: s1.append(node.left)
        if node.right: s1.append(node.right)
    while s2:
        res.append(s2.pop().val)
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert optimal_solution(root) == [3, 2, 1]
    print("Done.")
