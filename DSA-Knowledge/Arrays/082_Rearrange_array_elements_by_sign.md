# Rearrange array elements by sign

## Difficulty
Medium

---

## Pattern
Two Pointers / Vector Logic

---

## Recognition Clues
- Array has equal number of positive and negative integers.\n- Rearrange so that signs alternate (positive first).\n- Must preserve the relative order of elements of the same sign.

---

## Core Insight
- Positive elements must reside at even indices: 0, 2, 4, ...\n- Negative elements must reside at odd indices: 1, 3, 5, ...\n- Since we must preserve relative order, we can initialize a new array and write elements sequentially using positive and negative write pointers.

---

## Interview Explanation
1. **Brute Force Idea**: Filter all positive numbers into a list `pos` and all negative numbers into a list `neg`. Then, iterate and merge them back alternatingly: write `pos[i]` to `arr[2*i]` and `neg[i]` to `arr[2*i + 1]`.
2. **Why Inefficient**: While this is $O(N)$, it requires two separate passes to filter and a third pass to merge, allocating extra arrays.
3. **Key Observation**: We can place elements directly into their target indices in a single pass of the input array by maintaining pointers to the next open positive and negative positions.
4. **Optimal Solution Intuition**: Allocate an answer array of size $N$. Initialize `pos_idx = 0` and `neg_idx = 1`. Iterate through the input array: if `num > 0`, assign `ans[pos_idx] = num` and set `pos_idx += 2`. If `num < 0`, assign `ans[neg_idx] = num` and set `neg_idx += 2`.
5. **Time Complexity**: $O(N)$ (single pass).
6. **Space Complexity**: $O(N)$ to store the rearranged result.

---

## Brute Force
- **Idea**: Separate positives and negatives into two lists, then merge.
- **Code**:
```python
def rearrange_brute(nums):
    pos = [x for x in nums if x > 0]
    neg = [x for x in nums if x < 0]
    ans = []
    for i in range(len(pos)):
        ans.append(pos[i])
        ans.append(neg[i])
    return ans
```
- **TC**: $O(N)$
- **SC**: $O(N)$

---

## Optimal Approach
- **Algorithm**: Two-pointer single-pass arrangement.
- **Why it works**: Pre-indexing even/odd destinations allows placing elements directly without intermediate temporary lists.
- **Complexity**: Time: $O(N)$, Space: $O(N)$ (to store the returned array).

---

## Optimal Code
```python
def rearrangeArray(nums):
    n = len(nums)
    ans = [0] * n
    pos_idx = 0
    neg_idx = 1
    
    for num in nums:
        if num > 0:
            ans[pos_idx] = num
            pos_idx += 2
        else:
            ans[neg_idx] = num
            neg_idx += 2
            
    return ans
```

---

## Test Cases
- **Normal Case**: Input: `nums = [3, 1, -2, -5, 2, -4]`\n- Output: `[3, -2, 1, -5, 2, -4]`
- **Hard Case**: Input: `nums = [1, -1, 2, -2, 3, -3]`\n- Output: `[1, -1, 2, -2, 3, -3]`
- **Edge Case**: Input: `nums = [10, -10]`\n- Output: `[10, -10]`

---

## Common Mistakes
- Incrementing index pointers by 1 instead of 2.\n- Not maintaining stability (changing relative order of elements of the same sign).

---

## Killer Edge Cases
- Array has only 2 elements.\n- Array already alternated properly.

---

## Follow-Up Variants
- Rearrange by Sign $\rightarrow$ Rearrange when positive and negative counts are unequal (requires appending remaining elements at the end).

---

## Similar Problems
- Sort Array By Parity\n- Wiggle Sort

---

## Theory Connections
- Stable Partitioning Variant: Maintains order of equal-keyed elements (positive keys grouped together, negative keys grouped together) while interleaving.

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
