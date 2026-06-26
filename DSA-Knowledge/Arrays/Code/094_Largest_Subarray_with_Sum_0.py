"""
LeetCode Link: https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
Problem Name: Largest Subarray with 0 Sum
Description: Find length of the largest subarray with sum 0.

Folder: Arrays
File: 094_Largest_Subarray_with_Sum_0.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep track of prefix sums and their index. If seen before, sum over interval is 0.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(arr: list[int]) -> int:
    prefix_map = {}
    curr_sum = 0
    max_len = 0
    
    for i in range(len(arr)):
        curr_sum += arr[i]
        
        if curr_sum == 0:
            max_len = i + 1
            
        if curr_sum in prefix_map:
            max_len = max(max_len, i - prefix_map[curr_sum])
        else:
            prefix_map[curr_sum] = i
            
    return max_len

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([15, -2, 2, -8, 1, 7, 10, 23], 5),
        ([1, 2, 3], 0)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
