"""
LeetCode Link: https://leetcode.com/problems/cherry-pickup-ii/
Problem Name: Cherry Pickup II (Ninja and his Friends)
Description: 3D DP. Two robots starting at (0,0) and (0, C-1) picking cherries on grid.

Folder: Dynamic_Programming
File: 415_Ninja_and_his_Friends.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(R * C * C * 9)
# Space Complexity: O(C * C)
def optimal_solution(grid: list[list[int]]) -> int:
    r, c = len(grid), len(grid[0])
    dp = [[-float('inf')] * c for _ in range(c)]
    dp[0][c - 1] = grid[0][0] + grid[0][c - 1] if c > 1 else grid[0][0]
    
    for row in range(1, r):
        next_dp = [[-float('inf')] * c for _ in range(c)]
        for c1 in range(c):
            for c2 in range(c):
                # Rob1 is at c1, Rob2 is at c2
                cherry = grid[row][c1] + (grid[row][c2] if c1 != c2 else 0)
                max_prev = -float('inf')
                for dc1 in (-1, 0, 1):
                    for dc2 in (-1, 0, 1):
                        pc1, pc2 = c1 + dc1, c2 + dc2
                        if 0 <= pc1 < c and 0 <= pc2 < c:
                            max_prev = max(max_prev, dp[pc1][pc2])
                next_dp[c1][c2] = max_prev + cherry
        dp = next_dp
        
    return max(max(row) for row in dp)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
    assert optimal_solution(grid) == 24
    print("Done.")
