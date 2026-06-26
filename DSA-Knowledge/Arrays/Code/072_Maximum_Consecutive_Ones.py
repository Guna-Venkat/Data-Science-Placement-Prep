"""
LeetCode Link: https://leetcode.com/problems/max-consecutive-ones/
Problem Name: Max Consecutive Ones
Description: Find the maximum number of consecutive 1s in a binary array.

Folder: Arrays
File: 072_Maximum_Consecutive_Ones.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Reset count to 0 when 0 is seen, update max_count at each step.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    max_count = 0
    curr_count = 0
    for num in nums:
        if num == 1:
            curr_count += 1
            max_count = max(max_count, curr_count)
        else:
            curr_count = 0
    return max_count

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([1, 1, 0, 1, 1, 1], 3),
        ([1, 0, 1, 1, 0, 1], 2)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
