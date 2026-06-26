"""
LeetCode Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
Problem Name: Binary Tree Maximum Path Sum
Description: Find the maximum path sum of any non-empty path.

Folder: Binary_Trees
File: 312_Maximum_path_sum.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: DFS function returns maximum path sum starting from node going down.
# Ignore negative path sums. Update max sum with (left + right + node.val).
# Time Complexity: O(N)
# Space Complexity: O(H)
def optimal_solution(root: TreeNode) -> int:
    max_sum = -float('inf')
    
    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))
        max_sum = max(max_sum, left + right + node.val)
        return node.val + max(left, right)

    dfs(root)
    return max_sum

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert optimal_solution(root) == 42
    print("Done.")
