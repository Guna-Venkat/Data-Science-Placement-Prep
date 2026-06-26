# Left Rotate Array by One

## Difficulty
Easy

---

## Pattern
Iterative / Cyclic Shift

---

## Recognition Clues
- Move all elements left by exactly one position.
- Circular wrap-around of the first element to the last index.

---

## Core Insight
- Save the first element in a temporary variable, shift all subsequent elements to the left by one index, and then write the saved element to the last position.

---

## Interview Explanation
1. **Brute Force Idea**: Allocate an auxiliary array of size $N$. Copy `arr[1...N-1]` into `temp[0...N-2]` and copy `arr[0]` into `temp[N-1]`. Finally, copy the contents of `temp` back into `arr`.
2. **Why Inefficient**: Utilizing an auxiliary array results in $O(N)$ extra space complexity, which is unnecessary because the elements can be shifted in-place.
3. **Key Observation**: The displacement is a simple shift for $N-1$ elements. Only the first element wraps around. By saving the first element, we can perform the shift in-place without losing data.
4. **Optimal Solution Intuition**: Initialize a temporary variable `temp` to store `arr[0]`. Loop through the array from index 1 to $N-1$ and set `arr[i - 1] = arr[i]`. After the loop, set the last element `arr[N - 1] = temp`.
5. **Time Complexity**: $O(N)$ since we scan the array elements once.
6. **Space Complexity**: $O(1)$ auxiliary space because we only use a single temporary variable.

---

## Brute Force
- **Idea**: Use an auxiliary array to construct the rotated result and copy it back.
- **Code**:
```python
def left_rotate_one_brute(arr):
    if not arr:
        return arr
    n = len(arr)
    temp = [0] * n
    for i in range(1, n):
        temp[i - 1] = arr[i]
    temp[n - 1] = arr[0]
    for i in range(n):
        arr[i] = temp[i]
    return arr
```
- **TC**: $O(N)$
- **SC**: $O(N)$

---

## Optimal Approach
- **Algorithm**: 
  1. If the array is empty, return it.
  2. Save `temp = arr[0]`.
  3. Iterate $i$ from 1 to $N-1$ and shift: `arr[i - 1] = arr[i]`.
  4. Assign `arr[N - 1] = temp`.
- **Why it works**: Each element at index $i$ shifts to index $i-1$, and the first element is correctly placed at the empty slot at index $N-1$.
- **Complexity**: Time: $O(N)$, Space: $O(1)$.

---

## Optimal Code
```python
def left_rotate_by_one(arr):
    if not arr:
        return arr
        
    n = len(arr)
    temp = arr[0]
    for i in range(1, n):
        arr[i - 1] = arr[i]
    arr[n - 1] = temp
    
    return arr
```

---

## Test Cases
- **Normal Case**: 
  - Input: `arr = [1, 2, 3, 4, 5]`
  - Output: `[2, 3, 4, 5, 1]`
- **Hard Case**: 
  - Input: `arr = [5, 4, 3, 2, 1]`
  - Output: `[4, 3, 2, 1, 5]`
- **Edge Case**: 
  - Input: `arr = [10]`
  - Output: `[10]`

---

## Common Mistakes
- Overwriting `arr[0]` before saving it to a temporary variable.
- Off-by-one errors in loop boundaries, such as starting the loop from index 0 instead of 1, which overwrites elements with their own values or causes out-of-bound access.

---

## Killer Edge Cases
- Empty array.
- Single element array.
- Array with negative values.

---

## Follow-Up Variants
- **Left Rotate by One** $\rightarrow$ **Left Rotate by K Places**: Shift elements by $K$ positions instead of 1.
  - *Delta*: Reversing subsegments to achieve rotation in $O(N)$ time and $O(1)$ space.

---

## Similar Problems
- Right Rotate Array by One
- Rotate Array by K Places

---

## Theory Connections
- **Cyclic Shifts**: Left rotation corresponds to a cyclic permutation shift. In computer hardware, this is equivalent to a bitwise barrel shift or rotation instruction.

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

