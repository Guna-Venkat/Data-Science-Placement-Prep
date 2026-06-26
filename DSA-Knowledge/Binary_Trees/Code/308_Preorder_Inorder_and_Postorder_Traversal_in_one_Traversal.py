"""
LeetCode Link: https://www.codingninjas.com/studio/problems/tree-traversals_981269
Problem Name: Tree traversals in one traversal iterative
Description: Iterative pre, in, and post order traversal in one traversal using a single stack storing tuples of (node, state).

Folder: Binary_Trees
File: 308_Preorder_Inorder_and_Postorder_Traversal_in_one_Traversal.py
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
# Space Complexity: O(H) stack space
def optimal_solution(root: TreeNode) -> tuple[list[int], list[int], list[int]]:
    if not root:
        return [], [], []
        
    pre = []
    ino = []
    post = []
    stack = [[root, 1]] # 1: pre, 2: in, 3: post
    
    while stack:
        it = stack[-1]
        node, state = it[0], it[1]
        if state == 1:
            pre.append(node.val)
            it[1] += 1
            if node.left:
                stack.append([node.left, 1])
        elif state == 2:
            ino.append(node.val)
            it[1] += 1
            if node.right:
                stack.append([node.right, 1])
        else:
            post.append(node.val)
            stack.pop()
            
    return pre, ino, post

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    pre, ino, post = optimal_solution(root)
    assert pre == [1, 2, 3]
    assert ino == [2, 1, 3]
    assert post == [2, 3, 1]
    print("Done.")
