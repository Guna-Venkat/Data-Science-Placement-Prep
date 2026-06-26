"""
LeetCode Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Problem Name: Remove Duplicates from Sorted Array
Description: Remove duplicates in-place from sorted array, returning new length.

Folder: Arrays
File: 065_Remove_duplicates_from_Sorted_array.py
"""

# ============================================
# BRUTE FORCE APPROACH
# ============================================
# Idea: Store elements in a Set, then copy back to array.
# Time Complexity: O(N)
# Space Complexity: O(N)
def brute_force_solution(nums: list[int]) -> int:
    unique_set = sorted(list(set(nums)))
    for i in range(len(unique_set)):
        nums[i] = unique_set[i]
    return len(unique_set)

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Use two pointers: one for tracking unique index, one for scanning.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        # We need to copy arr to check mutations
        arr_copy = arr[:]
        assert optimal_solution(arr_copy) == expected, f"Test case {idx} failed"
        
    print("Done.")
