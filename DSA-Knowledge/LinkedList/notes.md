# LinkedList - Topic Notes

## Patterns Learned

### 1. Tortoise and Hare (Slow & Fast Pointers)
*   **Middle of Linked List**: Slow moves 1 step, Fast moves 2 steps. When Fast reaches the end (or None), Slow is exactly at the middle node.
*   **Cycle Detection (Floyd's Cycle Finding)**: Move Slow by 1 step and Fast by 2 steps. If there is a cycle, they will eventually meet.
*   **Start of Cycle**: Once Slow meets Fast inside the cycle, reset Slow to head. Move both pointers at equal speed (1 step). They will meet exactly at the starting node of the cycle.
*   **Length of Cycle**: Once Slow meets Fast, hold Fast in place. Move Slow step-by-step and count how many steps it takes to meet Fast again.

### 2. Node Reversal
*   **Iterative Reversal**: Keep pointers `prev = None`, `curr = head`. Iterate: save `temp = curr.next`, point `curr.next = prev`, shift `prev = curr`, `curr = temp`.
*   **Recursive Reversal**: Recursively reverse the rest of the list. Then set `head.next.next = head`, and break original link `head.next = None`.

### 3. Interweaving Nodes (In-Place Modifications)
*   Used to optimize space to $O(1)$ instead of using a Hash Map:
    *   **Clone List with Random Pointer**: Interleave duplicate nodes in the original list: `A -> A' -> B -> B'`. Update random pointers using `node.next.random = node.random.next`. Finally, separate original and cloned lists.
    *   **Palindrome LL Check**: Find the middle, reverse the second half, and compare both halves using two pointers. Restore the list afterward.

### 4. Dummy Nodes
*   Using a dummy node simplifies edge cases such as deleting or inserting at the head (e.g., in "Remove Nth Node from End", "Merge Sorted Lists").

---

## Common Mistakes in LinkedLists

1.  **Null Pointer Exceptions**: Accessing `node.next` when `node` is `None` (e.g., checking `fast.next.next` without first validating that `fast` and `fast.next` are not `None`).
2.  **Losing Track of Pointers**: Modifying links without preserving reference to the next nodes, causing nodes to get lost in memory. Always save `temp = curr.next` before overwriting `curr.next`.
3.  **Memory Leaks (Cycle creation)**: Creating unintended loops by not setting the `next` pointer of the final node to `None`.

---

## Edge Cases Specific to LinkedLists

*   **Single Node or Empty List**: Write guard checks `if not head or not head.next: return head`.
*   **Even vs. Odd Length Lists**: In middle element queries, verify if the problem requires the first or second middle node in case of an even length list.
*   **N exceeding List Length**: In rotation and deletion, modulo operations or bound checks are required.
