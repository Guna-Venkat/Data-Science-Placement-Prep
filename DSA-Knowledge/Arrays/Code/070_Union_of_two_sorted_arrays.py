"""
LeetCode Link: https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1
Problem Name: Union of Two Sorted Arrays
Description: Given two sorted arrays, find their union.

Folder: Arrays
File: 070_Union_of_two_sorted_arrays.py
"""

# ============================================
# BRUTE FORCE APPROACH
# ============================================
# Idea: Insert all elements of both arrays into a sorted Set.
# Time Complexity: O((N + M) log(N + M))
# Space Complexity: O(N + M)
def brute_force_solution(arr1: list[int], arr2: list[int]) -> list[int]:
    return sorted(list(set(arr1 + arr2)))

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Use two pointers to merge sorted arrays while skipping duplicates.
# Time Complexity: O(N + M)
# Space Complexity: O(1) auxiliary space (excluding result)
def optimal_solution(arr1: list[int], arr2: list[int]) -> list[int]:
    i, j = 0, 0
    union = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
            
    while i < len(arr1):
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1
        
    return union

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (([1, 2, 3, 4, 5], [2, 3, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7]),
        (([1, 1, 1], [2, 2]), [1, 2])
    ]
    
    for idx, ((arr1, arr2), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr1, arr2) == expected, f"Test case {idx} failed"
        
    print("Done.")
