# Arrays - Topic Notes

## Patterns Learned

### 1. Two-Pointer Technique
*   **Opposite Direction**: Useful for sorted arrays (e.g., Two Sum on sorted input, 3Sum, 4Sum). One pointer starts at `0`, the other at `N-1`. Shrink the search space based on comparisons.
*   **Same Direction (Fast & Slow)**: Used for in-place modifications (e.g., Remove Duplicates, Move Zeroes). The fast pointer scans every element, while the slow pointer tracks the boundary of write operations.

### 2. Sliding Window (Variable Size)
*   Used to find optimal subarrays matching a condition (e.g., Longest Subarray with Sum K).
*   Expand the right pointer `r` to include elements. If the sum exceeds the target, increment the left pointer `l` until the condition is satisfied again.
*   *Note*: Variable-size sliding window with two pointers only works optimally when all elements are positive (monotonic sum). For negative numbers, prefix sum with hashing is required.

### 3. Prefix Sum + HashMap (Subarray Sum Equals K / XOR K)
*   Compute running cumulative sums: `prefix_sum[i] = arr[0] + ... + arr[i]`.
*   Any subarray sum from index `j+1` to `i` is given by `prefix_sum[i] - prefix_sum[j]`.
*   To check if any subarray sums to `K`, check if `prefix_sum[i] - K` has been seen previously. Store prefix sums in a HashMap for $O(1)$ lookups.
*   Also applies to XOR queries: if $A \oplus B = C$, then $A \oplus C = B$.

### 4. Boyer-Moore Voting Algorithm (Majority Element)
*   Finds elements appearing $> N/2$ or $> N/3$ times in $O(N)$ time and $O(1)$ space.
*   Maintain candidates and counters. When counters drop to zero, select a new candidate. Equal values increment the counter, distinct values decrement it.

### 5. Kadane's Algorithm (Maximum Subarray Sum)
*   Maintain a running sum of the current subarray.
*   If the running sum falls below `0`, reset it to `0` (discarding the prefix since it would only decrease any subsequent sum).
*   Track the maximum running sum seen.

### 6. Gap Method (Shell Sort based)
*   Used to merge two sorted arrays in $O(1)$ space.
*   Compare and swap elements at a distance `gap = ceil((N + M) / 2)`. Divide `gap` by 2 after each complete pass until `gap` reaches `0`.

---

## Common Mistakes in Arrays

1.  **Index Out of Bounds during Shifts/Rotations**: Forgetting to wrap index access using `% N` or handling small arrays ($N \le 1$).
2.  **Duplicate Combinations in 3Sum/4Sum**: Not skipping identical adjacent elements when moving pointers, leading to duplicate triplets/quadruplets in the output.
3.  **Updating Map Coordinates incorrectly in Prefix Sum**: In "Longest Subarray with Sum K", we must only store the *first* occurrence of a prefix sum in the HashMap to maximize the subarray length.
4.  **Resetting Sum to 0 on Kadane's**: In arrays containing only negative numbers, resetting the running sum to `0` before updating the max sum will incorrectly yield `0` instead of the maximum single negative element. Ensure the max update occurs *before* the negative reset.

---

## Edge Cases Specific to Arrays

*   **Empty Arrays or Single Element Arrays**: Always write safety guards `if not arr: return ...`.
*   **All Negative Elements**: In maximum subarray sum, verify it handles negative values correctly.
*   **All Identical Elements**: e.g., `[1, 1, 1, 1]`, check if two-pointer loops terminate and avoid infinite loops.
*   **Values of K exceeding Array Length**: For left/right rotations, always wrap rotation steps using `k = k % N`.
*   **Overflow Risks**: In languages like C++/Java, adding elements to compute sum might cause integer overflow. In Python, this is handled automatically, but math equations like finding repeating/missing numbers using sum of squares could be computationally intensive.
