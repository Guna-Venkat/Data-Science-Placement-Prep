"""
LeetCode Link: https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1
Problem Name: Find Missing and Repeating Number
Description: Find the repeating and missing elements in an array containing elements from 1 to N.

Folder: Arrays
File: 098_Find_the_repeating_and_missing_number.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Math equations using S (Sum of numbers) and S2 (Sum of squares of numbers).
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int]) -> tuple[int, int]:
    n = len(arr)
    # Sn = Sum of 1 to N, S2n = Sum of squares of 1 to N
    Sn = n * (n + 1) // 2
    S2n = n * (n + 1) * (2 * n + 1) // 6
    
    S = sum(arr)
    S2 = sum(x*x for x in arr)
    
    # x = repeating, y = missing
    # S - Sn = x - y
    # S2 - S2n = x^2 - y^2 = (x - y)(x + y)
    val1 = S - Sn  # x - y
    val2 = S2 - S2n  # x^2 - y^2
    
    val3 = val2 // val1  # x + y
    
    x = (val1 + val3) // 2
    y = val3 - x
    
    return x, y

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([3, 1, 2, 5, 3], (3, 4)),
        ([4, 3, 6, 2, 1, 1], (1, 5))
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
