"""
LeetCode Link: https://leetcode.com/problems/subarray-sum-equals-k/
Problem Name: Subarray Sum Equals K
Description: Find the total number of continuous subarrays whose sum equals to K.

Folder: Arrays
File: 089_Count_subarrays_with_given_sum.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep track of prefix sum count in a HashMap. Check if curr_sum - K exists in map.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(nums: list[int], k: int) -> int:
    prefix_counts = {0: 1}
    curr_sum = 0
    count = 0
    
    for x in nums:
        curr_sum += x
        rem = curr_sum - k
        if rem in prefix_counts:
            count += prefix_counts[rem]
        prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
        
    return count

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (([1, 1, 1], 2), 2),
        (([1, 2, 3], 3), 2)
    ]
    
    for idx, ((nums, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, k) == expected, f"Test case {idx} failed"
        
    print("Done.")
