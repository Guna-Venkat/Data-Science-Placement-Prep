"""
LeetCode Link: https://leetcode.com/problems/kth-missing-positive-number/
Problem Name: Kth Missing Positive Number
Description: Find the kth missing positive integer.

Folder: Binary_Search
File: 121_Kth_Missing_Positive_Number.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: At index `mid`, the number of missing positives is `arr[mid] - (mid + 1)`.
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int], k: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        missing = arr[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    # Result formula: low + k
    return low + k

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([2, 3, 4, 7, 11], 5), 9),
        (([1, 2, 3, 4], 2), 6)
    ]
    for idx, ((arr, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr, k) == expected, f"Test case {idx} failed"
    print("Done.")
