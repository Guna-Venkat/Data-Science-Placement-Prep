# Print subarray with maximum subarray sum

## Difficulty
Medium

---

## Pattern
Dynamic Programming / Greedy (Kadane's Variant)

---

## Recognition Clues
- Find contiguous subarray with largest sum.\n- Requires returning the actual subarray elements or boundaries, not just the sum value.

---

## Core Insight
- We modify Kadane's algorithm by tracking the window start and end pointers.\n- Whenever `curr_sum` is reset to 0, the next index is a potential new starting boundary.\n- Whenever `curr_sum` exceeds `max_sum`, we update the recorded best window coordinates.

---

## Interview Explanation
1. **Brute Force Idea**: Generate all possible subarrays using two nested loops. Find the sum of each subarray and track the maximum sum. Retain the start and end indices of the subarray that yields this maximum sum, and slice the array at the end.
2. **Why Inefficient**: Computing and slicing all subarrays takes $O(N^2)$ time, which is suboptimal.
3. **Key Observation**: We can find the starting and ending indices on the fly inside Kadane's algorithm by updating a sliding start index whenever the running sum becomes negative.
4. **Optimal Solution Intuition**: Keep a running `curr_sum` and `max_sum`. Also track `start = 0`, `end = 0`, and a temporary `temp_start = 0`. As we scan, if `curr_sum > max_sum`, update `max_sum = curr_sum`, `start = temp_start`, and `end = current_index`. If `curr_sum < 0`, reset `curr_sum = 0` and update `temp_start = current_index + 1`.
5. **Time Complexity**: $O(N)$ (single pass).
6. **Space Complexity**: $O(1)$ auxiliary space.

---

## Brute Force
- **Idea**: Check all subarrays and record the indices of the maximum sum.
- **Code**:
```python
def max_subarray_print_brute(nums):
    max_sum = float('-inf')
    start, end = 0, 0
    n = len(nums)
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum > max_sum:
                max_sum = curr_sum
                start, end = i, j
    return nums[start:end+1]
```
- **TC**: $O(N^2)$
- **SC**: $O(1)$

---

## Optimal Approach
- **Algorithm**: Modified Kadane's algorithm tracking index pointers.
- **Why it works**: We extend Kadane's greediness: when `curr_sum` goes negative, the prefix is useless, so we shift our temporary starting boundary forward.
- **Complexity**: Time: $O(N)$, Space: $O(1)$ auxiliary space.

---

## Optimal Code
```python
def maxSubArrayPrint(nums):
    if not nums:
        return []
        
    max_sum = nums[0]
    curr_sum = 0
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(len(nums)):
        curr_sum += nums[i]
        
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i
            
        if curr_sum < 0:
            curr_sum = 0
            temp_start = i + 1
            
    return nums[start:end+1]
```

---

## Test Cases
- **Normal Case**: Input: `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`\n- Output: `[4, -1, 2, 1]`
- **Hard Case**: Input: `nums = [-5, -2, -8, -1, -3]`\n- Output: `[-1]`
- **Edge Case**: Input: `nums = [42]`\n- Output: `[42]`

---

## Common Mistakes
- Resetting the starting index to `i` instead of `i + 1` when `curr_sum < 0`.\n- Not updating indices before resetting `curr_sum`.

---

## Killer Edge Cases
- All elements are negative.\n- Single element array.\n- Multiple distinct subarrays sharing the same maximum sum (returns the first one).

---

## Follow-Up Variants
- Print Subarray Max Sum $\rightarrow$ Circular Max Sum Subarray

---

## Similar Problems
- Maximum Subarray (Kadane's)\n- Maximum Sum Circular Subarray

---

## Theory Connections
- Dynamic Programming with back-pointers: standard technique in sequence alignment and parsing algorithms to reconstruct the optimal path from computed scores.

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
