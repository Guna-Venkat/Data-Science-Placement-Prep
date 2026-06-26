"""
LeetCode Link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
Problem Name: Vertical Order Traversal of a Binary Tree
Description: Vertical level order traversal (sorted by column, level, then value).

Folder: Binary_Trees
File: 316_Vertical_Order_Traversal.py
"""

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep column and row indices. Sort values of nodes at same coordinates.
# Time Complexity: O(N log N)
# Space Complexity: O(N)
def optimal_solution(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    nodes = collections.defaultdict(list)
    # BFS
    queue = [(root, 0, 0)] # node, col, row
    while queue:
        node, col, row = queue.pop(0)
        nodes[col].append((row, node.val))
        if node.left: queue.append((node.left, col - 1, row + 1))
        if node.right: queue.append((node.right, col + 1, row + 1))
        
    result = []
    for col in sorted(nodes.keys()):
        # Sort by row index first, then by node value
        column_nodes = sorted(nodes[col], key=lambda x: (x[0], x[1]))
        result.append([val for row, val in column_nodes])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert optimal_solution(root) == [[9], [3, 15], [20], [7]]
    print("Done.")
