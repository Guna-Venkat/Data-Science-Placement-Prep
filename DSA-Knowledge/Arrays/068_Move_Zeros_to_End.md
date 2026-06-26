# Move Zeros to End

## Difficulty
Easy

---

## Pattern
Two Pointers / Stable Partitioning

---

## Recognition Clues
- Group elements into two categories in-place (zero vs non-zero).
- Maintain the relative order of the non-zero elements (stability constraint).

---

## Core Insight
- Maintain a pointer `j` that points to the first zero element in the array (the write position). 
- Iterate through the array with a pointer `i`. Whenever `arr[i]` is non-zero, swap `arr[i]` and `arr[j]`, then increment `j`. This shifts non-zero elements left while dragging the zero boundary along.

---

## Interview Explanation
1. **Brute Force Idea**: Create an auxiliary array `temp`. Traverse the original array and copy all non-zero elements into `temp`. Count how many zeros were present, and append that many zeros to the end of `temp`. Finally, copy the elements of `temp` back into the original array.
2. **Why Inefficient**: Utilizing an auxiliary list requires $O(N)$ extra space, which is suboptimal because we can partition the array in-place.
3. **Key Observation**: If we use a pointer `j` to track the leftmost index holding a zero, any non-zero element found to its right at index `i` can be swapped with index `j`. Since `arr[j]` is zero, swapping puts the non-zero in the correct position and shifts the zero further right, preserving relative order.
4. **Optimal Solution Intuition**: 
   - First, run a quick scan to locate the index of the first zero and assign it to `j`. If no zero exists, the array is already correct, so return.
   - Loop `i` from `j + 1` to $N-1$. 
   - If `nums[i] != 0`, swap `nums[i]` and `nums[j]`, then increment `j` by 1.
5. **Time Complexity**: $O(N)$ since we perform at most two linear passes.
6. **Space Complexity**: $O(1)$ auxiliary space since elements are swapped in-place.

---

## Brute Force
- **Idea**: Extract non-zero elements to a list, pad the rest with zeros, and overwrite the original array.
- **Code**:
```python
def move_zeroes_brute(nums):
    temp = [x for x in nums if x != 0]
    zeros_count = len(nums) - len(temp)
    temp.extend([0] * zeros_count)
    for i in range(len(nums)):
        nums[i] = temp[i]
    return nums
```
- **TC**: $O(N)$
- **SC**: $O(N)$

---

## Optimal Approach
- **Algorithm**:
  1. Find the first occurrence of zero and store its index in `j`.
  2. If `j == -1`, return the array.
  3. Iterate `i` from `j + 1` to `len(nums) - 1`.
  4. If `nums[i] != 0`, swap `nums[i]` and `nums[j]`, and increment `j`.
- **Why it works**: `j` always points to a zero, and the elements before `j` are guaranteed to be non-zero and in their original order. Swapping `nums[i]` with `nums[j]` advances this boundary stably.
- **Complexity**: Time: $O(N)$, Space: $O(1)$.

---

## Optimal Code
```python
def moveZeroes(nums):
    j = -1
    n = len(nums)
    
    # 1. Find the first zero element
    for i in range(n):
        if nums[i] == 0:
            j = i
            break
            
    # If no zero is found, the array is already sorted
    if j == -1:
        return nums
        
    # 2. Swap non-zero elements with the zero at index j
    for i in range(j + 1, n):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
            
    return nums
```

---

## Test Cases
- **Normal Case**: 
  - Input: `nums = [0, 1, 0, 3, 12]`
  - Output: `[1, 3, 12, 0, 0]`
- **Hard Case**: 
  - Input: `nums = [0, 0, 0, 0, 1]`
  - Output: `[1, 0, 0, 0, 0]`
- **Edge Case**: 
  - Input: `nums = [0]`
  - Output: `[0]`

---

## Common Mistakes
- Using a two-pointer scheme that starts from both ends (e.g. `left` and `right` moving inwards). While this is in-place, it reverses or disrupts the relative order of non-zero elements, which violates the stability requirement.
- Forgetting to increment the write pointer `j` after swapping.

---

## Killer Edge Cases
- Array contains no zeros.
- Array contains only zeros.
- Array has zeros only at the end.

---

## Follow-Up Variants
- **Move Zeros to End** $\rightarrow$ **Move Zeros to Start**: Move all zeros to the beginning of the array.
  - *Delta*: Scan backwards from $N-1$ to $0$ and maintain `j` pointing to the first non-zero element from the right.

---

## Similar Problems
- Sort Colors (Sort 0s 1s 2s)
- Remove Element

---

## Theory Connections
- **Stable Partitioning**: This problem is a special case of stable partitioning. Stable partition algorithms are crucial in database queries and system sorting (like Timsort) where preserving the initial sequence of key-value pairs is required.

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

