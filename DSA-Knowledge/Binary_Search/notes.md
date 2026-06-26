# Binary Search - Topic Notes

## Patterns Learned

### 1. Basic Binary Search & Bounds
*   **Lower Bound**: Find the first element $\ge X$. If `arr[mid] >= X`, record index `mid` as a potential answer and search the left half (`high = mid - 1`). Otherwise, search the right half.
*   **Upper Bound**: Find the first element $> X$. Same as Lower Bound, but using `arr[mid] > X`.
*   **Search Insert Position**: Identical to Lower Bound.

### 2. Search in Rotated Sorted Array
*   **Core Logic**: In a rotated sorted array, at least one half is always sorted. Check which half is sorted:
    *   If `arr[low] <= arr[mid]`, the left half is sorted. Check if target lies in `[arr[low], arr[mid])` to narrow search, otherwise search right half.
    *   Otherwise, the right half is sorted. Check if target lies in `(arr[mid], arr[high]]` to search right, otherwise search left.
*   **Handling Duplicates**: If `arr[low] == arr[mid] == arr[high]`, we cannot determine which half is sorted. Shrink the boundary: `low += 1`, `high -= 1` and continue.

### 3. Binary Search on Answer Space
*   Used when finding an optimal value (minimum of maximums, maximum of minimums, etc.) where a validation function `can_do(val)` is monotonic (i.e. if it is possible for `X`, it is also possible for all `Y > X`).
*   **Aggressive Cows**: Maximize the minimum distance between cows. Validation function check: Can we place all cows with distance $\ge D$?
*   **Book Allocation / Split Array Largest Sum / Painter's Partition**: Minimize the maximum sum/load. Validation function check: Can we allocate/split using at most $M$ students/subarrays?
*   **Koko Eating Bananas / Smallest Divisor**: Range is between $1$ and maximum element. Find the smallest speed/divisor that satisfies the hour/sum limit.

### 4. Binary Search on 2D Matrix
*   **Flattened 2D Search**: For a matrix where each row is sorted and the first element of a row is greater than the last element of the previous row. Treat as a 1D array of size $N \times M$. Map index `mid` to 2D using `row = mid // M` and `col = mid % M`.
*   **Corner Search (Row-Col wise sorted)**: Start at top-right corner. If `mat[r][c] == target`, found. If `target < mat[r][c]`, column `c` cannot contain target, decrement `c`. If `target > mat[r][c]`, row `r` cannot contain target, increment `r`.
*   **2D Peak Finder**: Binary search on columns. Find the maximum element index `max_row` in the middle column. If it is greater than neighbors in the adjacent columns (left/right), we found a peak. Otherwise, move the column boundary to the larger neighbor's side.

---

## Common Mistakes in Binary Search

1.  **Infinite Loops (`low <= high`)**: Using `low = mid` or `high = mid` instead of `low = mid + 1` and `high = mid - 1` when splitting integer ranges, causing the search to get stuck when `low == high - 1`.
2.  **Integer Overflow on `mid`**: Calculating `mid = (low + high) // 2` can cause overflow in statically typed languages if `low + high` exceeds maximum integer value. Safe formula: `mid = low + (high - low) // 2`.
3.  **Monotonicity Check in "BS on Answer"**: Not sorting the input array for problems like "Aggressive Cows" before validating placement, which invalidates the greedy distance check.
4.  **Floating Point Precision**: In "Minimize Max Distance to Gas Station", using standard integer division instead of float divisions, or not running the search for a fixed number of iterations (e.g. 100 iterations) to guarantee precision.

---

## Edge Cases Specific to Binary Search

*   **Target out of bounds**: Target smaller than first element or larger than last element.
*   **Array size 1 or 2**: Ensure bounds don't crash and the single/double elements are correctly verified.
*   **Duplicate Elements**: Lower/upper bound logic must be used to find first/last occurrences instead of returning immediately upon a target match.
*   **Rotated Array with no rotation**: The array is already fully sorted. The rotated search logic must handle this seamlessly (e.g. by recognizing the left half is sorted and continuing).
