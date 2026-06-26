# Longest Consecutive Sequence in an Array

## Difficulty
Medium

---

## Pattern
Hashing / Set Lookup

---

## Recognition Clues
- Find the length of the longest consecutive elements sequence.\n- The sequence does not need to be contiguous in the original array.\n- Must run in $O(N)$ time.

---

## Core Insight
- Sorting takes $O(N \log N)$ which violates the $O(N)$ constraint.\n- If we store all elements in a Hash Set, we can check for elements in $O(1)$ time.\n- To avoid redundant checks, only start building a consecutive sequence if the current number is the absolute start of a sequence (i.e. `num - 1` is not in the set).

---

## Interview Explanation
1. **Brute Force Idea**: Sort the array. Traverse the sorted array and count the length of the longest consecutive sequence by checking if `arr[i] == arr[i-1] + 1`.
2. **Why Inefficient**: Sorting takes $O(N \log N)$ time, which is slower than the requested $O(N)$ limit.
3. **Key Observation**: We can check if `num` is the start of a sequence in $O(1)$ time by verifying if `num - 1` is absent in a hash set of the numbers. If it is absent, we increment `num` iteratively to find the sequence length.
4. **Optimal Solution Intuition**:
   - Convert the array into a hash set `num_set`.
   - Iterate through the elements of `num_set` (to skip duplicate checks).
   - For each `num`, check if `num - 1` is in `num_set`. If it is *not*, it means `num` is the starting element of a consecutive sequence.
   - Increment `curr_num` and count consecutive elements (`curr_num + 1`, `curr_num + 2`, ...) present in the set.
   - Track the maximum length found.
5. **Time Complexity**: $O(N)$ because each element is visited at most twice (once during iteration and once inside the sequence-building loop).
6. **Space Complexity**: $O(N)$ to store elements in the hash set.

---

## Brute Force
- **Idea**: Sort the array and find the longest consecutive segment.
- **Code**:
```python
def longestConsecutive_brute(nums):
    if not nums:
        return 0
    nums.sort()
    longest = 1
    curr = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            curr += 1
        elif nums[i] != nums[i-1]:
            longest = max(longest, curr)
            curr = 1
    return max(longest, curr)
```
- **TC**: $O(N \log N)$
- **SC**: $O(1)$

---

## Optimal Approach
- **Algorithm**: Set-based sequence building with start-element filtering.
- **Why it works**: Filtering on `num - 1 not in set` ensures that we only traverse each consecutive chain once, preventing $O(N^2)$ worst-case behavior on long chains.
- **Complexity**: Time: $O(N)$, Space: $O(N)$.

---

## Optimal Code
```python
def longestConsecutive(nums):
    num_set = set(nums)
    max_len = 0
    
    for num in num_set:
        # Check if num is the start of a sequence
        if num - 1 not in num_set:
            curr_num = num
            curr_len = 1
            
            # Count consecutive elements
            while curr_num + 1 in num_set:
                curr_num += 1
                curr_len += 1
                
            max_len = max(max_len, curr_len)
            
    return max_len
```

---

## Test Cases
- **Normal Case**: Input: `nums = [100, 4, 200, 1, 3, 2]`\n- Output: `4` (sequence is `[1, 2, 3, 4]`)
- **Hard Case**: Input: `nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]`\n- Output: `9` (sequence is `[0, 1, 2, 3, 4, 5, 6, 7, 8]`)
- **Edge Case**: Input: `nums = []`\n- Output: `0`

---

## Common Mistakes
- Checking sequences for every element without the `num - 1 not in set` filter, which degrades time complexity to $O(N^2)$ for sorted-like inputs.\n- Not handling empty input array.

---

## Killer Edge Cases
- Empty input array.\n- Array contains duplicate elements.\n- All elements are consecutive.

---

## Follow-Up Variants
- Longest Consecutive Sequence $\rightarrow$ Longest Consecutive Sequence in Binary Tree

---

## Similar Problems
- Longest Consecutive Sequence\n- Find All Numbers Disappeared in an Array

---

## Theory Connections
- Disjoint Set Union (DSU) / Connected Components: This problem can also be modeled as finding the size of the largest connected component in a graph where edges exist between adjacent integer values.

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
