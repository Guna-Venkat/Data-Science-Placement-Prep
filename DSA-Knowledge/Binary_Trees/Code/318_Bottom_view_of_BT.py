"""
LeetCode Link: https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1
Problem Name: Bottom View of Binary Tree
Description: Print bottom view of a binary tree.

Folder: Binary_Trees
File: 318_Bottom_view_of_BT.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep track of horizontal distance. Record last node visited at each distance using BFS.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(root: TreeNode) -> list[int]:
    if not root:
        return []
    bottom_map = {} # col -> val
    queue = [(root, 0)]
    while queue:
        node, col = queue.pop(0)
        bottom_map[col] = node.val
        if node.left: queue.append((node.left, col - 1))
        if node.right: queue.append((node.right, col + 1))
        
    return [bottom_map[col] for col in sorted(bottom_map.keys())]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(6)))
    assert optimal_solution(root) == [2, 5, 3, 6]
    print("Done.")
