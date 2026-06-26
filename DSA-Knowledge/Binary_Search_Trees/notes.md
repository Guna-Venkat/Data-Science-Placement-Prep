# Binary Search Trees - Topic Notes

## Patterns Learned

### 1. BST Search and Properties
*   In a BST, for any node: `all_left_nodes.val < node.val < all_right_nodes.val`.
*   **Search**: Compare target with `node.val`. If smaller, go left. If larger, go right. Repeat iteratively/recursively. $O(H)$ time complexity, where $H$ is the tree height.
*   **Floor/Ceil**: 
    *   *Ceil*: If `node.val >= X`, record as potential ceil, search left for smaller valid values. Else search right.
    *   *Floor*: If `node.val <= X`, record as potential floor, search right for larger valid values. Else search left.

### 2. Inorder Traversal Properties
*   Inorder traversal of a BST yields keys in strictly sorted order.
*   **Kth Smallest**: Run iterative inorder traversal using stack. Return the Kth popped element.
*   **Kth Largest**: Equal to $(N - K + 1)$th smallest, where $N$ is total node count.
*   **Two Sum IV**: Use two BST Iterators. One runs normal inorder (`next()`), the other runs reverse inorder (`before()`). Use two-pointer approach to find matching sum in $O(N)$ time and $O(H)$ space.

### 3. Tree Validation (BST Range Check)
*   **Valid BST**: Pass a range `[min_val, max_val]` to each node. For left child, range becomes `[min_val, node.val)`. For right child, range becomes `(node.val, max_val]`. If any node value falls out of range, tree is invalid.

### 4. BST Construction & Reconstruction
*   **Construct from Preorder**: Use a global index pointer and pass an upper bound limit to recursive calls. A node is only created if `preorder[idx] < upper_bound`. Left child limit is current node value; right child limit is the parent's upper bound limit. $O(N)$ solution.

### 5. Node Deletion in BST
*   Case 1: Node has no children. Set node pointer in parent to `None`.
*   Case 2: Node has one child. Replace node with its child.
*   Case 3: Node has two children. Find inorder successor (minimum element of the right subtree), copy its value to the current node, and delete the successor node.

---

## Common Mistakes in Binary Search Trees

1.  **Duplicate Elements**: Failing to account for duplicate values. In standard BSTs, elements are distinct. Check problem specifications for how to handle equals (usually left child $\le$ root or right child $\ge$ root).
2.  **Simple BST Validation Pitfall**: Only checking `node.left.val < node.val < node.right.val` for each local node. This does not guarantee the entire tree is a BST. A node in a left subtree could be larger than the root. Always use a range validation method.
3.  **Recursion Stack Overflow**: For highly skewed BSTs (where $H = N$), recursive solutions can exceed recursion depth. Prefer iterative methods where applicable (e.g. search, ceil/floor, LCA).

---

## Edge Cases Specific to Binary Search Trees

*   **Skewed Trees**: Left-skewed or right-skewed trees act like linked lists. Height $H = N$. Ensure space complexities are noted as $O(N)$ for skewed cases.
*   **Node Not Found**: In Ceil/Floor/Search/Successor, return `-1` or `None` if no matching node satisfies the condition.
*   **Empty Trees**: Check if root is `None` first.
*   **LCA of P/Q when one is parent of another**: LCA is simply the parent node itself.
