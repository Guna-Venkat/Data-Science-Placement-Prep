"""
LeetCode Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
Problem Name: Morris Preorder Traversal
Description: Preorder traversal in O(1) space.

Folder: Binary_Trees
File: 332_Morris_Preorder_Traversal_of_a_Binary_Tree.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Morris traversal establishes temporary links (threads) from rightmost node 
# of left subtree back to the current node.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(root: TreeNode) -> list[int]:
    res = []
    curr = root
    while curr:
        if not curr.left:
            res.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right
                
            if not prev.right:
                res.append(curr.val) # Preorder: record node before moving left
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                curr = curr.right
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert optimal_solution(root) == [1, 2, 3]
    print("Done.")
