"""
LeetCode Link: https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1
Problem Name: Number of Occurrence
Description: Count occurrences of a target number in sorted array.

Folder: Binary_Search
File: 108_Count_Occurrences_in_a_Sorted_Array.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Count = Last Occurrence - First Occurrence + 1
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int], x: int) -> int:
    def get_first():
        l, r = 0, len(arr) - 1
        first = -1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == x:
                first = mid
                r = mid - 1
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return first

    def get_last():
        l, r = 0, len(arr) - 1
        last = -1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == x:
                last = mid
                l = mid + 1
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return last

    f = get_first()
    if f == -1:
        return 0
    return get_last() - f + 1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([1, 1, 2, 2, 2, 2, 3], 2), 4),
        (([1, 1, 2, 2, 2, 2, 3], 4), 0)
    ]
    for idx, ((arr, x), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr, x) == expected, f"Test case {idx} failed"
    print("Done.")
