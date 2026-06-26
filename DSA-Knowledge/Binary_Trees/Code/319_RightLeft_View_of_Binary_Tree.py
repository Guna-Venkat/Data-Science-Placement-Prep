"""
LeetCode Link: https://leetcode.com/problems/binary-tree-right-side-view/
Problem Name: Right and Left View of Binary Tree
Description: Return right and left views of binary tree.

Folder: Binary_Trees
File: 319_RightLeft_View_of_Binary_Tree.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Recursive DFS keeping track of level. First node visited at that level in Root-Right-Left
# is right view; Root-Left-Right is left view.
# Time Complexity: O(N)
# Space Complexity: O(H)
def right_view(root: TreeNode) -> list[int]:
    res = []
    def dfs(node, level):
        if not node:
            return
        if level == len(res):
            res.append(node.val)
        dfs(node.right, level + 1)
        dfs(node.left, level + 1)
    dfs(root, 0)
    return res

def left_view(root: TreeNode) -> list[int]:
    res = []
    def dfs(node, level):
        if not node:
            return
        if level == len(res):
            res.append(node.val)
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    dfs(root, 0)
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert right_view(root) == [1, 3, 4]
    assert left_view(root) == [1, 2, 5]
    print("Done.")
