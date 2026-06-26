# Linear Search

## Difficulty
Easy

---

## Pattern
Iterative / Single Pass

---

## Recognition Clues
- Search for a specific target value in an unsorted list.
- Unstructured input where elements have no sorted relation.

---

## Core Insight
- In an unsorted array, any element could be the target. We must inspect elements one by one from index 0 to $N-1$ until a match is found.

---

## Interview Explanation
1. **Brute Force Idea**: The brute force and optimal ideas coincide for an unsorted array. We scan the array sequentially from start to end, checking if the current element matches the target.
2. **Why Inefficient**: For an unsorted array, this is not inefficient; it is the theoretical lower bound. We cannot search faster than $O(N)$ because the target could be located at the very last index.
3. **Key Observation**: We can return early (terminate the search) the moment we find the target.
4. **Optimal Solution Intuition**: Loop through the array. At each index `i`, compare `arr[i]` with `target`. If they are equal, return `i`. If the loop finishes without matching, return `-1`.
5. **Time Complexity**: $O(N)$ in the worst case (when the target is at the end or not present).
6. **Space Complexity**: $O(1)$ since no additional memory is allocated.

---

## Brute Force
- **Idea**: Scan elements sequentially (same as optimal).
- **Code**:
```python
def linear_search_brute(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```
- **TC**: $O(N)$
- **SC**: $O(1)$

---

## Optimal Approach
- **Algorithm**: Standard linear traversal.
- **Why it works**: By checking every position, we guarantee that if the element exists, we will encounter and return its first index.
- **Complexity**: Time: $O(N)$, Space: $O(1)$.

---

## Optimal Code
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
            
    return -1
```

---

## Test Cases
- **Normal Case**: 
  - Input: `arr = [3, 5, 2, 8, 11]`, `target = 8`
  - Output: `3`
- **Hard Case**: 
  - Input: `arr = [-5, 0, 10, 100, 500]`, `target = -2`
  - Output: `-1`
- **Edge Case**: 
  - Input: `arr = [42]`, `target = 42`
  - Output: `0`

---

## Common Mistakes
- Returning `-1` prematurely inside the loop (e.g., returning `-1` inside the `else` block of the comparison).
- Not returning the index of the first occurrence if duplicates exist.

---

## Killer Edge Cases
- Target is not present in the array.
- Empty array.
- Target is present multiple times.

---

## Follow-Up Variants
- **Linear Search** $\rightarrow$ **Binary Search**: If the array is sorted, we can search in $O(\log N)$ time.
  - *Delta*: Split search space in half at each step.

---

## Similar Problems
- Find Minimum/Maximum in Array
- Binary Search

---

## Theory Connections
- **Search Lower Bounds**: For an unsorted list of size $N$, finding a specific element has a lower bound complexity of $\Omega(N)$ comparisons, as proven by adversary arguments (any algorithm checking fewer than $N$ elements can be fooled by placing the target in an unchecked slot).

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

