# Binary Trees - Topic Notes

## Patterns Learned

### 1. Recursive and Iterative Traversals
*   **Depth-First Search (DFS)**: 
    *   *Preorder*: Root -> Left -> Right.
    *   *Inorder*: Left -> Root -> Right.
    *   *Postorder*: Left -> Right -> Root.
*   **Iterative with Stack**:
    *   *Preorder*: Push root. Pop, record, push right, push left.
    *   *Inorder*: Move left until None, pushing to stack. Pop, record, move right.
    *   *Postorder (2 Stacks)*: Push root to Stack 1. Pop, push to Stack 2. Push left, then right to Stack 1. Stack 2 contains postorder in reverse.
    *   *Pre/In/Post in One Pass*: Push `[node, 1]` to stack. Increment state: state 1 = Preorder (push left), state 2 = Inorder (push right), state 3 = Postorder (pop).

### 2. Breadth-First Search (BFS / Level Order)
*   Use a queue to process node level-by-level.
*   **Zigzag Traversal**: Reverse the array elements at every alternate level.
*   **Maximum Width**: Assign 0-based binary coordinates to nodes: left child is `2*i`, right child is `2*i + 1`. Width of level is `right_idx - left_idx + 1`.

### 3. Coordinate mapping (Tree Views)
*   **Vertical Order**: Keep column coordinate `x` and level `y`. Sort columns, then rows, then values.
*   **Top/Bottom Views**: Record first node visited (for Top view) or last node visited (for Bottom view) at each column coordinate `x` during Level Order traversal.
*   **Left/Right Views**: Perform DFS. If current level equals result list length, record the node. For Right View, recurse right then left. For Left View, recurse left then right.

### 4. Morris Traversal (O(1) Space)
*   Avoid stack overhead by creating temporary threads.
*   For current node, find its in-order predecessor (rightmost node in left subtree).
*   If predecessor's right pointer is null, point it to current node (create thread), move to left child.
*   If predecessor's right pointer points to current node, remove thread (set to null), record current node (for Inorder), move to right child.

---

## Common Mistakes in Binary Trees

1.  **Coordinates Overflow**: When calculating width with coordinate index doubling, Python handles large integers automatically, but other languages can overflow. Pre-emptively subtract the first index of the level to keep coordinates small.
2.  **Parent Pointer Reference**: When traversing in 3 directions (Left, Right, Parent) for distance K / burning tree queries, ensure parent pointers are correctly mapped beforehand.
3.  **Morris Traversal Leftover Threads**: Forgetting to restore `predecessor.right = None` during Morris traversal, leaving corrupted pointers in the tree.

---

## Edge Cases Specific to Binary Trees

*   **Symmetric Check**: Check mirror nodes recursively: `is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)`.
*   **Balanced Tree**: A tree is balanced if heights of left and right subtrees differ by $\le 1$ and both subtrees are balanced. Use bottom-up recursion to avoid $O(N^2)$ checks.
*   **Identical Trees**: Return `True` if both are `None`, `False` if only one is `None` or values differ.
