"""
LeetCode Link: https://www.geeksforgeeks.org/problems/rotation4755/1
Problem Name: Rotation Count
Description: Find out how many times the array is rotated (equivalent to index of minimum element).

Folder: Binary_Search
File: 112_Find_out_how_many_times_the_array_is_rotated.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: The rotation count is equal to the index of the minimum element.
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int]) -> int:
    low, high = 0, len(arr) - 1
    min_val = float('inf')
    ans_idx = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[low] <= arr[high]:
            if arr[low] < min_val:
                min_val = arr[low]
                ans_idx = low
            break
        if arr[low] <= arr[mid]:
            if arr[low] < min_val:
                min_val = arr[low]
                ans_idx = low
            low = mid + 1
        else:
            if arr[mid] < min_val:
                min_val = arr[mid]
                ans_idx = mid
            high = mid - 1
    return ans_idx

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        ([5, 1, 2, 3, 4], 1),
        ([4, 5, 6, 7, 0, 1, 2], 4)
    ]
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
    print("Done.")
