# Maximum Product Subarray in an Array

## Difficulty
Medium

---

## Pattern
Prefix/Suffix Running Product / Kadane's Variant

---

## Recognition Clues
- Find the contiguous subarray that has the largest product.\n- Array can contain positive, negative, and zero values.

---

## Core Insight
- If the array has no zeros and an even number of negative numbers, the max product is the product of all elements.\n- If there is an odd number of negative numbers, we must discard one negative number. This splits the array into a prefix product and a suffix product.\n- We can compute the running prefix product and running suffix product. If we hit a zero, we reset the running product back to 1.

---

## Interview Explanation
1. **Brute Force Idea**: Find all possible subarrays, calculate their products, and return the maximum.
2. **Why Inefficient**: Takes $O(N^2)$ time.
3. **Key Observation**: If we have an odd number of negatives, the optimal subarray must be either a prefix product (ending just before the last negative) or a suffix product (starting just after the first negative). Zeros split the array into independent subproblems. Thus, the maximum product subarray is always a prefix product or a suffix product of some zero-free segment.
4. **Optimal Solution Intuition**:
   - Set `max_prod = -infinity`.
   - Set `prefix = 1` and `suffix = 1`.
   - Loop `i` from 0 to $N-1$:
     - If `prefix == 0`, reset `prefix = 1` (zero boundary).
     - If `suffix == 0`, reset `suffix = 1`.
     - Update `prefix *= nums[i]` and `suffix *= nums[N - 1 - i]`.
     - Update `max_prod = max(max_prod, prefix, suffix)`.
5. **Time Complexity**: $O(N)$ (single pass).
6. **Space Complexity**: $O(1)$ auxiliary space.

---

## Brute Force
- **Idea**: Calculate product of all possible subarrays.
- **Code**:
```python
def maxProduct_brute(nums):
    max_prod = float('-inf')
    n = len(nums)
    for i in range(n):
        curr_prod = 1
        for j in range(i, n):
            curr_prod *= nums[j]
            max_prod = max(max_prod, curr_prod)
    return max_prod
```
- **TC**: $O(N^2)$
- **SC**: $O(1)$

---

## Optimal Approach
- **Algorithm**: Prefix and suffix scan with zero-resets.
- **Why it works**: The global maximum product must be bounded by array edges or zero elements, which simplifies candidates to prefix or suffix products.
- **Complexity**: Time: $O(N)$, Space: $O(1)$.

---

## Optimal Code
```python
def maxProduct(nums):
    max_prod = float('-inf')
    prefix = 1
    suffix = 1
    n = len(nums)
    
    for i in range(n):
        # Reset products if they hit zero
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
            
        prefix *= nums[i]
        suffix *= nums[n - 1 - i]
        
        max_prod = max(max_prod, prefix, suffix)
        
    return max_prod
```

---

## Test Cases
- **Normal Case**: Input: `nums = [2, 3, -2, 4]`\n- Output: `6` (subarray `[2, 3]`)
- **Hard Case**: Input: `nums = [-2, 0, -1]`\n- Output: `0` (since max is 0 or -1, wait: -2*0=0, -1*0=0, max is 0)
- **Edge Case**: Input: `nums = [-3]`\n- Output: `-3`

---

## Common Mistakes
- Failing to reset the prefix/suffix product to 1 when a 0 is encountered.\n- Initializing `max_prod = 0` which fails if the array has only negative numbers (e.g. `[-3]` where max product is `-3`).

---

## Killer Edge Cases
- Array contains only negative numbers.\n- Array contains zeros.\n- Single element array.

---

## Follow-Up Variants
- Max Product Subarray $\rightarrow$ Max Product Subarray with positive values only.

---

## Similar Problems
- Maximum Subarray\n- Product of Array Except Self

---

## Theory Connections
- State space reduction: This problem can also be solved using a Kadane-like DP where we track both `max_so_far` and `min_so_far` at each step (since a negative value times `min_so_far` can become the new `max_so_far`).

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
