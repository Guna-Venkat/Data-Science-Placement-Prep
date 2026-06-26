"""
LeetCode Link: https://leetcode.com/problems/split-array-largest-sum/
Problem Name: Split Array Largest Sum
Description: Split array into k subarrays minimizing the maximum sum.

Folder: Binary_Search
File: 124_Split_array_largest_sum.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Equivalent to the Book Allocation Problem.
# Time Complexity: O(N log(sum - max))
# Space Complexity: O(1)
def optimal_solution(nums: list[int], k: int) -> int:
    if k > len(nums):
        return -1
        
    def count_splits(max_sum):
        splits = 1
        curr_sum = 0
        for x in nums:
            if curr_sum + x <= max_sum:
                curr_sum += x
            else:
                splits += 1
                curr_sum = x
        return splits

    low, high = max(nums), sum(nums)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if count_splits(mid) <= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([7, 2, 5, 10, 8], 2), 18)
    ]
    for idx, ((nums, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, k) == expected, f"Test case {idx} failed"
    print("Done.")
