"""
LeetCode Link: https://leetcode.com/problems/next-permutation/
Problem Name: Next Permutation
Description: Find the next lexicographical permutation of numbers.

Folder: Arrays
File: 083_Next_Permutation.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: 
# 1. Find pivot (first decreasing index from right).
# 2. Swap pivot with smallest larger element on its right.
# 3. Reverse elements after pivot.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> list[int]:
    n = len(nums)
    pivot = -1
    
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot = i
            break
            
    if pivot == -1:
        nums.reverse()
        return nums
        
    for i in range(n - 1, pivot, -1):
        if nums[i] > nums[pivot]:
            nums[pivot], nums[i] = nums[i], nums[pivot]
            break
            
    # Reverse subarray nums[pivot+1:]
    nums[pivot+1:] = reversed(nums[pivot+1:])
    return nums

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr[:]) == expected, f"Test case {idx} failed"
        
    print("Done.")
