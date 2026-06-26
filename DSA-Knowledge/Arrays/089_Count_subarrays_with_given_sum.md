# Count subarrays with given sum

## Difficulty
Medium

---

## Pattern
Prefix Sum / Hashing (Frequency)

---

## Recognition Clues
- Count total number of contiguous subarrays whose sum equals $K$.\n- Array contains positive, negative, and zero values.

---

## Core Insight
- Let prefix sum up to index $i$ be $S_i$. We want to find index pairs $(j, i)$ where $S_i - S_j = K$, which means $S_j = S_i - K$.\n- We can scan the array and maintain the running frequencies of prefix sums in a Hash Map.\n- At each step, add the frequency of `curr_sum - K` to our count.

---

## Interview Explanation
1. **Brute Force Idea**: Generate all possible subarrays using two nested loops. Calculate the sum of each subarray. If it equals $K$, increment our count.
2. **Why Inefficient**: Computing all sums takes $O(N^2)$ time.
3. **Key Observation**: If the cumulative sum at index $i$ is `curr_sum`, and some previous cumulative sum at index $j$ was `curr_sum - K`, the subarray sum in between is exactly $K$. We can look up the count of such previous indices in $O(1)$ time if we store prefix sum frequencies in a hash map.
4. **Optimal Solution Intuition**:
   - Initialize a hash map `pre_map` with `{0: 1}` (meaning a prefix sum of 0 has occurred once, representing a subarray starting from index 0).
   - Maintain a running prefix sum `curr_sum` and `count = 0`.
   - Iterate through the array. For each element:
     - Add it to `curr_sum`.
     - Add `pre_map[curr_sum - K]` to `count` if it exists in the map.
     - Update `pre_map[curr_sum] = pre_map.get(curr_sum, 0) + 1`.
5. **Time Complexity**: $O(N)$ (single pass).
6. **Space Complexity**: $O(N)$ to store prefix sums in the map.

---

## Brute Force
- **Idea**: Generate all subarrays and count those that sum to $K$.
- **Code**:
```python
def subarraySum_brute(nums, k):
    count = 0
    n = len(nums)
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum == k:
                count += 1
    return count
```
- **TC**: $O(N^2)$
- **SC**: $O(1)$

---

## Optimal Approach
- **Algorithm**: Prefix sum tracking with frequency hashing.
- **Why it works**: Storing prefix sum frequencies allows us to count all valid left-hand bounds for the current subarray in $O(1)$ time, optimizing range queries.
- **Complexity**: Time: $O(N)$, Space: $O(N)$.

---

## Optimal Code
```python
def subarraySum(nums, k):
    pre_map = {0: 1}  # Base case: sum of 0 seen 1 time
    curr_sum = 0
    count = 0
    
    for num in nums:
        curr_sum += num
        rem = curr_sum - k
        
        # If rem exists in map, add its frequency to count
        if rem in pre_map:
            count += pre_map[rem]
            
        # Update prefix sum frequency
        pre_map[curr_sum] = pre_map.get(curr_sum, 0) + 1
        
    return count
```

---

## Test Cases
- **Normal Case**: Input: `nums = [1, 1, 1]`, `k = 2`\n- Output: `2` (subarrays `[1, 1]` at index 0-1 and 1-2)
- **Hard Case**: Input: `nums = [3, 4, 7, 2, -3, 1, 4, 2]`, `k = 7`\n- Output: `4`
- **Edge Case**: Input: `nums = [1, -1, 0]`, `k = 0`\n- Output: `3` (subarrays `[1, -1]`, `[0]`, `[1, -1, 0]`)

---

## Common Mistakes
- Forgetting to initialize the hash map with `{0: 1}`, which misses subarrays starting at index 0.\n- Adding the current element to the map before checking `curr_sum - K` (causes problems when $K=0$ because it counts the current prefix sum as its own left-bound candidate).

---

## Killer Edge Cases
- Array contains negative numbers and zeros.\n- Target sum $K = 0$.\n- No subarrays sum to $K$.

---

## Follow-Up Variants
- Count Subarrays with Sum K $\rightarrow$ Longest Subarray with Sum K

---

## Similar Problems
- Subarray Sums Divisible by K\n- Path Sum III (Binary Tree)

---

## Theory Connections
- Range Sum Inversion: Using the relation $S[i...j] = S[j] - S[i-1]$ to express subarray queries as a difference of prefix elements, reducing interval problems to prefix problems.

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
