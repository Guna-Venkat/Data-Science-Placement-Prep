"""
LeetCode Link: https://www.geeksforgeeks.org/problems/second-largest3735/1
Problem Name: Second Largest Element
Description: Find the second largest distinct element in an array without sorting.

Folder: Arrays
File: 063_Second_Largest_Element.py
"""

# ============================================
# BRUTE FORCE APPROACH
# ============================================
# Idea: Sort the array, find the maximum, and scan backwards to find the first different element.
# Time Complexity: O(N log N)
# Space Complexity: O(1)
def brute_force_solution(arr: list[int]) -> int:
    if len(arr) < 2:
        return -1
    sorted_arr = sorted(arr)
    largest = sorted_arr[-1]
    for i in range(len(sorted_arr) - 2, -1, -1):
        if sorted_arr[i] != largest:
            return sorted_arr[i]
    return -1

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Maintain 'largest' and 'second_largest' during a single pass.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int]) -> int:
    if len(arr) < 2:
        return -1
    largest = -float('inf')
    second_largest = -float('inf')
    
    for x in arr:
        if x > largest:
            second_largest = largest
            largest = x
        elif x > second_largest and x != largest:
            second_largest = x
            
    return second_largest if second_largest != -float('inf') else -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests for Second Largest...")
    
    test_cases = [
        ([12, 35, 1, 10, 34, 1], 34),
        ([10, 10, 10], -1),
        ([1, 2, 5, 4, 3, 5], 4)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
