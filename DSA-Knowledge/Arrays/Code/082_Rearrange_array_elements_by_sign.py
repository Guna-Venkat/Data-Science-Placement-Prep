"""
LeetCode Link: https://leetcode.com/problems/rearrange-array-elements-by-sign/
Problem Name: Rearrange Array Elements by Sign
Description: Rearrange array into alternating positive and negative values.

Folder: Arrays
File: 082_Rearrange_array_elements_by_sign.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Single pass with two pointer indices pointing to even/odd placements.
# Time Complexity: O(N)
# Space Complexity: O(N) for output array
def optimal_solution(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [0] * n
    pos_idx = 0
    neg_idx = 1
    
    for x in nums:
        if x > 0:
            res[pos_idx] = x
            pos_idx += 2
        else:
            res[neg_idx] = x
            neg_idx += 2
            
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([3, 1, -2, -5, 2, -4], [3, -2, 1, -5, 2, -4]),
        ([-1, 1], [1, -1])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
