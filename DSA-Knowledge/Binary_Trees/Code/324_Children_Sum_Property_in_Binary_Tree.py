"""
LeetCode Link: https://www.codingninjas.com/studio/problems/childrensumproperty_790775
Problem Name: Children Sum Property in Binary Tree
Description: Convert a binary tree such that each node's value equals sum of children's values. Incrementing only.

Folder: Binary_Trees
File: 324_Children_Sum_Property_in_Binary_Tree.py
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
def optimal_solution(root: TreeNode):
    if not root or (not root.left and not root.right):
        return
        
    child_sum = 0
    if root.left: child_sum += root.left.val
    if root.right: child_sum += root.right.val
    
    if child_sum >= root.val:
        root.val = child_sum
    else:
        # propagate parent's value down to prevent node deficit
        if root.left: root.left.val = root.val
        if root.right: root.right.val = root.val
        
    optimal_solution(root.left)
    optimal_solution(root.right)
    
    total = 0
    if root.left: total += root.left.val
    if root.right: total += root.right.val
    if root.left or root.right:
        root.val = total

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(2, TreeNode(35, TreeNode(2), TreeNode(3)), TreeNode(10, TreeNode(5), TreeNode(2)))
    optimal_solution(root)
    # verify root val equals children sum
    assert root.val == root.left.val + root.right.val
    print("Done.")
