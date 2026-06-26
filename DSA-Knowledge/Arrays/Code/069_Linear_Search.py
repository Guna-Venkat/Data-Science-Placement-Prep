"""
LeetCode Link: https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1
Problem Name: Linear Search
Description: Search for an element in an array. Return index if found, else -1.

Folder: Arrays
File: 069_Linear_Search.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int], target: int) -> int:
    for idx, val in enumerate(arr):
        if val == target:
            return idx
    return -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (([1, 2, 3, 4, 5], 3), 2),
        (([1, 2, 3, 4, 5], 6), -1)
    ]
    
    for idx, ((arr, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr, target) == expected, f"Test case {idx} failed"
        
    print("Done.")
