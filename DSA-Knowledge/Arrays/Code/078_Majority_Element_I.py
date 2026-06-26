"""
LeetCode Link: https://leetcode.com/problems/majority-element/
Problem Name: Majority Element (> N/2)
Description: Find the element that appears more than N/2 times.

Folder: Arrays
File: 078_Majority_Element_I.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Boyer-Moore Voting Algorithm. Candidate selection with cancellation.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    return candidate

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
