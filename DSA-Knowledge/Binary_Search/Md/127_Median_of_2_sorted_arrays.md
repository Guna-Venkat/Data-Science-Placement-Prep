# Median of 2 Sorted Arrays

**Pattern:** Binary Search on Partitions (Cut/Index Division)

**Recognition:**
- Find median of two sorted arrays of sizes $N_1$ and $N_2$ in $O(\log(\min(N_1, N_2)))$ time complexity.
- Partition both arrays into a left half and a right half such that the left half contains exactly half of the total elements: `(N1 + N2 + 1) // 2`.
- Identify elements at the boundary edges: `l1, l2` (max of left partitions) and `r1, r2` (min of right partitions).

**Optimal Code (Python):**
```python
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    n1, n2 = len(nums1), len(nums2)
    # Ensure nums1 is the smaller array to optimize time complexity and avoid out of bound errors
    if n1 > n2:
        return findMedianSortedArrays(nums2, nums1)
        
    low, high = 0, n1
    total_elements = n1 + n2
    left_half_size = (n1 + n2 + 1) // 2
    
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = left_half_size - cut1
        
        # Calculate boundary elements. Use -inf and inf for edge cases.
        l1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
        l2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
        r1 = nums1[cut1] if cut1 < n1 else float('inf')
        r2 = nums2[cut2] if cut2 < n2 else float('inf')
        
        if l1 <= r2 and l2 <= r1:
            # Odd number of total elements
            if total_elements % 2 == 1:
                return float(max(l1, l2))
            # Even number of total elements
            return (max(l1, l2) + min(r1, r2)) / 2.0
        elif l1 > r2:
            # Shift partition left in nums1
            high = cut1 - 1
        else:
            # Shift partition right in nums1
            low = cut1 + 1
            
    return 0.0
```

**Killer Edge:**
- One of the arrays is empty (correctly handled by `-inf`/`inf` defaults).
- Completely disjoint arrays (e.g. `[1, 2]` and `[3, 4]`).
- Total element count is odd vs even.

**Mistake:**
- Not swapping the arrays to make `nums1` the smaller array, which causes index out of bound issues when calculating `cut2`.
- Incorrectly updating binary search pointers (e.g., using `high = cut1` or `low = cut1` instead of `cut1 - 1` and `cut1 + 1`).
