"""
LeetCode Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Problem Name: Serialize and Deserialize Binary Tree
Description: Convert binary tree to string and back.

Folder: Binary_Trees
File: 331_Serialize_and_De_serialize_BT.py
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
class Codec:
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return "#"
        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"

    def deserialize(self, data: str) -> TreeNode:
        vals = data.split(",")
        idx = 0
        
        def build():
            nonlocal idx
            if vals[idx] == "#":
                idx += 1
                return None
            root = TreeNode(int(vals[idx]))
            idx += 1
            root.left = build()
            root.right = build()
            return root
            
        return build()

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    codec = Codec()
    serialized = codec.serialize(root)
    deserialized = codec.deserialize(serialized)
    assert deserialized.val == 1
    assert deserialized.left.val == 2
    assert deserialized.right.val == 3
    print("Done.")
