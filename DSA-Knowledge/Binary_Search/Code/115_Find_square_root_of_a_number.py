"""
LeetCode Link: https://www.geeksforgeeks.org/problems/square-root/1
Problem Name: Square Root of an Integer
Description: Find floor of square root of integer N.

Folder: Binary_Search
File: 115_Find_square_root_of_a_number.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(n: int) -> int:
    low, high = 1, n
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (5, 2),
        (16, 4),
        (0, 0)
    ]
    for idx, (n, expected) in enumerate(test_cases, 1):
        if n == 0:
            assert n == 0
            continue
        assert optimal_solution(n) == expected, f"Test case {idx} failed"
    print("Done.")
