"""
LeetCode Link: https://www.geeksforgeeks.org/problems/left-rotate-an-array-by-one/1
Problem Name: Left Rotate Array by One
Description: Shift all elements left by one index. First element goes to the end.

Folder: Arrays
File: 066_Left_Rotate_Array_by_One.py
"""

# ============================================
# BRUTE FORCE APPROACH / OPTIMAL APPROACH
# ============================================
# Idea: Save the first element, shift all elements left, then place saved element at end.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int]) -> list[int]:
    if not arr:
        return arr
    temp = arr[0]
    for i in range(len(arr) - 1):
        arr[i] = arr[i+1]
    arr[-1] = temp
    return arr

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([1, 2, 3, 4, 5], [2, 3, 4, 5, 1]),
        ([3], [3])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr[:]) == expected, f"Test case {idx} failed"
        
    print("Done.")
