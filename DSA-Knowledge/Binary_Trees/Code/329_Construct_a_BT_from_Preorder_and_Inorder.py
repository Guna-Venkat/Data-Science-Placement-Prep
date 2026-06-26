"""
LeetCode Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Problem Name: Construct Binary Tree from Preorder and Inorder Traversal
Description: Construct binary tree from preorder and inorder arrays.

Folder: Binary_Trees
File: 329_Construct_a_BT_from_Preorder_and_Inorder.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Preorder first element is root. Find its position in Inorder to split left/right subtrees.
# Time Complexity: O(N)
# Space Complexity: O(N) mapping
def optimal_solution(preorder: list[int], inorder: list[int]) -> TreeNode:
    in_map = {val: idx for idx, val in enumerate(inorder)}
    pre_idx = 0
    
    def build(in_start, in_end):
        nonlocal pre_idx
        if in_start > in_end:
            return None
            
        root_val = preorder[pre_idx]
        root = TreeNode(root_val)
        pre_idx += 1
        
        root_idx = in_map[root_val]
        root.left = build(in_start, root_idx - 1)
        root.right = build(root_idx + 1, in_end)
        return root

    return build(0, len(inorder) - 1)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    pre = [3, 9, 20, 15, 7]
    ino = [9, 3, 15, 20, 7]
    root = optimal_solution(pre, ino)
    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
    print("Done.")
