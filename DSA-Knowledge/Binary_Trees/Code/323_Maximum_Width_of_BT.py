"""
LeetCode Link: https://leetcode.com/problems/maximum-width-of-binary-tree/
Problem Name: Maximum Width of Binary Tree
Description: Find the maximum width of a binary tree. Width is number of nodes in level between end nodes (including nulls).

Folder: Binary_Trees
File: 323_Maximum_Width_of_BT.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Assign 0-based index to each node. For node at idx: left child is 2*idx, right is 2*idx + 1.
# Width of level is (last_idx - first_idx + 1).
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(root: TreeNode) -> int:
    if not root:
        return 0
    max_width = 0
    # queue holds (node, idx)
    queue = [(root, 0)]
    while queue:
        level_size = len(queue)
        min_idx = queue[0][1]
        first_idx = 0
        last_idx = 0
        for i in range(level_size):
            node, idx = queue.pop(0)
            curr_idx = idx - min_idx # prevent integer overflow
            if i == 0: first_idx = curr_idx
            if i == level_size - 1: last_idx = curr_idx
            if node.left: queue.append((node.left, 2 * curr_idx))
            if node.right: queue.append((node.right, 2 * curr_idx + 1))
        max_width = max(max_width, last_idx - first_idx + 1)
    return max_width

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
    assert optimal_solution(root) == 4
    print("Done.")
