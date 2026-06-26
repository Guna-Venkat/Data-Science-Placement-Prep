"""
LeetCode Link: https://leetcode.com/problems/subsets-ii/
Problem Name: Subsets II
Description: Generate all unique subsets (duplicates allowed in input array).

Folder: Recursion
File: 194_Subsets_II.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Sort. Loop over index space. Skip duplicates `i > idx and nums[i] == nums[i-1]`.
# Time Complexity: O(2^N * N)
# Space Complexity: O(N)
def optimal_solution(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    
    def backtrack(idx, path):
        result.append(list(path))
        
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    res = optimal_solution([1, 2, 2])
    assert sorted(res) == sorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
    print("Done.")
