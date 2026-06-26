# Next Permutation

## Difficulty
Medium

---

## Pattern
Vector Logic / Array Manipulation

---

## Recognition Clues
- Rearrange numbers into the lexicographically next greater permutation.\n- If no such arrangement exists, rearrange to the lowest possible order (sorted ascending).\n- Must be in-place.

---

## Core Insight
- A decreasing suffix has no next permutation. The pivot we want to swap is the first element from the right that breaks this decreasing sequence.\n- Swap the pivot with the smallest element in the suffix that is strictly greater than the pivot.\n- Reverse the suffix to make it sorted ascending (minimizing the next permutation's value).

---

## Interview Explanation
1. **Brute Force Idea**: Generate all permutations, sort them, find the current one, and return the next in the list.
2. **Why Inefficient**: Generating all permutations takes $O(N! \cdot N)$ time.
3. **Key Observation**: Permutations increase when digits to the right are swapped. To find the *smallest* increase, we should work from the right.
4. **Optimal Solution Intuition**:
   - Step 1: Find the first pair from the right where `nums[i] < nums[i+1]` (let this be index `pivot`). If no pivot exists, the array is decreasing. Reverse the entire array and return.
   - Step 2: Find the largest index `j > pivot` such that `nums[j] > nums[pivot]`. Swap `nums[pivot]` and `nums[j]`.
   - Step 3: Reverse the suffix starting at `pivot + 1` to sort it in ascending order.
5. **Time Complexity**: $O(N)$ (a few linear scans).
6. **Space Complexity**: $O(1)$ in-place.

---

## Brute Force
- **Idea**: Generate all permutations, sort them, and select the next one.
- **Code**:
```python
# Not feasible in normal time limits due to O(N! * N) complexity.
```
- **TC**: $O(N! \cdot N)$
- **SC**: $O(N! \cdot N)$

---

## Optimal Approach
- **Algorithm**: Single-pass pivot analysis.
- **Why it works**: Locating the rightmost ascending transition pinpoints where the swap can yield the next lexicographical state with minimal delta.
- **Complexity**: Time: $O(N)$, Space: $O(1)$.

---

## Optimal Code
```python
def nextPermutation(nums):
    n = len(nums)
    i = n - 2
    
    # 1. Find the first decreasing element from the right
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
        
    if i >= 0:
        # 2. Find the element just larger than nums[i] to swap with
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        
    # 3. Reverse the suffix to make it lexicographically smallest
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
```

---

## Test Cases
- **Normal Case**: Input: `nums = [1, 2, 3]`\n- Output: `[1, 3, 2]`
- **Hard Case**: Input: `nums = [3, 2, 1]`\n- Output: `[1, 2, 3]`
- **Edge Case**: Input: `nums = [1, 1, 5]`\n- Output: `[1, 5, 1]`

---

## Common Mistakes
- Forgetting to check the condition `nums[j] <= nums[i]` (using `<` instead, which fails for duplicates).\n- Reversing the wrong suffix index range (should be `i+1` to end).

---

## Killer Edge Cases
- Array is sorted descending (largest permutation).\n- Array contains duplicate values.\n- Single element array.

---

## Follow-Up Variants
- Next Permutation $\rightarrow$ Previous Permutation

---

## Similar Problems
- Permutations\n- Next Greater Element

---

## Theory Connections
- Lexicographical Ordering: Maps discrete combinatorial structures to a totally ordered set. The pivot-finding method is based on Narayana Pandita's algorithm from 14th century India.

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
