# Longest Increasing Subsequence

**Pattern:** Dynamic Programming with Binary Search (Patience Sorting)

**Recognition:**
- Find length of the longest strictly increasing subsequence in an array.
- $O(N^2)$ dynamic programming approach is too slow for large inputs ($N \ge 10^5$).
- Maintain an active sorted list `sub` where `sub[i]` represents the smallest tail of all increasing subsequences of length `i+1` encountered so far.

**Optimal Code (Python):**
```python
import bisect

def lengthOfLIS(nums: list[int]) -> int:
    if not nums:
        return 0
        
    sub = []
    for num in nums:
        # Find the insertion index for num in sub to maintain sorted order
        idx = bisect.bisect_left(sub, num)
        
        # If num is greater than all elements in sub, append it
        if idx == len(sub):
            sub.append(num)
        # Otherwise, replace the element at idx to optimize the tail value
        else:
            sub[idx] = num
            
    return len(sub)
```

**Killer Edge:**
- Array is sorted in descending order (returns `1`).
- Array contains all duplicate values (returns `1` because we need strictly increasing).
- Empty input.

**Mistake:**
- Using `bisect_right` instead of `bisect_left` which would handle duplicate elements incorrectly, violating the strictly increasing requirement.
- Confusing the `sub` array as the actual LIS subsequence. The elements in `sub` do not represent the correct LIS sequence elements, only the *length* of `sub` is correct.
