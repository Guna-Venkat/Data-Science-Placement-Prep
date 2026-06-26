# Check if the Array is Sorted II (Sorted and Rotated)

## Difficulty
Easy

---

## Pattern
Iterative / Circular Array Property

---

## Recognition Clues
- The problem asks if a given array was originally sorted in non-decreasing order and then rotated by some offset.
- Involves circular relationships where the last element connects back to the first.

---

## Core Insight
- A sorted array contains no "drops" (where an element is greater than the next). 
- If a sorted array is rotated, it will introduce exactly one drop at the point of rotation. 
- Therefore, a circular check of the array must reveal at most one index $i$ such that `arr[i] > arr[(i + 1) % N]`.

---

## Interview Explanation
1. **Brute Force Idea**: Generate all $N$ possible rotations of the array. For each rotation, perform a linear check to see if the elements are in non-decreasing order. If any rotation is sorted, return `True`.
2. **Why Inefficient**: Generating and checking each rotation takes $O(N)$ time. Since there are $N$ rotations, the total time complexity is $O(N^2)$, which is suboptimal.
3. **Key Observation**: If we treat the array as circular, there can be at most one point where the sequence decreases (the "pivot" or "rotation drop"). If there are more than two decreases, it cannot be a single rotated sorted array.
4. **Optimal Solution Intuition**: Loop through the array from $0$ to $N-1$ and check if `nums[i] > nums[(i + 1) % N]`. Count how many times this condition is met. If the count is $\le 1$, return `True`, else `False`.
5. **Time Complexity**: $O(N)$ because we make a single pass through the array.
6. **Space Complexity**: $O(1)$ because we only store a single counter variable.

---

## Brute Force
- **Idea**: Perform all $N$ circular rotations and check if any rotation results in a sorted array.
- **Code**:
```python
def check_sorted_rotated_brute(nums):
    n = len(nums)
    for k in range(n):
        rotated = nums[k:] + nums[:k]
        is_sorted = True
        for i in range(n - 1):
            if rotated[i] > rotated[i + 1]:
                is_sorted = False
                break
        if is_sorted:
            return True
    return False
```
- **TC**: $O(N^2)$
- **SC**: $O(N)$ to store the rotated array.

---

## Optimal Approach
- **Algorithm**: 
  1. Initialize `count = 0` and get the length $N$.
  2. Iterate $i$ from $0$ to $N-1$.
  3. If `nums[i] > nums[(i + 1) % N]`, increment `count`.
  4. If `count > 1`, return `False` immediately.
  5. Return `True` after completing the loop.
- **Why it works**: A sorted array has 0 drops. A sorted and rotated array has exactly 1 drop (where the largest element wraps around to the smallest). If there are $\ge 2$ drops, the array is out of order.
- **Complexity**: Time: $O(N)$, Space: $O(1)$.

---

## Optimal Code
```python
def check(nums):
    count = 0
    n = len(nums)
    
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count += 1
            if count > 1:
                return False
                
    return True
```

---

## Test Cases
- **Normal Case**: 
  - Input: `nums = [3, 4, 5, 1, 2]`
  - Output: `True` (exactly one drop: 5 -> 1)
- **Hard Case**: 
  - Input: `nums = [2, 1, 3, 4]`
  - Output: `False` (two drops: 2 -> 1, and 4 -> 2 circularly)
- **Edge Case**: 
  - Input: `nums = [1, 1, 1]`
  - Output: `True` (zero drops)

---

## Common Mistakes
- Forgetting to check the wrap-around case between the last element and the first element (`nums[n-1]` and `nums[0]`).
- Using strictly greater than (`>`) or greater than or equal to (`>=`) incorrectly when handling duplicate elements.

---

## Killer Edge Cases
- All elements in the array are identical.
- Array is already sorted and not rotated (0 drops).
- Single element array.

---

## Follow-Up Variants
- **Check Sorted & Rotated** $\rightarrow$ **Search in Rotated Sorted Array**: Find the index of a target element in a rotated sorted array using binary search.

---

## Similar Problems
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array

---

## Theory Connections
- **Circular Arrays**: Simulates a ring buffer structure using modular arithmetic, mapping a linear coordinate space $[0, N-1]$ to a topology without boundaries.

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

