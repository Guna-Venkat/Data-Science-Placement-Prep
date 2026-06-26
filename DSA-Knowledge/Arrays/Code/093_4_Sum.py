"""
LeetCode Link: https://leetcode.com/problems/4sum/
Problem Name: 4Sum
Description: Find all unique quadruplets which sum to target.

Folder: Arrays
File: 093_4_Sum.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Sort the array, two nested loops i and j, then two pointer search. Skip duplicates.
# Time Complexity: O(N^3)
# Space Complexity: O(1) auxiliary
def optimal_solution(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    res = []
    
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
                
            l, r = j + 1, n - 1
            while l < r:
                curr_sum = nums[i] + nums[j] + nums[l] + nums[r]
                if curr_sum == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1
                    
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (([1, 0, -1, 0, -2, 2], 0), [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])
    ]
    
    for idx, ((nums, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, target) == expected, f"Test case {idx} failed"
        
    print("Done.")
