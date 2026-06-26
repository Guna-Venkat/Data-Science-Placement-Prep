"""
LeetCode Link: https://leetcode.com/problems/3sum/
Problem Name: 3Sum
Description: Find all unique triplets in the array which gives the sum of zero.

Folder: Arrays
File: 092_3_Sum.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Sort the array, loop i, then use two pointers j and k for remaining search.
# Time Complexity: O(N^2)
# Space Complexity: O(1) auxiliary (excluding result)
def optimal_solution(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    res = []
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        l, r = i + 1, n - 1
        while l < r:
            curr_sum = nums[i] + nums[l] + nums[r]
            if curr_sum == 0:
                res.append([nums[i], nums[l], nums[r]])
                # Skip duplicates for l and r
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            elif curr_sum < 0:
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
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
