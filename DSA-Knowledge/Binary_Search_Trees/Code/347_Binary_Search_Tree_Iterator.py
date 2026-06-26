"""
LeetCode Link: https://leetcode.com/problems/binary-search-tree-iterator/
Problem Name: BST Iterator
Description: Implement an iterator over a BST that represents in-order traversal.

Folder: Binary_Search_Trees
File: 347_Binary_Search_Tree_Iterator.py
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Initialize with stack, push all left children.
# next() pops element and pushes all left children of its right child.
# Time Complexity: O(1) amortized
# Space Complexity: O(H)
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self._push_all_left(root)
        
    def _push_all_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self._push_all_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15, TreeNode(9), TreeNode(20))
    
    iterator = BSTIterator(root)
    assert iterator.next() == 3
    assert iterator.next() == 7
    assert iterator.hasNext() == True
    assert iterator.next() == 9
    print("Done.")
