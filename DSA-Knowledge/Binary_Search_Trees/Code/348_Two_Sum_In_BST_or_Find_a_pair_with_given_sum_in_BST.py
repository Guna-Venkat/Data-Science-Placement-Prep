"""
LeetCode Link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
Problem Name: Two Sum IV - Input is a BST
Description: Find if there exist two elements in the BST such that their sum is equal to target.

Folder: Binary_Search_Trees
File: 348_Two_Sum_In_BST_or_Find_a_pair_with_given_sum_in_BST.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Initialize two stacks for iterative traversals (next and before).
# Perform standard two-pointer search.
# Time Complexity: O(N)
# Space Complexity: O(H)
class BSTIterator:
    def __init__(self, root: TreeNode, is_reverse: bool):
        self.stack = []
        self.is_reverse = is_reverse
        self._push(root)
        
    def _push(self, node):
        while node:
            self.stack.append(node)
            node = node.right if self.is_reverse else node.left
            
    def next_val(self) -> int:
        node = self.stack.pop()
        self._push(node.left if self.is_reverse else node.right)
        return node.val

def find_target(root: TreeNode, k: int) -> bool:
    if not root:
        return False
    left_iter = BSTIterator(root, False)
    right_iter = BSTIterator(root, True)
    
    l = left_iter.next_val()
    r = right_iter.next_val()
    
    while l < r:
        curr_sum = l + r
        if curr_sum == k:
            return True
        elif curr_sum < k:
            l = left_iter.next_val()
        else:
            r = right_iter.next_val()
            
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(2), TreeNode(4))
    root.right = TreeNode(6, None, TreeNode(7))
    
    assert find_target(root, 9) == True
    assert find_target(root, 28) == False
    print("Done.")
