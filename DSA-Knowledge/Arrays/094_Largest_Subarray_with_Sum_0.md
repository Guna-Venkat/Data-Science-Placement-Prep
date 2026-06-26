# Largest Subarray with Sum 0

## Difficulty
Medium

---

## Pattern
Prefix Sum / Hashing (Index)

---

## Recognition Clues
- Find the length of the largest contiguous subarray with sum equal to 0.\n- Array can contain positive, negative, and zero values.

---

## Core Insight
- Let prefix sum up to index $i$ be $S_i$. If $S_i - S_j = 0$, then $S_i = S_j$.\n- We want to find duplicate prefix sums in the array.\n- By storing the first index of each prefix sum in a hash map, we can maximize the length $i - j$ when we find a match.

---

## Interview Explanation
1. **Brute Force Idea**: Check all possible subarrays using two nested loops. Compute their sums, and if the sum is 0, update the maximum length.
2. **Why Inefficient**: Takes $O(N^2)$ time.
3. **Key Observation**: If the cumulative sum at index $i$ is identical to the cumulative sum at index $j$, the sum of elements between $j+1$ and $i$ must be exactly 0. We can check this in $O(1)$ using a hash map.
4. **Optimal Solution Intuition**:
   - Maintain a running prefix sum `curr_sum` and a hash map `pre_map` mapping `prefix_sum -> first_index`.
   - Iterate through the array. For each element:
     - Add it to `curr_sum`.
     - If `curr_sum == 0`, the subarray from index 0 to $i$ has sum 0. Update `max_len = i + 1`.
     - If `curr_sum` is in `pre_map`, calculate the distance `i - pre_map[curr_sum]`, and update `max_len = max(max_len, distance)`.
     - Else, store `pre_map[curr_sum] = i`.
5. **Time Complexity**: $O(N)$ (single pass).
6. **Space Complexity**: $O(N)$ to store prefix sums in the map.

---

## Brute Force
- **Idea**: Verify sum of all possible subarrays.
- **Code**:
```python
def maxLen_brute(arr):
    max_len = 0
    n = len(arr)
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum == 0:
                max_len = max(max_len, j - i + 1)
    return max_len
```
- **TC**: $O(N^2)$
- **SC**: $O(1)$

---

## Optimal Approach
- **Algorithm**: First-occurrence hashing of prefix sums.
- **Why it works**: Equivalence of prefix sums implies the interval sum is zero; storing only the first occurrence maximizes the span.
- **Complexity**: Time: $O(N)$, Space: $O(N)$.

---

## Optimal Code
```python
def maxLen(arr):
    pre_map = {}
    curr_sum = 0
    max_len = 0
    
    for i in range(len(arr)):
        curr_sum += arr[i]
        
        # If sum is 0, subarray from 0 to i sums to 0
        if curr_sum == 0:
            max_len = i + 1
            
        # If prefix sum was seen before, update max_len
        if curr_sum in pre_map:
            max_len = max(max_len, i - pre_map[curr_sum])
        else:
            # Store only the first occurrence
            pre_map[curr_sum] = i
            
    return max_len
```

---

## Test Cases
- **Normal Case**: Input: `arr = [15, -2, 2, -8, 1, 7, 10, 23]`\n- Output: `5` (subarray `[-2, 2, -8, 1, 7]` from index 1 to 5)
- **Hard Case**: Input: `arr = [2, 8, -3, -5, 2, -4, 6, 1, 2, 1]`\n- Output: `8`
- **Edge Case**: Input: `arr = [1, 1, 1]`\n- Output: `0` (no subarray sums to 0)

---

## Common Mistakes
- Overwriting the index in the hash map when a prefix sum is encountered again. This minimizes the length instead of maximizing it.\n- Not handling the case where `curr_sum == 0` (or failing to initialize the map appropriately).

---

## Killer Edge Cases
- All elements are 0.\n- No subarrays sum to 0.\n- Subarray starts at index 0.

---

## Follow-Up Variants
- Largest Subarray with Sum 0 $\rightarrow$ Longest Subarray with Sum K

---

## Similar Problems
- Subarray Sum Equals K\n- Contiguous Array (LeetCode 525)

---

## Theory Connections
- Zero-Sum Intervals: Translates interval sum queries to coordinate collisions in the prefix space, solving range properties in $O(N)$ instead of $O(N^2)$ using hashtables.

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
