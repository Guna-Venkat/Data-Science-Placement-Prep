"""
LeetCode Link: https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1
Problem Name: K-th Element of Two Sorted Arrays
Description: Find the kth element in the final sorted array of two sorted arrays.

Folder: Binary_Search
File: 128_Kth_element_of_2_sorted_arrays.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Similar to Median of Two Sorted Arrays, binary search on partition cut.
# Time Complexity: O(log(min(N, M)))
# Space Complexity: O(1)
def optimal_solution(arr1: list[int], arr2: list[int], k: int) -> int:
    n1, n2 = len(arr1), len(arr2)
    if n1 > n2:
        return optimal_solution(arr2, arr1, k)
        
    low = max(0, k - n2)
    high = min(k, n1)
    
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = k - cut1
        
        l1 = arr1[cut1-1] if cut1 > 0 else -float('inf')
        l2 = arr2[cut2-1] if cut2 > 0 else -float('inf')
        r1 = arr1[cut1] if cut1 < n1 else float('inf')
        r2 = arr2[cut2] if cut2 < n2 else float('inf')
        
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1
            
    return -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([2, 3, 6, 7, 9], [1, 4, 8, 10], 5), 6)
    ]
    for idx, ((arr1, arr2, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr1, arr2, k) == expected, f"Test case {idx} failed"
    print("Done.")
