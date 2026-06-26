"""
LeetCode Link: https://leetcode.com/problems/number-of-enclaves/
Problem Name: Number of Enclaves
Description: Count number of 1s in a grid from which we cannot walk off boundary.

Folder: Graphs
File: 365_Number_of_enclaves.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Mark all boundary-connected 1s using DFS/BFS. Count remaining 1s.
# Time Complexity: O(R * C)
# Space Complexity: O(R * C)
def optimal_solution(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    
    def dfs(r, c):
        grid[r][c] = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                dfs(nr, nc)
                
    for r in range(rows):
        if grid[r][0] == 1: dfs(r, 0)
        if grid[r][cols - 1] == 1: dfs(r, cols - 1)
    for c in range(cols):
        if grid[0][c] == 1: dfs(0, c)
        if grid[rows - 1][c] == 1: dfs(rows - 1, c)
        
    return sum(sum(row) for row in grid)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    assert optimal_solution(grid) == 3
    print("Done.")
