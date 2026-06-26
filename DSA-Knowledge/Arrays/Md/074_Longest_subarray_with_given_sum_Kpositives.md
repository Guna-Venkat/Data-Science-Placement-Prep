# Longest subarray with given sum K positives

## Difficulty
Easy/Medium

---

## Pattern
Sliding Window / Two Pointers

---

## Recognition Clues
- Find a contiguous subarray whose sum is exactly $K$.
- The input array contains only positive numbers (or non-negative numbers).
- The goal is to maximize the length of the subarray.

---

## Core Insight
- Because all elements are positive, the running sum is strictly monotonic: expanding the right boundary increases the sum, and contracting the left boundary decreases the sum.
- We can maintain a sliding window `[left, right]` where we adjust the boundaries based on whether the current sum is less than, equal to, or greater than $K$.

---

## Interview Explanation
1. **Brute Force Idea**: Generate all possible subarrays using two nested loops. Calculate the sum of each subarray. If the sum is equal to $K$, update our maximum length with the length of that subarray.
2. **Why Inefficient**: Computing the sum of all subarrays takes $O(N^2)$ time, which is too slow for large inputs.
3. **Key Observation**: If the sum of the current window `[left, right]` exceeds $K$, any larger window `[left, right + x]` will also exceed $K$ (since all numbers are positive). Thus, we can safely advance `left` to shrink the sum.
4. **Optimal Solution Intuition**: 
   - Initialize `left = 0`, `right = 0`, `curr_sum = 0`, and `max_len = 0`.
   - Expand the window by adding `arr[right]` to `curr_sum`.
   - If `curr_sum > k`, contract the window from the left by subtracting `arr[left]` and incrementing `left` until `curr_sum <= k`.
   - If `curr_sum == k`, update `max_len = max(max_len, right - left + 1)`.
   - Repeat until `right` reaches the end of the array.
5. **Time Complexity**: $O(N)$ because both the `left` and `right` pointers traverse the array at most once.
6. **Space Complexity**: $O(1)$ auxiliary space since we only store pointer positions and sums.

---

## Brute Force
- **Idea**: Try all subarrays and calculate their sum.
- **Code**:
```python
def longest_subarray_sum_k_positives_brute(arr, k):
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
- **Algorithm**: Sliding Window / Two Pointers.
  1. Initialize `left = 0`, `right = 0`, `curr_sum = 0`, and `max_len = 0`.
  2. While `right < len(arr)`:
     - Add `arr[right]` to `curr_sum`.
     - While `curr_sum > k` and `left <= right`:
       - Subtract `arr[left]` from `curr_sum` and increment `left`.
     - If `curr_sum == k`, update `max_len = max(max_len, right - left + 1)`.
     - Increment `right`.
  3. Return `max_len`.
- **Why it works**: The monotonicity of prefix sums of positive numbers ensures that we do not miss any valid window by advancing `left` when the sum is too large.
- **Complexity**: Time: $O(N)$, Space: $O(1)$.

---

## Optimal Code
```python
def longestSubarrayWithSumK(a, k):
    left, right = 0, 0
    curr_sum = 0
    max_len = 0
    n = len(a)
    
    while right < n:
        curr_sum += a[right]
        
        # Shrink window if sum exceeds target
        while curr_sum > k and left <= right:
            curr_sum -= a[left]
            left += 1
            
        # Check if window meets target
        if curr_sum == k:
            max_len = max(max_len, right - left + 1)
            
        right += 1
        
    return max_len
```

---

## Test Cases
- **Normal Case**: 
  - Input: `a = [1, 2, 3, 1, 1, 1, 1]`, `k = 3`
  - Output: `3` (subarray `[1, 1, 1]` from index 3 to 5)
- **Hard Case**: 
  - Input: `a = [2, 2, 2]`, `k = 5`
  - Output: `0` (no subarray sums to 5)
- **Edge Case**: 
  - Input: `a = [5]`, `k = 5`
  - Output: `1`

---

## Common Mistakes
- **Applying this sliding window approach to arrays containing negative numbers**. If the array contains negative numbers, the prefix sums are not monotonic, and shrinking from the left is no longer correct. You must use the prefix-sum hash map approach instead.
- Incorrect contraction condition (e.g. contracting when `curr_sum >= k` instead of strictly `curr_sum > k`).

---

## Killer Edge Cases
- Array contains zero values (`[1, 0, 0, 2]`, `k=3` -> should return `4` for `[1, 0, 0, 2]`).
- All elements are greater than $K$.
- Target $K$ is not present.

---

## Follow-Up Variants
- **Longest Subarray with Sum K (Positives)** $\rightarrow$ **Longest Subarray with Sum K (Positives & Negatives)**: Find the maximum length when the array can contain negative integers.
  - *Delta*: Sliding window fails. Use a hash map to store `prefix_sum -> index` pairs and find `current_sum - K` in the map.

---

## Similar Problems
- Subarray Sum Equals K (LeetCode 560)
- Minimum Size Subarray Sum (LeetCode 209)

---

## Theory Connections
- **Monotonicity**: The sliding window technique is valid when there is a monotonic relationship between the size of the window and the property being measured (the sum). This is mathematically analogous to Two-Pointer searches on sorted arrays.

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

