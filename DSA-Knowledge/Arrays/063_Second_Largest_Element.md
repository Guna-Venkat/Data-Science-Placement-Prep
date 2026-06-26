# Second Largest Element

## Difficulty
Easy

---

## Pattern
Iterative / Single Pass

---

## Recognition Clues
- Find the second-best/runner-up value.
- Handles duplicate values and requires strict inequality for the runner-up.

---

## Core Insight
- Maintain two running variables, `largest` and `second_largest`. When a new maximum is found, the previous maximum is demoted to the second largest.

---

## Interview Explanation
1. **Brute Force Idea**: Sort the array in descending order. The first element is the largest. Traverse from index 1 to $N-1$ and return the first element that is strictly smaller than the largest.
2. **Why Inefficient**: Sorting takes $O(N \log N)$ time, which is wasteful since we only need the top two unique elements.
3. **Key Observation**: We can maintain both the maximum and the second-maximum elements in a single pass of the array.
4. **Optimal Solution Intuition**: Initialize `largest = -infinity` and `second_largest = -infinity`. Iterate through the array. For each element `num`:
   - If `num > largest`, then `second_largest` becomes `largest`, and `largest` is updated to `num`.
   - If `num < largest` and `num > second_largest`, we update `second_largest` to `num`.
5. **Time Complexity**: $O(N)$ because we process the array in one pass.
6. **Space Complexity**: $O(1)$ since only two variables are tracked.

---

## Brute Force
- **Idea**: Sort the array in descending order, then iterate to find the first element different from the largest.
- **Code**:
```python
def second_largest_brute(arr):
    if len(arr) < 2:
        return -1
    arr.sort(reverse=True)
    largest = arr[0]
    for num in arr[1:]:
        if num != largest:
            return num
    return -1
```
- **TC**: $O(N \log N)$
- **SC**: $O(1)$

---

## Optimal Approach
- **Algorithm**: Initialize `largest` and `second_largest` to negative infinity. Iterate through the array. Update the values according to whether `num` exceeds `largest` or lies between `largest` and `second_largest`.
- **Why it works**: By comparing each element to the two running limits, we maintain the invariant that at any index $i$, `largest` and `second_largest` hold the top two unique elements in `arr[0...i]`.
- **Complexity**: Time: $O(N)$, Space: $O(1)$.

---

## Optimal Code
```python
def second_largest(arr):
    if len(arr) < 2:
        return -1
        
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
            
    return second_largest if second_largest != float('-inf') else -1
```

---

## Test Cases
- **Normal Case**: 
  - Input: `arr = [12, 35, 1, 10, 34, 1]`
  - Output: `34`
- **Hard Case**: 
  - Input: `arr = [-10, -10, -10]`
  - Output: `-1` (no second largest exists)
- **Edge Case**: 
  - Input: `arr = [10, 5]`
  - Output: `5`

---

## Common Mistakes
- Initializing `second_largest` to `0` or `-1` which fails if all elements are negative.
- Forgetting to check `num != largest` when updating `second_largest` (mistakenly counting duplicates of the largest element).
- Forgetting to demote `largest` to `second_largest` when a new maximum is found.

---

## Killer Edge Cases
- All elements are equal.
- Array contains only negative numbers.
- Array has fewer than 2 elements.

---

## Follow-Up Variants
- **Second Largest** $\rightarrow$ **K-th Largest Element**: Find the $K$-th largest element (requires Min-Heap or Quick Select).

---

## Similar Problems
- Second Smallest Element
- Find Third Largest Element

---

## Theory Connections
- **Tournament Method**: A selection algorithm that finds the maximum and second largest using $N + \lceil \log_2 N \rceil - 2$ comparisons, which is theoretically optimal.

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

