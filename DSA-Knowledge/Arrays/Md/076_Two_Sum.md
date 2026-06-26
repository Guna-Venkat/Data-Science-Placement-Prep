# Two Sum

## Difficulty
Easy

---

## Pattern
Hashing / Two Pointers

---

## Recognition Clues
- Find two numbers in an array that add up to a specific target value.
- Return either the indices of the two numbers or a boolean indicating if such a pair exists.

---

## Core Insight
- For the index-retrieval variant, we can trade space for time by using a Hash Map. For each element $X$ at index $i$, we check if its complement $Y = \text{target} - X$ exists in our map. If it does, we return $[index(Y), i]$.
- For the boolean YES/NO variant (or if the array is already sorted), we can sort the array and use a Two-Pointer approach from both ends, achieving $O(1)$ auxiliary space.

---

## Interview Explanation
1. **Brute Force Idea**: Use two nested loops to check all possible pairs of elements. If the sum of `nums[i]` and `nums[j]` (where $i \ne j$) equals the target, return their indices.
2. **Why Inefficient**: Checking all pairs takes $O(N^2)$ time, which is highly inefficient for large arrays.
3. **Key Observation**: If we are currently looking at element $X$, the only partner that can complete the sum to target is $Y = \text{target} - X$. Instead of scanning the entire array to find $Y$, we can look it up in $O(1)$ average time using a hash map containing elements visited so far.
4. **Optimal Solution Intuition (Hash Map)**:
   - Initialize an empty hash map `num_map` (mapping `number -> index`).
   - Iterate through the array. For each element `nums[i]`:
     - Calculate `complement = target - nums[i]`.
     - If `complement` is in `num_map`, we have found the pair. Return `[num_map[complement], i]`.
     - Otherwise, insert `nums[i]` with its index `i` into `num_map`.
5. **Time Complexity**: $O(N)$ because hash map insertions and lookups take $O(1)$ average time.
6. **Space Complexity**: $O(N)$ to store the array elements in the hash map.

---

## Brute Force
- **Idea**: Check every pair of elements.
- **Code**:
```python
def two_sum_brute(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
```
- **TC**: $O(N^2)$
- **SC**: $O(1)$

---

## Optimal Approach
- **Algorithm**: One-pass Hash Map.
  1. Initialize `num_map = {}`.
  2. For `i, num` in `enumerate(nums)`:
     - `complement = target - num`
     - If `complement` in `num_map`, return `[num_map[complement], i]`.
     - Else, store `num_map[num] = i`.
  3. Return `[]` if no pair is found.
- **Why it works**: A single pass guarantees that if a pair exists, the second element of the pair will find the first element (which has already been added to the map).
- **Complexity**: Time: $O(N)$, Space: $O(N)$.

---

## Optimal Code
```python
def twoSum(nums, target):
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        # If complement exists in map, return indices
        if complement in num_map:
            return [num_map[complement], i]
        # Store index of current number
        num_map[num] = i
        
    return []
```

---

## Test Cases
- **Normal Case**: 
  - Input: `nums = [2, 7, 11, 15]`, `target = 9`
  - Output: `[0, 1]`
- **Hard Case**: 
  - Input: `nums = [3, 2, 4]`, `target = 6`
  - Output: `[1, 2]`
- **Edge Case**: 
  - Input: `nums = [3, 3]`, `target = 6`
  - Output: `[0, 1]`

---

## Common Mistakes
- **Using the same element twice**: If `nums = [3, 2, 4]` and `target = 6`, returning `[0, 0]` because $3 + 3 = 6$ (but index 0 cannot be used twice).
- **Sorting the array first when index positions must be returned**: Sorting changes element indices. If you must sort, you must maintain index-value pairs.

---

## Killer Edge Cases
- Array contains duplicate values that add up to target (e.g. `[3, 3]`, target 6).
- Negative values inside the array or a negative target sum.
- Multiple pairs sum to target (only first pair needs to be returned).

---

## Follow-Up Variants
- **Two Sum (Unsorted, Return Indices)** $\rightarrow$ **Two Sum II (Sorted, Return 1-based Indices)**:
  - *Delta*: Avoid Hash Map. Initialize `left = 0` and `right = N-1`. If `nums[left] + nums[right] == target`, return. If sum is smaller, `left += 1`. If larger, `right -= 1`. Space drops to $O(1)$.
- **Two Sum** $\rightarrow$ **3 Sum**: Find all unique triplets that sum to 0.

---

## Similar Problems
- Two Sum II - Input Array Is Sorted (LeetCode 167)
- 3 Sum (LeetCode 15)
- 4 Sum (LeetCode 18)

---

## Theory Connections
- **Hash Table Efficiency**: Demonstrates the classic time-space trade-off. We reduce search time from $O(N^2)$ to $O(N)$ at the expense of $O(N)$ memory. Hash tables resolve search operations in amortized $O(1)$ time by mapping keys to array buckets using hash functions.

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

