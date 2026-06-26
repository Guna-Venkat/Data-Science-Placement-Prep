"""
LeetCode Link: https://leetcode.com/problems/delete-node-in-a-bst/
Problem Name: Delete Node in a BST
Description: Delete a node with the given key from the BST.

Folder: Binary_Search_Trees
File: 341_Delete_a_Node_in_BST.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Search for the node. Once found:
# - If node has 0 or 1 child, replace with child.
# - If node has 2 children, find inorder successor (min of right child), 
#   replace node value with successor value, and delete successor.
# Time Complexity: O(H)
# Space Complexity: O(H) recursion stack
def optimal_solution(root: TreeNode, key: int) -> TreeNode:
    if not root:
        return None
        
    if key < root.val:
        root.left = optimal_solution(root.left, key)
    elif key > root.val:
        root.right = optimal_solution(root.right, key)
    else:
        # Case 1 & 2: 0 or 1 child
        if not root.left:
            return root.right
        if not root.right:
            return root.left
            
        # Case 3: 2 children. Find min in right subtree.
        curr = root.right
        while curr.left:
            curr = curr.left
            
        root.val = curr.val
        root.right = optimal_solution(root.right, curr.val)
        
    return root

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(2), TreeNode(4))
    root.right = TreeNode(6, None, TreeNode(7))
    
    new_root = optimal_solution(root, 3)
    # 3 is deleted, either 4 or 2 takes its place
    assert new_root.left.val == 4 or new_root.left.val == 2
    print("Done.")
