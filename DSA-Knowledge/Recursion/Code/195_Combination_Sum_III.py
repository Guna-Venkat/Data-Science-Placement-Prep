"""
LeetCode Link: https://leetcode.com/problems/combination-sum-iii/
Problem Name: Combination Sum III
Description: Find all combinations of k numbers that sum to n using numbers 1 to 9.

Folder: Recursion
File: 195_Combination_Sum_III.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(9! / (k! * (9-k)!)) combinations
# Space Complexity: O(k) stack depth
def optimal_solution(k: int, n: int) -> list[list[int]]:
    result = []
    
    def backtrack(num, target, path):
        if len(path) == k:
            if target == 0:
                result.append(list(path))
            return
        if num > 9 or target < 0:
            return
            
        # pick
        path.append(num)
        backtrack(num + 1, target - num, path)
        path.pop()
        
        # don't pick
        backtrack(num + 1, target, path)

    backtrack(1, n, [])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    res = optimal_solution(3, 7)
    assert res == [[1, 2, 4]]
    print("Done.")
