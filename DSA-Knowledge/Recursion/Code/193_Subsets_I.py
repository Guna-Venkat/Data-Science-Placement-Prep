"""
LeetCode Link: https://www.geeksforgeeks.org/problems/subset-sums2234/1
Problem Name: Subset Sums (Subsets I)
Description: Generate sum of all possible subsets.

Folder: Recursion
File: 193_Subsets_I.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(2^N)
# Space Complexity: O(N) recursion stack
def optimal_solution(arr: list[int]) -> list[int]:
    result = []
    
    def backtrack(idx, curr_sum):
        if idx == len(arr):
            result.append(curr_sum)
            return
            
        # pick
        backtrack(idx + 1, curr_sum + arr[idx])
        # don't pick
        backtrack(idx + 1, curr_sum)

    backtrack(0, 0)
    result.sort()
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([2, 3]) == [0, 2, 3, 5]
    print("Done.")
