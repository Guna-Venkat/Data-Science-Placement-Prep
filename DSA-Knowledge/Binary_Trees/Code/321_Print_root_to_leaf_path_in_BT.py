"""
LeetCode Link: https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1
Problem Name: Root to Leaf Paths
Description: Find all paths from root to leaf nodes.

Folder: Binary_Trees
File: 321_Print_root_to_leaf_path_in_BT.py
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
# Space Complexity: O(H)
def optimal_solution(root: TreeNode) -> list[list[int]]:
    result = []
    
    def dfs(node, path):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right:
            result.append(list(path))
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        path.pop()

    dfs(root, [])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert optimal_solution(root) == [[1, 2, 4], [1, 2, 5], [1, 3]]
    print("Done.")
