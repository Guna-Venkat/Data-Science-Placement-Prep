"""
LeetCode Link: https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1
Problem Name: Top View of Binary Tree
Description: Print top view of a binary tree.

Folder: Binary_Trees
File: 317_Top_View_of_BT.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep track of horizontal distance. Record first node visited at each distance using BFS.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(root: TreeNode) -> list[int]:
    if not root:
        return []
    top_map = {} # col -> val
    # queue contains (node, col)
    queue = [(root, 0)]
    while queue:
        node, col = queue.pop(0)
        if col not in top_map:
            top_map[col] = node.val
        if node.left: queue.append((node.left, col - 1))
        if node.right: queue.append((node.right, col + 1))
        
    return [top_map[col] for col in sorted(top_map.keys())]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(6)))
    assert optimal_solution(root) == [2, 1, 3, 6]
    print("Done.")
