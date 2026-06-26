# Longest subarray with sum K

## Difficulty
Medium

---

## Pattern
Hashing / Prefix Sum

---

## Recognition Clues
- Find a contiguous subarray whose sum is exactly $K$.
- Array can contain both positive, negative, and zero values.
- Goal is to maximize the length of the subarray.

---

## Core Insight
- Since negative numbers are present, the running sum is no longer monotonic, rendering the sliding window approach incorrect.
- Let the prefix sum up to index $i$ be $S_i$. A subarray from index $j+1$ to $i$ has a sum of $S_i - S_j$. If this sum equals $K$, then $S_j = S_i - K$.
- We can scan the array and store the first occurrence of each prefix sum $S_j$ in a hash map. By looking up $S_i - K$, we can find the earliest index $j$ that satisfies the condition, thereby maximizing the length $i - j$.

---

## Interview Explanation
1. **Brute Force Idea**: Generate all possible subarrays using two nested loops. Calculate the sum of each subarray. If it equals $K$, check if its length is greater than the current maximum and update it.
2. **Why Inefficient**: Computing all subarray sums takes $O(N^2)$ time, which is too slow for large arrays.
3. **Key Observation**: If we know the prefix sum at the current index is `curr_sum`, we want to find if there is a previous prefix sum equal to `curr_sum - K`. To maximize the length of the subarray, we want to find the *earliest* index where `curr_sum - K` occurred.
4. **Optimal Solution Intuition**: 
   - Maintain a running prefix sum `curr_sum` and a hash map `pre_map` to store `prefix_sum -> first_index` mappings.
   - For each index $i$, update `curr_sum += arr[i]`.
   - If `curr_sum == K`, we found a valid subarray starting from index 0, so `max_len = max(max_len, i + 1)`.
   - If `curr_sum - K` exists in `pre_map`, a valid subarray exists from `pre_map[curr_sum - K] + 1` to $i$. Update `max_len = max(max_len, i - pre_map[curr_sum - K])`.
   - If `curr_sum` is not already in `pre_map`, insert it: `pre_map[curr_sum] = i`. (Do not update if it already exists, as we want to keep the earliest index).
5. **Time Complexity**: $O(N)$ because hash map insertions and lookups take $O(1)$ average time.
6. **Space Complexity**: $O(N)$ to store prefix sums in the hash map.

---

## Brute Force
- **Idea**: Check all subarrays and calculate their sum.
- **Code**:
```python
def longest_subarray_sum_k_brute(arr, k):
    max_len = 0
    n = len(arr)
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum == k:
                max_len = max(max_len, j - i + 1)
    return max_len
```
- **TC**: $O(N^2)$
- **SC**: $O(1)$

---

## Optimal Approach
- **Algorithm**: Prefix Sum with Hashing.
  1. Initialize `pre_map = {}`, `curr_sum = 0`, and `max_len = 0`.
  2. For $i$ from $0$ to $N-1$:
     - `curr_sum += arr[i]`
     - If `curr_sum == k`, update `max_len = max(max_len, i + 1)`.
     - Set `rem = curr_sum - k`.
     - If `rem` is in `pre_map`, update `max_len = max(max_len, i - pre_map[rem])`.
     - If `curr_sum` is not in `pre_map`, set `pre_map[curr_sum] = i`.
  3. Return `max_len`.
- **Why it works**: By storing only the first occurrence of each prefix sum, we guarantee that the distance `i - pre_map[curr_sum - k]` is maximized.
- **Complexity**: Time: $O(N)$, Space: $O(N)$.

---

## Optimal Code
```python
def longestSubarray(arr, k):
    pre_map = {}
    curr_sum = 0
    max_len = 0
    
    for i in range(len(arr)):
        curr_sum += arr[i]
        
        # Check if subarray from index 0 to i sums to k
        if curr_sum == k:
            max_len = max(max_len, i + 1)
            
        rem = curr_sum - k
        # If rem has occurred before, a subarray sums to k
        if rem in pre_map:
            max_len = max(max_len, i - pre_map[rem])
            
        # Store prefix sum only if it hasn't occurred before
        if curr_sum not in pre_map:
            pre_map[curr_sum] = i
            
    return max_len
```

---

## Test Cases
- **Normal Case**: 
  - Input: `arr = [10, 5, 2, 7, 1, 9]`, `k = 15`
  - Output: `4` (subarray `[5, 2, 7, 1]`)
- **Hard Case**: 
  - Input: `arr = [1, -1, 5, -2, 3]`, `k = 3`
  - Output: `4` (subarray `[1, -1, 5, -2]`)
- **Edge Case**: 
  - Input: `arr = [-5]`, `k = -5`
  - Output: `1`

---

## Common Mistakes
- **Overwriting prefix sum indices in the hash map**. If `curr_sum` already exists in `pre_map`, do not update its index. Updating it moves the index forward, which minimizes the subarray length.
- Failing to check if `curr_sum == k` explicitly (or initializing the map with `{0: -1}`).

---

## Killer Edge Cases
- Array contains negative numbers, positive numbers, and zeros.
- Subarray sum equal to $K$ starts at index 0.
- No subarray sums to $K$.

---

## Follow-Up Variants
- **Longest Subarray with Sum K** $\rightarrow$ **Count Subarrays with Sum K**: Count the total number of subarrays whose sum is $K$.
  - *Delta*: Store the *frequency* of each prefix sum in the hash map instead of the index, and add the frequency of `curr_sum - K` to a running count at each step.

---

## Similar Problems
- Subarray Sum Equals K (LeetCode 560)
- Subarray Sums Divisible by K (LeetCode 974)

---

## Theory Connections
- **Prefix Sum Reduction**: Translates range sum query checks from $O(N)$ to $O(1)$ space-time. Combining prefix sums with hashing is a standard pattern for solving exact range constraint problems on array-like sequences in linear time.

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

