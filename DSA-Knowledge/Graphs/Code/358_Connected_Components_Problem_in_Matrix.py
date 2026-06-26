"""
LeetCode Link: https://leetcode.com/problems/number-of-islands/
Problem Name: Connected Components in Matrix
Description: Find total connected components (islands) including diagonal steps.

Folder: Graphs
File: 358_Connected_Components_Problem_in_Matrix.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(R * C)
# Space Complexity: O(R * C)
def optimal_solution(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r, c):
        grid[r][c] = "0"
        # 8 directions (diagonal steps included in this GFG version)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                dfs(nr, nc)
                
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                dfs(r, c)
    return islands

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [["1", "1", "0"], ["0", "0", "1"], ["1", "0", "1"]]
    # Diagonal components connected: all form 1 component
    assert optimal_solution(grid) == 1
    print("Done.")
