"""
LeetCode Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Problem Name: Binary Tree Zigzag Level Order Traversal
Description: Level order traversal in spiral form.

Folder: Binary_Trees
File: 314_Zig_Zag_or_Spiral_Traversal.py
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
# Space Complexity: O(N)
def optimal_solution(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    result = []
    queue = [root]
    left_to_right = True
    while queue:
        level_size = len(queue)
        level = [0] * level_size
        for i in range(level_size):
            node = queue.pop(0)
            idx = i if left_to_right else (level_size - 1 - i)
            level[idx] = node.val
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
        left_to_right = not left_to_right
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert optimal_solution(root) == [[3], [20, 9], [15, 7]]
    print("Done.")
