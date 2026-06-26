"""
LeetCode Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
Problem Name: Iterative Postorder Traversal using 1 Stack
Description: Postorder traversal using a single stack.

Folder: Binary_Trees
File: 307_Post_order_Traversal_of_Binary_Tree_using_1_stack.py
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
# Space Complexity: O(H)
def optimal_solution(root: TreeNode) -> list[int]:
    res = []
    stack = []
    curr = root
    last_visited = None
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        peek_node = stack[-1]
        if peek_node.right and last_visited != peek_node.right:
            curr = peek_node.right
        else:
            res.append(peek_node.val)
            last_visited = stack.pop()
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert optimal_solution(root) == [3, 2, 1]
    print("Done.")
