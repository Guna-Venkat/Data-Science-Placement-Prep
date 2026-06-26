"""
LeetCode Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Problem Name: Kth Smallest/Largest Element in BST
Description: Find the Kth smallest and Kth largest elements in a BST.

Folder: Binary_Search_Trees
File: 342_Find_Kth_smallest_largest_element_in_BST.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Inorder traversal goes in sorted order. We can run iterative inorder
# using a stack and count up to K.
# Time Complexity: O(N) worst-case
# Space Complexity: O(H) stack
def kth_smallest(root: TreeNode, k: int) -> int:
    stack = []
    curr = root
    count = 0
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        count += 1
        if count == k:
            return curr.val
        curr = curr.right
    return -1

def get_node_count(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + get_node_count(root.left) + get_node_count(root.right)

def kth_largest(root: TreeNode, k: int) -> int:
    # Kth largest is (N - k + 1)th smallest
    n = get_node_count(root)
    return kth_smallest(root, n - k + 1)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(2), TreeNode(4))
    root.right = TreeNode(6)
    
    assert kth_smallest(root, 1) == 2
    assert kth_smallest(root, 3) == 4
    assert kth_largest(root, 1) == 6
    print("Done.")
