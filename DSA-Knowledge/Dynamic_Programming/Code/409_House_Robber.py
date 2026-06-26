"""
LeetCode Link: https://leetcode.com/problems/house-robber-ii/
Problem Name: House Robber II
Description: Rob houses arranged in a circle. First and last are adjacent.

Folder: Dynamic_Programming
File: 409_House_Robber.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def rob_linear(nums):
    prev2, prev = 0, 0
    for num in nums:
        curr = max(num + prev2, prev)
        prev2 = prev
        prev = curr
    return prev

def optimal_solution(nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([2, 3, 2]) == 3
    assert optimal_solution([1, 2, 3, 1]) == 4
    print("Done.")
