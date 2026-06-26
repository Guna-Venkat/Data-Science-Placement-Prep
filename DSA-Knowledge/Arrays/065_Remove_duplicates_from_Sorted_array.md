# Remove duplicates from Sorted array

## Difficulty
Easy

---

## Pattern
Two Pointers / In-place Partitioning

---

## Recognition Clues
- Input array is already sorted.
- Requires in-place modification with $O(1)$ auxiliary space.
- Goal is to shift unique elements to the front and return the count of unique items.

---

## Core Insight
- Since the array is sorted, all duplicate elements are adjacent. 
- Use a `slow` pointer to track the position of the last placed unique element and a `fast` pointer to find the next unique element.

---

## Interview Explanation
1. **Brute Force Idea**: Iterate through the array and insert all elements into a hash set (or hash map) to filter duplicates. Sort the set elements (or read them if the set keeps order), and write them back into the array from index 0.
2. **Why Inefficient**: Using a hash set requires $O(N)$ extra memory, which violates the requirement of $O(1)$ auxiliary space.
3. **Key Observation**: Because the array is sorted, we can check if `arr[fast]` is a duplicate of the last unique element simply by comparing it to `arr[slow]`.
4. **Optimal Solution Intuition**: Initialize a `slow` pointer at index 0. Iterate `fast` from index 1 to $N-1$. Whenever `arr[fast]` differs from `arr[slow]`, we increment `slow` and copy `arr[fast]` to `arr[slow]`. At the end, the number of unique elements is `slow + 1`.
5. **Time Complexity**: $O(N)$ because the `fast` pointer scans the array exactly once.
6. **Space Complexity**: $O(1)$ because we only use two pointers.

---

## Brute Force
- **Idea**: Insert elements into a set, sort them (to preserve order), and write back to the array.
- **Code**:
```python
def remove_duplicates_brute(nums):
    unique_elements = sorted(list(set(nums)))
    for i in range(len(unique_elements)):
        nums[i] = unique_elements[i]
    return len(unique_elements)
```
- **TC**: $O(N \log N)$ due to sorting the unique list.
- **SC**: $O(N)$ to store elements in the set and list.

---

## Optimal Approach
- **Algorithm**: 
  1. Handle the empty array boundary case.
  2. Set `slow = 0`.
  3. Iterate `fast` from `1` to `len(nums) - 1`.
  4. If `nums[fast] != nums[slow]`, increment `slow` and assign `nums[slow] = nums[fast]`.
  5. Return `slow + 1`.
- **Why it works**: The `slow` pointer acts as a boundary: elements at or before `slow` are guaranteed to be unique and sorted. The `fast` pointer scans forward to find new elements to add to this boundary.
- **Complexity**: Time: $O(N)$, Space: $O(1)$.

---

## Optimal Code
```python
def removeDuplicates(nums):
    if not nums:
        return 0
        
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
            
    return slow + 1
```

---

## Test Cases
- **Normal Case**: 
  - Input: `nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]`
  - Output: `5` (first 5 elements of `nums` become `[0, 1, 2, 3, 4]`)
- **Hard Case**: 
  - Input: `nums = [1, 1, 1, 1, 1]`
  - Output: `1` (first element is `[1]`)
- **Edge Case**: 
  - Input: `nums = [1]`
  - Output: `1`

---

## Common Mistakes
- Returning `slow` instead of `slow + 1` (which is the actual count of unique elements).
- Comparing `nums[fast]` with `nums[fast - 1]` instead of `nums[slow]`. While this identifies duplicates, it makes writing to the correct index harder.

---

## Killer Edge Cases
- Empty array.
- Array with all unique elements.
- Array with all identical elements.

---

## Follow-Up Variants
- **Remove Duplicates I** $\rightarrow$ **Remove Duplicates from Sorted Array II**: Allow duplicates to appear at most twice (LeetCode 80).
  - *Delta*: Compare `nums[fast]` with `nums[slow - 1]` instead of `nums[slow]`.

---

## Similar Problems
- Move Zeroes
- Remove Element

---

## Theory Connections
- **Two-Pointer Partitioning**: This technique is a variation of the partitioning scheme used in QuickSort (Lomuto Partition Scheme), where elements meeting a certain predicate are clustered at the beginning of the array.

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

