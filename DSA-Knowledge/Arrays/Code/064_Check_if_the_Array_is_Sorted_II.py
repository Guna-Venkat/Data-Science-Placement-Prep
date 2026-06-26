"""
LeetCode Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
Problem Name: Check if Array Is Sorted and Rotated
Description: Check if the array can be sorted by rotating it some number of positions.

Folder: Arrays
File: 064_Check_if_the_Array_is_Sorted_II.py
"""

# ============================================
# BRUTE FORCE APPROACH
# ============================================
# Idea: Check every possible rotation to see if it is sorted.
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def brute_force_solution(nums: list[int]) -> bool:
    n = len(nums)
    for rot in range(n):
        rotated = nums[rot:] + nums[:rot]
        is_sorted = True
        for i in range(1, n):
            if rotated[i] < rotated[i-1]:
                is_sorted = False
                break
        if is_sorted:
            return True
    return False

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: If an array is sorted and rotated, there can be at most one element 
# that is strictly greater than its next element (wrapping around to index 0).
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> bool:
    n = len(nums)
    count = 0
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count += 1
    return count <= 1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([3, 4, 5, 1, 2], True),
        ([2, 1, 3, 4], False),
        ([1, 2, 3], True)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
