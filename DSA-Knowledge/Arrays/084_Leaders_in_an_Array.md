# Leaders in an Array

## Difficulty
Easy

---

## Pattern
Iterative / Right-to-Left Scan

---

## Recognition Clues
- Find all elements that are strictly greater than all elements to their right.\n- The last element is always a leader.

---

## Core Insight
- Checking from left to right requires $O(N)$ comparisons for each element.\n- By scanning from right to left, we can maintain a running maximum. Any element that is greater than or equal to this running maximum is a leader.

---

## Interview Explanation
1. **Brute Force Idea**: For each element, run an inner loop checking all elements to its right. If it is greater than all of them, it is a leader.
2. **Why Inefficient**: Two nested loops result in $O(N^2)$ time complexity.
3. **Key Observation**: If we scan from right to left, the leader criteria simplifies: an element is a leader if it is greater than the maximum of all elements encountered so far from the right.
4. **Optimal Solution Intuition**: Start at the last index. The last element is always a leader. Initialize `max_right = arr[-1]`. Iterate backwards from $N-2$ down to 0. If `arr[i] >= max_right`, then `arr[i]` is a leader; update `max_right = arr[i]`. Reverse the output list at the end to restore the original left-to-right order.
5. **Time Complexity**: $O(N)$.
6. **Space Complexity**: $O(1)$ auxiliary space.

---

## Brute Force
- **Idea**: For every element, check if all elements to its right are smaller.
- **Code**:
```python
def leaders_brute(arr):
    n = len(arr)
    ans = []
    for i in range(n):
        is_leader = True
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                is_leader = False
                break
        if is_leader:
            ans.append(arr[i])
    return ans
```
- **TC**: $O(N^2)$
- **SC**: $O(1)$

---

## Optimal Approach
- **Algorithm**: Right-to-left scan tracking running maximum.
- **Why it works**: Computing suffix maxima incrementally reduces the verification step at each index from a linear scan to a constant-time comparison.
- **Complexity**: Time: $O(N)$, Space: $O(1)$ auxiliary space.

---

## Optimal Code
```python
def leaders(arr):
    n = len(arr)
    if n == 0:
        return []
        
    max_right = arr[-1]
    ans = [max_right]
    
    # Scan from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] >= max_right:
            max_right = arr[i]
            ans.append(max_right)
            
    # Reverse to restore original left-to-right order
    return ans[::-1]
```

---

## Test Cases
- **Normal Case**: Input: `arr = [16, 17, 4, 3, 5, 2]`\n- Output: `[17, 5, 2]`
- **Hard Case**: Input: `arr = [1, 2, 3, 4, 5]`\n- Output: `[5]`
- **Edge Case**: Input: `arr = [5, 4, 3, 2, 1]`\n- Output: `[5, 4, 3, 2, 1]`

---

## Common Mistakes
- Forgetting to reverse the result list at the end.\n- Strict inequality vs non-strict inequality: checking if elements must be strictly greater than or greater-than-equal.

---

## Killer Edge Cases
- Array is in ascending order.\n- Array is in descending order.\n- Single element array.

---

## Follow-Up Variants
- Leaders in Array $\rightarrow$ Find rightmost elements (similar scanning logic).

---

## Similar Problems
- Next Greater Element\n- Monotonic Stack Problems

---

## Theory Connections
- Suffix Maxima: Precalculating prefix/suffix maxima/minima is a general technique to optimize range query lookups in static structures.

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
