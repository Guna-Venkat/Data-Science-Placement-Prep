"""
LeetCode Link: https://leetcode.com/problems/sort-colors/
Problem Name: Sort Colors (Sort array of 0s, 1s, and 2s)
Description: Sort an array with 0s, 1s, and 2s in-place.

Folder: Arrays
File: 077_Sort_an_array_of_0s_1s_and_2s.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Dutch National Flag Algorithm. Pointers low, mid, high.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> list[int]:
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr[:]) == expected, f"Test case {idx} failed"
        
    print("Done.")
