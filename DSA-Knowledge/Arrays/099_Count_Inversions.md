# Count Inversions

## Difficulty
Hard

---

## Pattern
Merge Sort / Divide and Conquer

---

## Recognition Clues
- Count pairs $(i, j)$ such that $i < j$ and $arr[i] > arr[j]$.\n- Indicates how close the array is to being sorted.

---

## Core Insight
- A brute force double loop takes $O(N^2)$ time.\n- We can divide the array into two halves, recursively count inversions in both halves, and count cross-inversions during the merge step.\n- During merging of sorted halves `left_arr` and `right_arr`: if `left_arr[i] > right_arr[j]`, then all remaining elements in `left_arr` (from index `i` to the end) are also greater than `right_arr[j]`. Add `mid - i + 1` to the inversion count.

---

## Interview Explanation
1. **Brute Force Idea**: Use two nested loops to check all pairs $(i, j)$ where $j > i$. If `arr[i] > arr[j]`, increment the inversion count.
2. **Why Inefficient**: Comparing all pairs takes $O(N^2)$ time.
3. **Key Observation**: If we split the array and sort the halves, we can count inversions in $O(N \log N)$ time. During the merge step of Merge Sort, if an element from the right half is smaller than an element from the left half, it is smaller than all remaining elements in that left half because the left half is sorted.
4. **Optimal Solution Intuition**:
   - Implement a recursive Merge Sort function that returns the inversion count.
   - In the merge step, maintain pointers `i` (left half) and `j` (right half).
   - If `arr[i] <= arr[j]`, append `arr[i]` to the merged result.
   - If `arr[i] > arr[j]`, it forms inversions with `arr[i...mid]`. Increment `inv_count` by `(mid - i + 1)` and append `arr[j]`.
5. **Time Complexity**: $O(N \log N)$ (same as Merge Sort).
6. **Space Complexity**: $O(N)$ for temporary array storage during merging.

---

## Brute Force
- **Idea**: Check all possible pairs using two loops.
- **Code**:
```python
def countInversions_brute(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    return count
```
- **TC**: $O(N^2)$
- **SC**: $O(1)$

---

## Optimal Approach
- **Algorithm**: Merge Sort-based divide and conquer.
- **Why it works**: Sorting segments enables counting range inversions collectively instead of individually, bringing time complexity down to $O(N \log N)$.
- **Complexity**: Time: $O(N \log N)$, Space: $O(N)$ auxiliary space.

---

## Optimal Code
```python
def countInversions(arr):
    def merge_and_count(temp_arr, left, mid, right):
        i, j, k = left, mid + 1, left
        inv_count = 0
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                # Elements left[i...mid] are greater than right[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
            
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1
            
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1
            
        for loop_var in range(left, right + 1):
            arr[loop_var] = temp_arr[loop_var]
            
        return inv_count

    def merge_sort_and_count(temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += merge_sort_and_count(temp_arr, left, mid)
            inv_count += merge_sort_and_count(temp_arr, mid + 1, right)
            inv_count += merge_and_count(temp_arr, left, mid, right)
        return inv_count

    n = len(arr)
    temp = [0] * n
    return merge_sort_and_count(temp, 0, n - 1)
```

---

## Test Cases
- **Normal Case**: Input: `arr = [8, 4, 2, 1]`\n- Output: `6` (pairs: (8,4), (8,2), (8,1), (4,2), (4,1), (2,1))
- **Hard Case**: Input: `arr = [2, 4, 1, 3, 5]`\n- Output: `3` (pairs: (2,1), (4,1), (4,3))
- **Edge Case**: Input: `arr = [1, 2, 3]`\n- Output: `0` (sorted)

---

## Common Mistakes
- Off-by-one errors in recursion base cases or mid-points.\n- Adding `mid - i` instead of `mid - i + 1` to the inversion count.

---

## Killer Edge Cases
- Array is sorted in ascending order (0 inversions).\n- Array is sorted in descending order ($N(N-1)/2$ inversions).\n- Array contains duplicate elements.

---

## Follow-Up Variants
- Count Inversions $\rightarrow$ Reverse Pairs (LeetCode 493).

---

## Similar Problems
- Reverse Pairs (LeetCode 493)\n- Global and Local Inversions (LeetCode 775)

---

## Theory Connections
- Divide and Conquer: By sorting subsegments, we establish order invariants that permit counting multiple relationship properties in logarithmic steps. Inversion count is used in rank correlation statistics (Kendall's tau coefficient).

---

## Personal Progress

**Confidence**
- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4
- [ ] 5

**Time Bucket**
- [ ] <10 min
- [ ] 10-20
- [ ] 20-40
- [ ] 40+

**Status**
- [ ] Not Attempted
- [ ] Hint Used
- [ ] Solved
- [ ] Mastered

**Revision Count**: 
**Last Revised**: 
**Next Review**: 

---

## Notes
