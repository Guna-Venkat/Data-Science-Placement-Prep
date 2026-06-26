"""
LeetCode Link: https://leetcode.com/problems/two-sum/
Problem Name: Two Sum
Description: Find indices of two numbers that sum to K.

Folder: Arrays
File: 076_Two_Sum.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Use HashMap to store indices of visited elements. Look up target - num.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(nums: list[int], target: int) -> list[int]:
    visited = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in visited:
            return [visited[complement], i]
        visited[num] = i
    return []

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2])
    ]
    
    for idx, ((nums, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, target) == expected, f"Test case {idx} failed"
        
    print("Done.")
