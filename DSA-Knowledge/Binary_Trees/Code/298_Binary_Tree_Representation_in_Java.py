"""
LeetCode Link: https://www.geeksforgeeks.org/problems/binary-tree-representation/1
Problem Name: Binary Tree Representation
Description: Build a binary tree representation. Return root.

Folder: Binary_Trees
File: 298_Binary_Tree_Representation_in_Java.py
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
def optimal_solution(arr: list[int]) -> TreeNode:
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        curr = queue.pop(0)
        if i < len(arr):
            curr.left = TreeNode(arr[i])
            queue.append(curr.left)
            i += 1
        if i < len(arr):
            curr.right = TreeNode(arr[i])
            queue.append(curr.right)
            i += 1
    return root

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = optimal_solution([1, 2, 3, 4, 5])
    assert root.val == 1
    assert root.left.val == 2
    assert root.right.val == 3
    print("Done.")
