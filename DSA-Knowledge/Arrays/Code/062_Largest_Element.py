"""
LeetCode Link: https://www.geeksforgeeks.org/problems/largest-element-in-array5009/1
Problem Name: Largest Element in Array
Description: Given an array A[], find the largest element in it.

Folder: Arrays
File: 062_Largest_Element.py
"""

# ============================================
# BRUTE FORCE APPROACH
# ============================================
# Idea: Sort the array in ascending order and return the last element.
# Time Complexity: O(N log N) due to sorting.
# Space Complexity: O(1) auxiliary space (or O(N) depending on sort implementation).
def brute_force_solution(arr: list[int]) -> int:
    if not arr:
        return -1
    arr_copy = sorted(arr)
    return arr_copy[-1]

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep track of the maximum element seen so far as we traverse the array.
# Time Complexity: O(N) single pass.
# Space Complexity: O(1) constant space.
def optimal_solution(arr: list[int]) -> int:
    if not arr:
        return -1
    max_val = arr[0]
    for val in arr:
        if val > max_val:
            max_val = val
    return max_val

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests for Largest Element...")
    
    test_cases = [
        ([1, 8, 7, 56, 90], 90),
        ([1, 2, 0, 3, 2, 4, 5], 5),
        ([-10, -2, -30, -4], -2)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
