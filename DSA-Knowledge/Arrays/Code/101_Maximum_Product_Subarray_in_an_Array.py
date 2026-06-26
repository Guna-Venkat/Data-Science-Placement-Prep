"""
LeetCode Link: https://leetcode.com/problems/maximum-product-subarray/
Problem Name: Maximum Product Subarray
Description: Find contiguous subarray within an array which has the largest product.

Folder: Arrays
File: 101_Maximum_Product_Subarray_in_an_Array.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep track of prefix product and suffix product. Max product is the max seen.
# If product becomes 0, reset to 1 (conceptually starting a new subarray).
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    n = len(nums)
    prefix = 1
    suffix = 1
    max_prod = -float('inf')
    
    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
            
        prefix *= nums[i]
        suffix *= nums[n - 1 - i]
        
        max_prod = max(max_prod, prefix, suffix)
        
    return max_prod

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([2, 3, -2, 4], 6),
        ([-2, 0, -1], 0)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
