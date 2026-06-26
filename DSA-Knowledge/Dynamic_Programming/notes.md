# Dynamic Programming - Topic Notes

## Patterns Learned

### 1. 1D DP / Fibonacci Layout
*   **Optimal Substructure**: The result of `DP[i]` depends strictly on a fixed window of previous values (e.g. `DP[i-1]`, `DP[i-2]`).
*   **Space Optimization**: Instead of maintaining a full `DP` array of size $N$, keep track of state variables like `prev` and `prev2` to achieve $O(1)$ space.

### 2. 2D & 3D Grid DP
*   **Unique Paths & Falling Sums**: Initialize base row, then transition values: `curr[c] = val + min(prev[c], prev[c-1], prev[c+1])`.
*   **3D DP (Cherry Pickup II)**: Coordinates tracking two agents simultaneously on a grid. Row `r` matches for both; keep columns `c1` and `c2`. State dimensions: `dp[r][c1][c2]`.

### 3. Subset / Knapsack DP
*   **Subset Sum**: For each element, choose to either *pick* it or *not pick* it.
*   **Space Optimization**: Backwards loop (`range(Target, val - 1, -1)`) allows running subset DP using a single-row array of size `Target + 1`.
*   **Unbounded Knapsack / Rod Cutting**: Forward loop allows reusing items infinitely: `dp[t] = max(dp[t], val + dp[t - weight])`.

### 4. String / Longest Common Subsequence (LCS)
*   **Transition**:
    *   If `S1[i] == S2[j]`: `dp[i][j] = 1 + dp[i-1][j-1]`
    *   Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`
*   **Palindromes**: Longest Palindromic Subsequence is equivalent to `LCS(S, reverse(S))`. Min insertions to make palindrome is `len(S) - LPS(S)`.

### 5. Stocks DP (State-based transition)
*   **Unlimited Transactions**: Accumulate positive price differences `prices[i] - prices[i-1]`.
*   **K Transactions / Cooldown / Fees**: Maintain separate variables or states representing holdings (`hold`, `free`, `cooldown`).

### 6. Longest Increasing Subsequence (LIS)
*   **Standard DP**: $O(N^2)$ table matching indices.
*   **Binary Search Optimization**: Maintain active pile boundaries. Use `bisect_left` to overwrite/extend active subsequence elements, yielding $O(N \log N)$ time.
*   **Print Path**: Track parent back-references `hash_prev` during dynamic programming updates to backtrack the actual LIS subsequence.

### 7. Matrix Chain Multiplication (MCM) / Partition DP
*   **Range Division**: Evaluate minimum or maximum cost of computing subarrays separated by partition `k` in range `(i, j)`.
*   **Evaluation Patterns**: Evaluating stick cuts, bursting balloons, boolean parenthesizations, and partition sums.

---

## Common Mistakes in Dynamic Programming

1.  **Improper Base Initialization**: Not initializing target indices like `dp[0] = 1` for combination counts or `dp[0] = 0` for min coins, leading to TLE or bad state outcomes.
2.  **State Space Pollution**: Updating the same DP row in a forward direction during subset checks where reuse is not allowed (Unbounded Knapsack vs Standard Knapsack).
3.  **Recursion Depth Limits**: Writing pure recursion + memoization in Python without raising `sys.setrecursionlimit()`. Always prioritize bottom-up tabulation when possible.

---

## Edge Cases Specific to Dynamic Programming

*   **Zero Values**: Handing inputs where elements can be 0 (e.g. Target Sum where picking zeros doubles combinations).
*   **Strict Decreasing / Increasing Limits**: LIS or Bitonic tests where arrays are already sorted or fully duplicate.
*   **Large Coordinates**: Handling coordinates gracefully in maximal rectangles to avoid indexing errors when input rows vary in length.
