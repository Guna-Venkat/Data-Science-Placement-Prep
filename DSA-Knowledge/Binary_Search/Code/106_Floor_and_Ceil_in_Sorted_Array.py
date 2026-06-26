"""
LeetCode Link: https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1
Problem Name: Floor and Ceil
Description: Find floor (largest element <= x) and ceil (smallest element >= x).

Folder: Binary_Search
File: 106_Floor_and_Ceil_in_Sorted_Array.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int], x: int) -> tuple[int, int]:
    # Find Floor
    low, high = 0, len(arr) - 1
    floor = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            floor = arr[mid]
            low = mid + 1
        else:
            high = mid - 1
            
    # Find Ceil
    low, high = 0, len(arr) - 1
    ceil = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ceil = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
            
    return floor, ceil

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([1, 2, 8, 10, 11, 12, 19], 8), (8, 8)),
        (([1, 2, 8, 10, 11, 12, 19], 5), (2, 8)),
        (([1, 2, 8, 10, 11, 12, 19], 0), (-1, 1))
    ]
    for idx, ((arr, x), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr, x) == expected, f"Test case {idx} failed"
    print("Done.")
