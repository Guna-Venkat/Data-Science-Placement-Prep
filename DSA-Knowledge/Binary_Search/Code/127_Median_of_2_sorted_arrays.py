"""
LeetCode Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
Problem Name: Median of Two Sorted Arrays
Description: Find the median of two sorted arrays in O(log(min(n, m))) time.

Folder: Binary_Search
File: 127_Median_of_2_sorted_arrays.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary search on partition of the smaller array.
# Time Complexity: O(log(min(N, M)))
# Space Complexity: O(1)
def optimal_solution(nums1: list[int], nums2: list[int]) -> float:
    if len(nums1) > len(nums2):
        return optimal_solution(nums2, nums1)
        
    n1, n2 = len(nums1), len(nums2)
    low, high = 0, n1
    half = (n1 + n2 + 1) // 2
    
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = half - cut1
        
        l1 = nums1[cut1-1] if cut1 > 0 else -float('inf')
        l2 = nums2[cut2-1] if cut2 > 0 else -float('inf')
        r1 = nums1[cut1] if cut1 < n1 else float('inf')
        r2 = nums2[cut2] if cut2 < n2 else float('inf')
        
        if l1 <= r2 and l2 <= r1:
            if (n1 + n2) % 2 == 1:
                return float(max(l1, l2))
            return (max(l1, l2) + min(r1, r2)) / 2.0
        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1
            
    return 0.0

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([1, 3], [2]), 2.0),
        (([1, 2], [3, 4]), 2.5)
    ]
    for idx, ((n1, n2), expected) in enumerate(test_cases, 1):
        assert optimal_solution(n1, n2) == expected, f"Test case {idx} failed"
    print("Done.")
