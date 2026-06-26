"""
LeetCode Link: https://leetcode.com/problems/count-complete-tree-nodes/
Problem Name: Count Complete Tree Nodes
Description: Count nodes in a complete binary tree in less than O(N) time.

Folder: Binary_Trees
File: 327_Count_total_nodes_in_a_complete_BT.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: If left height equals right height, tree is perfect: count is 2^height - 1.
# Else recurse left and right.
# Time Complexity: O((log N)^2)
# Space Complexity: O(log N)
def optimal_solution(root: TreeNode) -> int:
    if not root:
        return 0
        
    def get_left_height(node):
        h = 0
        while node:
            h += 1
            node = node.left
        return h

    def get_right_height(node):
        h = 0
        while node:
            h += 1
            node = node.right
        return h

    lh = get_left_height(root)
    rh = get_right_height(root)
    
    if lh == rh:
        return (1 << lh) - 1
        
    return 1 + optimal_solution(root.left) + optimal_solution(root.right)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    assert optimal_solution(root) == 6
    print("Done.")
