"""
LeetCode Link: https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k8645/1
Problem Name: Longest Subarray with Sum K (Positives, Negatives, Zeros)
Description: Find length of longest subarray with sum K.

Folder: Arrays
File: 075_Longest_subarray_with_sum_K.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Map prefix_sum to its first occurrence index. If prefix_sum - K is in map, compute length.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(arr: list[int], k: int) -> int:
    prefix_map = {}
    curr_sum = 0
    max_len = 0
    
    for i in range(len(arr)):
        curr_sum += arr[i]
        
        if curr_sum == k:
            max_len = i + 1
            
        rem = curr_sum - k
        if rem in prefix_map:
            max_len = max(max_len, i - prefix_map[rem])
            
        # Store only the first occurrence to maximize the length
        if curr_sum not in prefix_map:
            prefix_map[curr_sum] = i
            
    return max_len

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (([10, 5, 2, 7, 1, 9], 15), 4),
        (([-1, 8, 5, -2, 2, -8, 1, 7], 0), 5)
    ]
    
    for idx, ((arr, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr, k) == expected, f"Test case {idx} failed"
        
    print("Done.")
