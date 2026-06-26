"""
LeetCode Link: https://leetcode.com/problems/house-robber/
Problem Name: Maximum Sum of Non-Adjacent Elements
Description: Rob houses without robbing two adjacent houses.

Folder: Dynamic_Programming
File: 408_Maximum_Sum_of_Non_Adjacent_Elements.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    prev2, prev = 0, 0
    for num in nums:
        pick = num + prev2
        non_pick = prev
        curr = max(pick, non_pick)
        prev2 = prev
        prev = curr
    return prev

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 3, 1]) == 4
    assert optimal_solution([2, 7, 9, 3, 1]) == 12
    print("Done.")
