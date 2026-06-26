"""
LeetCode Link: https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k8645/1
Problem Name: Longest Subarray with Sum K (Positives)
Description: Find length of longest subarray with sum K in positive integer array.

Folder: Arrays
File: 074_Longest_subarray_with_given_sum_Kpositives.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Two pointer / sliding window. Expand right, shrink left when sum exceeds K.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int], k: int) -> int:
    l = 0
    curr_sum = 0
    max_len = 0
    
    for r in range(len(arr)):
        curr_sum += arr[r]
        while curr_sum > k and l <= r:
            curr_sum -= arr[l]
            l += 1
        if curr_sum == k:
            max_len = max(max_len, r - l + 1)
            
    return max_len

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (([1, 2, 3, 1, 1, 1, 1], 3), 4),
        (([1, 4, 3, 3, 5, 5], 16), 0)
    ]
    
    for idx, ((arr, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr, k) == expected, f"Test case {idx} failed"
        
    print("Done.")
