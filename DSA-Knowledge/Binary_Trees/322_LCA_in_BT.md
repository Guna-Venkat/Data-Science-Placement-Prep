# Lowest Common Ancestor in Binary Tree

**Pattern:** Binary Tree DFS Recursion (Bottom-up Propagation)

**Recognition:**
- Find the lowest shared ancestor node of two given nodes `p` and `q`.
- General Binary Tree (no sorted properties like BST).
- Decision rule: if current node is null, `p`, or `q`, return current node. Otherwise, recursively search left and right children. If both return non-null, current node is the LCA.

**Optimal Code (Python):**
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # Base case: if root is None or we find either p or q
    if not root or root == p or root == q:
        return root
        
    # Search in left and right subtrees
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    # If both left and right are non-null, current node is the LCA
    if left and right:
        return root
        
    # If only one child is non-null, return the non-null value
    return left if left else right
```

**Killer Edge:**
- One node is the parent of the other (e.g. `p` is the parent of `q`, meaning `p` itself is the LCA).
- Nodes are in opposite subtrees of the root.

**Mistake:**
- Applying Binary Search Tree LCA logic (checking values of root against `p.val` and `q.val` to decide which subtree to search) which fails for general binary trees without sorted properties.
- Not propagating the found node value correctly up the recursive call stack (returning `None` instead of the found subtree reference).
