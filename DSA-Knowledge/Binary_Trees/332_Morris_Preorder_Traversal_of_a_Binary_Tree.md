# Morris Preorder Traversal

**Pattern:** Threaded Binary Tree (Space-Optimized Iterative Traversal)

**Recognition:**
- Traverse a binary tree in preorder using $O(1)$ auxiliary space (no recursion stack or iterative container stack).
- Temporarily modify the tree by creating a "thread" link from the inorder predecessor (rightmost node of the left subtree) back to the current node.
- Preorder visits the node **when establishing the thread**, whereas Inorder visits when removing it.

**Optimal Code (Python):**
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def morrisPreorder(root: TreeNode) -> list[int]:
    result = []
    curr = root
    
    while curr:
        if not curr.left:
            result.append(curr.val)
            curr = curr.right
        else:
            # Find the inorder predecessor (rightmost node in left subtree)
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right
                
            if not prev.right:
                # Establish thread link
                prev.right = curr
                result.append(curr.val)  # Visit parent node (Preorder)
                curr = curr.left
            else:
                # Remove thread link to restore tree structure
                prev.right = None
                curr = curr.right
                
    return result
```

**Killer Edge:**
- Strictly right-skewed or left-skewed trees.
- Ensuring the tree structure is fully restored to its original state after traversal completes.

**Mistake:**
- Visiting `curr.val` inside the `else` block when `prev.right == curr`. That is Inorder traversal. In Preorder, we visit when `prev.right` is `None` (before traversing the left subtree).
- Omitting the `prev.right != curr` condition inside the predecessor loop, causing an infinite loop when traversing elements.
