# Kadanes Algorithm

## Difficulty
Medium

---

## Pattern
Dynamic Programming / Greedy

---

## Recognition Clues
- Find a contiguous subarray (containing at least one number) which has the largest sum.
- Requires finding the sum or boundaries in $O(N)$ time and $O(1)$ space.

---

## Core Insight
- A negative running sum will always decrease the sum of any subsequent subarray.
- Therefore, as we scan the array, we accumulate the elements into a running sum `curr_sum`. If `curr_sum` drops below zero, we reset it to zero and begin a new subarray candidate starting at the next element.

---

## Interview Explanation
1. **Brute Force Idea**: Generate all possible subarrays using two nested loops. For each subarray, calculate its sum. Track the maximum sum found across all subarrays and return it.
2. **Why Inefficient**: Checking all subarrays takes $O(N^2)$ time, which is too slow for large input sizes.
3. **Key Observation**: We don't need to rebuild the sum for each subarray. If the running sum ending at index $i-1$ is positive, it can contribute to a larger sum at index $i$. If it is negative, it will only drag down the value, so we should discard it.
4. **Optimal Solution Intuition (Kadane's)**:
   - Initialize `max_sum = nums[0]` (never initialize to 0, because the array could consist of all negative numbers).
   - Initialize `curr_sum = 0`.
   - Iterate through the array:
     - Add `num` to `curr_sum`.
     - Update `max_sum = max(max_sum, curr_sum)`.
     - If `curr_sum` falls below 0, reset `curr_sum = 0`.
5. **Time Complexity**: $O(N)$ since we perform a single linear pass.
6. **Space Complexity**: $O(1)$ auxiliary space since we only store two scalar values.

---

## Brute Force
- **Idea**: Check all subarrays and calculate their sums.
- **Code**:
```python
def max_subarray_brute(nums):
    max_sum = float('-inf')
    n = len(nums)
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum
```
- **TC**: $O(N^2)$
- **SC**: $O(1)$

---

## Optimal Approach
- **Algorithm**: Kadane's Algorithm.
  1. Initialize `max_sum = nums[0]` and `curr_sum = 0`.
  2. For `num` in `nums`:
     - `curr_sum += num`
     - Update `max_sum = max(max_sum, curr_sum)`.
     - If `curr_sum < 0`, reset `curr_sum = 0`.
  3. Return `max_sum`.
- **Why it works**: At each index, we make a local greedy choice: either add the current element to the preceding running sum or start a new sequence at the current element.
- **Complexity**: Time: $O(N)$, Space: $O(1)$.

---

## Optimal Code
```python
def maxSubArray(nums):
    max_sum = nums[0]
    curr_sum = 0
    
    for num in nums:
        curr_sum += num
        # Update max_sum BEFORE resetting curr_sum to handle all-negative arrays
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
            
    return max_sum
```

---

## Test Cases
- **Normal Case**: 
  - Input: `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`
  - Output: `6` (subarray is `[4, -1, 2, 1]`)
- **Hard Case**: 
  - Input: `nums = [-5, -2, -8, -1, -3]`
  - Output: `-1` (subarray is `[-1]`)
- **Edge Case**: 
  - Input: `nums = [1]`
  - Output: `1`

---

## Common Mistakes
- **Initializing `max_sum = 0`**: If all elements are negative (e.g. `[-5, -3]`), the correct maximum is `-3`. Initializing to 0 would return 0, which is incorrect.
- **Resetting `curr_sum` before updating `max_sum`**: If the array is `[-1]`, resetting first would set `curr_sum` to 0, and `max_sum` would be compared against 0 instead of `-1`.

---

## Killer Edge Cases
- All elements are negative numbers.
- Array contains only 1 element.
- Mixed negative and positive numbers with large negative drops.

---

## Follow-Up Variants
- **Kadane's (Find Max Sum)** $\rightarrow$ **Print Subarray with Max Sum**:
  - *Delta*: Track the starting and ending indices of the window when updating `max_sum`.

---

## Similar Problems
- Maximum Product Subarray (LeetCode 152)
- Maximum Sum Circular Subarray (LeetCode 918)

---

## Theory Connections
- **Dynamic Programming (State Reduction)**: Kadane's algorithm is formulated as a DP relation: $dp[i] = \max(nums[i], dp[i-1] + nums[i])$, where $dp[i]$ is the max sum ending at index $i$. Since computing $dp[i]$ only requires $dp[i-1]$, we can reduce the space complexity from $O(N)$ to $O(1)$ by using a single variable.

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

