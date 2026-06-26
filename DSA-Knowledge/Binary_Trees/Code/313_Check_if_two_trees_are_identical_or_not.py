"""
LeetCode Link: https://leetcode.com/problems/same-tree/
Problem Name: Same Tree
Description: Check if two binary trees are identical.

Folder: Binary_Trees
File: 313_Check_if_two_trees_are_identical_or_not.py
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
def optimal_solution(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return optimal_solution(p.left, q.left) and optimal_solution(p.right, q.right)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    t1 = TreeNode(1, TreeNode(2), TreeNode(3))
    t2 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert optimal_solution(t1, t2) == True
    print("Done.")
