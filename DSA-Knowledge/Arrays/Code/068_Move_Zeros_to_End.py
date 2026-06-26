"""
LeetCode Link: https://leetcode.com/problems/move-zeroes/
Problem Name: Move Zeroes
Description: Move all 0s to the end of the array while maintaining relative order of non-zero elements.

Folder: Arrays
File: 068_Move_Zeros_to_End.py
"""

# ============================================
# BRUTE FORCE APPROACH
# ============================================
# Idea: Store non-zero elements in a temp list, then fill the rest of the array with zeroes.
# Time Complexity: O(N)
# Space Complexity: O(N)
def brute_force_solution(nums: list[int]) -> list[int]:
    temp = [x for x in nums if x != 0]
    for i in range(len(temp)):
        nums[i] = temp[i]
    for i in range(len(temp), len(nums)):
        nums[i] = 0
    return nums

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Use a pointer for the next position of non-zero element. Swap when non-zero found.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> list[int]:
    last_non_zero = 0
    for curr in range(len(nums)):
        if nums[curr] != 0:
            nums[last_non_zero], nums[curr] = nums[curr], nums[last_non_zero]
            last_non_zero += 1
    return nums

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr[:]) == expected, f"Test case {idx} failed"
        
    print("Done.")
