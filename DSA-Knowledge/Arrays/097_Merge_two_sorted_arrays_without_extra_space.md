# Merge two sorted arrays without extra space

## Difficulty
Hard

---

## Pattern
Gap Method (Shell Sort Variant) / Two Pointers

---

## Recognition Clues
- Merge two sorted arrays `arr1` and `arr2` of sizes $N$ and $M$ in-place.\n- The merged elements must be sorted: first $N$ elements in `arr1` and next $M$ in `arr2`.\n- No auxiliary space is allowed ($O(1)$ auxiliary space).

---

## Core Insight
- Since arrays are sorted, the largest elements of `arr1` should be swapped with the smallest elements of `arr2` if they are out of order.\n- We can use two pointers: `left = N - 1` (end of `arr1`) and `right = 0` (start of `arr2`). Swap elements if `arr1[left] > arr2[right]`, then sort both arrays separately.\n- Alternatively, the **Gap Method** (based on Shell Sort) compares elements at a distance `gap = ceil((N+M)/2)`. We swap elements if they are out of order, and divide the gap by 2 until it becomes 0.

---

## Interview Explanation
1. **Brute Force Idea**: Create an auxiliary array of size $N+M$. Copy both arrays into it, sort the combined array, and copy the first $N$ elements back to `arr1` and the next $M$ elements to `arr2`.
2. **Why Inefficient**: Takes $O(N+M)$ extra space, which violates the $O(1)$ space constraint.
3. **Key Observation**: Any element in `arr1` must be smaller than or equal to any element in `arr2`. We can compare elements from the end of `arr1` and the start of `arr2`. If they are out of order, swap them. Once all out-of-order elements are swapped, sort the arrays individually.
4. **Optimal Solution Intuition (Two-Pointer Swap + Sort)**:
   - Set `left = N - 1` and `right = 0`.
   - While `left >= 0` and `right < M`:
     - If `arr1[left] > arr2[right]`, swap `arr1[left]` and `arr2[right]`, decrement `left`, and increment `right`.
     - Else, break (since elements are in correct partitions).
   - Sort `arr1` and sort `arr2` in-place. (Sorting takes $O(N \log N + M \log M)$ time).
5. **Time Complexity**: $O((N+M)\log(N+M))$ if using the Gap Method, or $O(N \log N + M \log M)$ for the Swap+Sort method.
6. **Space Complexity**: $O(1)$ auxiliary space.

---

## Brute Force
- **Idea**: Combine both arrays into a temporary list, sort it, and partition back.
- **Code**:
```python
def merge_brute(arr1, arr2, n, m):
    temp = arr1 + arr2
    temp.sort()
    for i in range(n):
        arr1[i] = temp[i]
    for i in range(m):
        arr2[i] = temp[n + i]
```
- **TC**: $O((N+M)\log(N+M))$
- **SC**: $O(N+M)$

---

## Optimal Approach
- **Algorithm**: Two-pointer partitioning followed by individual sorting (or the Gap Method).
- **Why it works**: Swapping out-of-order elements across the boundary establishes the correct partitions, allowing standard sorting algorithms to finish the sorting in-place.
- **Complexity**: Time: $O(N \log N + M \log M)$, Space: $O(1)$ auxiliary space.

---

## Optimal Code
```python
def merge(arr1, arr2, n, m):
    left = n - 1
    right = 0
    
    # 1. Swap elements across boundaries if out of order
    while left >= 0 and right < m:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break
            
    # 2. Sort both arrays individually in-place
    arr1.sort()
    arr2.sort()
```

---

## Test Cases
- **Normal Case**: Input: `arr1 = [1, 3, 5, 7]`, `arr2 = [0, 2, 6, 8, 9]`, `n = 4`, `m = 5`\n- Output: `arr1 = [0, 1, 2, 3]`, `arr2 = [5, 6, 7, 8, 9]`
- **Hard Case**: Input: `arr1 = [10, 12]`, `arr2 = [5, 18, 20]`, `n = 2`, `m = 3`\n- Output: `arr1 = [5, 10]`, `arr2 = [12, 18, 20]`
- **Edge Case**: Input: `arr1 = [1]`, `arr2 = [2]`\n- Output: `arr1 = [1]`, `arr2 = [2]`

---

## Common Mistakes
- Forgetting to sort the arrays after swapping elements.\n- Out of bounds errors during swap pointer increments.

---

## Killer Edge Cases
- All elements in `arr1` are larger than all elements in `arr2`.\n- All elements are already in sorted order.\n- Arrays have unequal sizes.

---

## Follow-Up Variants
- Merge Sorted Arrays without Space $\rightarrow$ Merge Sorted Arrays (LeetCode 88 - with space padded in `arr1`).

---

## Similar Problems
- Merge Sorted Array (LeetCode 88)\n- Shell Sort

---

## Theory Connections
- Shell Sort / Gap Method: The Gap Method is a variation of Shell Sort. By comparing elements at decreasing step intervals (gaps), it resolves long-distance inversions faster, sorting the combined space in-place in $O((N+M) \log (N+M))$ time.

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
