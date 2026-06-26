"""
LeetCode Link: https://www.codingninjas.com/studio/problems/tree-traversals_981269
Problem Name: Preorder, Inorder, and Postorder in One Traversal
Description: Return pre, in, and post order traversals of a tree in a single DFS traversal.

Folder: Binary_Trees
File: 299_Pre_Post_Inorder_in_one_traversal.py
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
# Space Complexity: O(H) recursion stack
def optimal_solution(root: TreeNode) -> tuple[list[int], list[int], list[int]]:
    pre_order = []
    in_order = []
    post_order = []
    
    def dfs(node):
        if not node:
            return
        pre_order.append(node.val)
        dfs(node.left)
        in_order.append(node.val)
        dfs(node.right)
        post_order.append(node.val)

    dfs(root)
    return pre_order, in_order, post_order

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    pre, ino, post = optimal_solution(root)
    assert pre == [1, 2, 3]
    assert ino == [2, 1, 3]
    assert post == [2, 3, 1]
    print("Done.")
