"""
LeetCode Link: https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
Problem Name: Minimum Cost to Cut a Stick
Description: Find minimal cost to make all cuts on a stick of length N.

Folder: Dynamic_Programming
File: 452_Minimum_cost_to_cut_the_stick.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Sort cuts. Append 0 and N to cuts array. Partition space.
# Time Complexity: O(M^3) where M is cuts length
# Space Complexity: O(M^2)
def optimal_solution(n: int, cuts: list[int]) -> int:
    cuts = [0] + sorted(cuts) + [n]
    m = len(cuts)
    dp = [[0] * m for _ in range(m)]
    
    for length in range(2, m):
        for i in range(m - length):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])
                
    return dp[0][m - 1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(7, [1, 3, 4, 5]) == 16
    print("Done.")
