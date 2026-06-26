"""
LeetCode Link: https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1
Problem Name: Find Nth Root of M
Description: Find integer Nth root of M (return -1 if it's not an integer).

Folder: Binary_Search
File: 116_Find_Nth_root_of_a_number.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(log M)
# Space Complexity: O(1)
def optimal_solution(n: int, m: int) -> int:
    low, high = 1, m
    while low <= high:
        mid = (low + high) // 2
        val = mid ** n
        if val == m:
            return mid
        elif val < m:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        ((2, 9), 3),
        ((3, 27), 3),
        ((2, 8), -1)
    ]
    for idx, ((n, m), expected) in enumerate(test_cases, 1):
        assert optimal_solution(n, m) == expected, f"Test case {idx} failed"
    print("Done.")
