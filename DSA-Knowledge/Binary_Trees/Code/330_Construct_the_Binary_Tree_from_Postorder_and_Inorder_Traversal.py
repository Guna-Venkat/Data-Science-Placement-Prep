"""
LeetCode Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
Problem Name: Construct Binary Tree from Inorder and Postorder Traversal
Description: Construct binary tree from postorder and inorder arrays.

Folder: Binary_Trees
File: 330_Construct_the_Binary_Tree_from_Postorder_and_Inorder_Traversal.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Postorder last element is root. Traversed backward: build right child first, then left.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(inorder: list[int], postorder: list[int]) -> TreeNode:
    in_map = {val: idx for idx, val in enumerate(inorder)}
    post_idx = len(postorder) - 1
    
    def build(in_start, in_end):
        nonlocal post_idx
        if in_start > in_end:
            return None
            
        root_val = postorder[post_idx]
        root = TreeNode(root_val)
        post_idx -= 1
        
        root_idx = in_map[root_val]
        root.right = build(root_idx + 1, in_end)
        root.left = build(in_start, root_idx - 1)
        return root

    return build(0, len(inorder) - 1)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    ino = [9, 3, 15, 20, 7]
    post = [9, 15, 7, 20, 3]
    root = optimal_solution(ino, post)
    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
    print("Done.")
