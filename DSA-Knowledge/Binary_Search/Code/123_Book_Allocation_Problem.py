"""
LeetCode Link: https://www.geeksforgeeks.org/allocate-minimum-number-pages/
Problem Name: Allocate Books
Description: Allocate books to M students such that the maximum pages allocated to a student is minimized.

Folder: Binary_Search
File: 123_Book_Allocation_Problem.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary Search on the maximum pages in range [max(arr), sum(arr)].
# Time Complexity: O(N log(sum - max))
# Space Complexity: O(1)
def optimal_solution(arr: list[int], m: int) -> int:
    if m > len(arr):
        return -1
        
    def count_students(max_pages):
        students = 1
        pages = 0
        for x in arr:
            if pages + x <= max_pages:
                pages += x
            else:
                students += 1
                pages = x
        return students

    low, high = max(arr), sum(arr)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if count_students(mid) <= m:
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
        (([12, 34, 67, 90], 2), 113)
    ]
    for idx, ((arr, m), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr, m) == expected, f"Test case {idx} failed"
    print("Done.")
