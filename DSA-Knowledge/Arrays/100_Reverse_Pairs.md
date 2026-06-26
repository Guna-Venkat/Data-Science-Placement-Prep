# Reverse Pairs

## Difficulty
Hard

---

## Pattern
Merge Sort / Divide and Conquer

---

## Recognition Clues
- Count pairs $(i, j)$ such that $i < j$ and $arr[i] > 2 \cdot arr[j]$.\n- Requires $O(N \log N)$ time.

---

## Core Insight
- Similar to Count Inversions, we can count reverse pairs during the Merge Sort process.\n- However, because the condition is $arr[i] > 2 \cdot arr[j]$ (non-standard comparison), we must perform the count *before* merging the sorted halves.\n- For each element in the left half, we advance a pointer in the right half as long as the condition holds. This keeps count of valid pairs without repeating work.

---

## Interview Explanation
1. **Brute Force Idea**: Use two nested loops to check all pairs $(i, j)$ where $j > i$. If `nums[i] > 2 * nums[j]`, increment the count.
2. **Why Inefficient**: Takes $O(N^2)$ time.
3. **Key Observation**: If the left and right halves are sorted, we can count the pairs in linear time. For each index `i` in the left half, we move a pointer `j` in the right half to the right as long as `nums[i] > 2 * nums[j]`. The number of valid pairs for this `i` is `j - (mid + 1)`. Since both halves are sorted, `j` only moves forward, resulting in a two-pointer scan of $O(N)$.
4. **Optimal Solution Intuition**:
   - Use a Merge Sort divide-and-conquer skeleton.
   - In the merge helper, before merging, loop `i` from `left` to `mid`:
     - While `j <= right` and `nums[i] > 2 * nums[j]`, increment `j`.
     - Add `j - (mid + 1)` to the reverse pairs count.
   - After counting, perform the standard merge step to sort the array.
5. **Time Complexity**: $O(N \log N)$ (since the counting step is $O(N)$ and merging is $O(N)$).
6. **Space Complexity**: $O(N)$ for temporary array merge storage.

---

## Brute Force
- **Idea**: Compare all possible pairs.
- **Code**:
```python
def reversePairs_brute(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > 2 * nums[j]:
                count += 1
    return count
```
- **TC**: $O(N^2)$
- **SC**: $O(1)$

---

## Optimal Approach
- **Algorithm**: Merge Sort-based divide and conquer with pre-merge counting.
- **Why it works**: We must count pairs before sorting elements because merging scrambles the index ordering ($i < j$), but sorting is needed to keep the count step linear ($O(N)$).
- **Complexity**: Time: $O(N \log N)$, Space: $O(N)$ auxiliary space.

---

## Optimal Code
```python
def reversePairs(nums):
    def count_and_merge(left, mid, right):
        count = 0
        j = mid + 1
        
        # 1. Count reverse pairs before merging
        for i in range(left, mid + 1):
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            count += (j - (mid + 1))
            
        # 2. Standard merge step
        temp = []
        p1, p2 = left, mid + 1
        while p1 <= mid and p2 <= right:
            if nums[p1] <= nums[p2]:
                temp.append(nums[p1])
                p1 += 1
            else:
                temp.append(nums[p2])
                p2 += 1
                
        while p1 <= mid:
            temp.append(nums[p1])
            p1 += 1
        while p2 <= right:
            temp.append(nums[p2])
            p2 += 1
            
        # Write back sorted elements
        for idx in range(len(temp)):
            nums[left + idx] = temp[idx]
            
        return count

    def merge_sort(left, right):
        if left >= right:
            return 0
        mid = (left + right) // 2
        count = merge_sort(left, mid) + merge_sort(mid + 1, right)
        count += count_and_merge(left, mid, right)
        return count

    return merge_sort(0, len(nums) - 1)
```

---

## Test Cases
- **Normal Case**: Input: `nums = [1, 3, 2, 3, 1]`\n- Output: `2` (pairs: (3, 1) at indices 1-4 and 3-4)
- **Hard Case**: Input: `nums = [2, 4, 3, 5, 1]`\n- Output: `3` (pairs: (4,1), (3,1), (5,1))
- **Edge Case**: Input: `nums = [5, 4, 3, 2, 1]`\n- Output: `4`

---

## Common Mistakes
- Attempting to count and merge in a single pass (fails because the $arr[i] > 2 \cdot arr[j]$ condition is not transitive, unlike standard sorting comparisons).\n- Resetting pointer `j` to `mid + 1` for every `i`. (Not necessary and degrades complexity to $O(N^2)$ because since `nums[i]` increases, the threshold `2 * nums[j]` also increases, meaning `j` only moves forward).

---

## Killer Edge Cases
- Array contains negative numbers (where the inequality direction can be counter-intuitive).\n- Array is already sorted.\n- Values are very large (potential overflow when computing `2 * nums[j]` in languages with fixed-width integers).

---

## Follow-Up Variants
- Reverse Pairs $\rightarrow$ Count of Range Sum (LeetCode 327).

---

## Similar Problems
- Count Inversions\n- Count of Smaller Numbers After Self (LeetCode 315)

---

## Theory Connections
- Divide and Conquer / Multi-pass Merging: Isolates relation counting from the sorting step, showing how divide-and-conquer can evaluate non-transitive inequalities in $O(N \log N)$ time.

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
