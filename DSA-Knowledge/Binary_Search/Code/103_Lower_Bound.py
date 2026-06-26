"""
LeetCode Link: https://www.geeksforgeeks.org/problems/implement-lower-bound/1
Problem Name: Lower Bound
Description: Find the index of the first element in sorted array which is >= X.

Folder: Binary_Search
File: 103_Lower_Bound.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int], x: int) -> int:
    low, high = 0, len(arr) - 1
    ans = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([1, 2, 8, 10, 11, 12, 19], 0), 0),
        (([1, 2, 8, 10, 11, 12, 19], 5), 2),
        (([1, 2, 8, 10, 11, 12, 19], 20), 7)
    ]
    for idx, ((arr, x), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr, x) == expected, f"Test case {idx} failed"
    print("Done.")
