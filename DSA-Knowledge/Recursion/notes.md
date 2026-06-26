# Recursion - Topic Notes

## Patterns Learned

### 1. Base Recursion / Math
*   **Binary Exponentiation**: Compute $x^n$ recursively in $O(\log n)$ by using the relation $x^n = (x^{n/2})^2$ for even powers.
*   **Stack Manipulations**: Use recursion to reverse or sort a stack without loops. Pop items to empty stack, recursively sort/reverse the rest, and then insert/re-insert items correctly at the bottom or in sorted order.

### 2. Pick / Non-Pick (Subsequences Pattern)
*   At each index `idx`, make two choices:
    1.  *Pick*: Add element `arr[idx]` to subsequence and call `solve(idx + 1)`.
    2.  *Don't Pick*: Call `solve(idx + 1)` without adding the element.
*   Useful for generating subsets, combinations, and counting subsequences that sum to $K$.

### 3. Backtracking with Loops
*   Used when the same level allows picking multiple different candidates.
*   Iterate through candidates from current index, choose one, backtrack, and restore state (undo).
*   **Duplicate Elimination**: Sort candidates first. In the loop, skip duplicates using `if i > idx and candidates[i] == candidates[i - 1]: continue`.

### 4. Grid DFS and Constraint Matching
*   **Word Search**: DFS check in 4 directions. Mark current cell as visited (e.g. `board[r][c] = "#"`), recurse, and then restore.
*   **N-Queens**: Track columns, main diagonals `(r - c)`, and anti-diagonals `(r + c)` in hash sets to check placement validity in $O(1)$ time.
*   **Sudoku Solver**: Traverse all cells. If empty, try placing characters `'1'` to `'9'`. Recursively check validity of board; if it fails, backtrack to `.` and try next character.

---

## Common Mistakes in Recursion

1.  **Missing Base Case**: Forgetting base cases or index out-of-bounds guards, leading to `RecursionError: maximum recursion depth exceeded`.
2.  **State Pollution**: Forgetting to backtrack (pop from lists, reset grid values, or clean up hash sets) before returning from recursive calls.
3.  **TLE on Repeating Subproblems**: Not using memoization/caching when recursion encounters identical subproblems (e.g. in Word Break or Fibonacci).

---

## Edge Cases Specific to Recursion

*   **Negative / Zero Exponents**: In Pow(x, n), handle $n = 0$ returning $1.0$ and negative powers returning $1 / x^{-n}$.
*   **Empty Inputs**: Gracefully return empty lists for empty strings or arrays.
*   **Leading Zeros**: In string partitioning and expression generation, skip cases where partitions begin with a leading zero (e.g. `"05"` is invalid if length > 1).
