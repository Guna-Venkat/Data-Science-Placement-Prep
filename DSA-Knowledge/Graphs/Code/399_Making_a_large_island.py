"""
LeetCode Link: https://leetcode.com/problems/making-a-large-island/
Problem Name: Making a Large Island
Description: Change at most one 0 to 1. Find size of largest island possible.

Folder: Graphs
File: 399_Making_a_large_island.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Color islands with unique IDs. Map ID to component size. 
# For each 0, sum sizes of unique neighbor island IDs.
# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
def optimal_solution(grid: list[list[int]]) -> int:
    n = len(grid)
    island_sizes = {}
    color = 2
    
    def dfs(r, c, clr):
        grid[r][c] = clr
        size = 1
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                size += dfs(nr, nc, clr)
        return size
        
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                size = dfs(r, c, color)
                island_sizes[color] = size
                color += 1
                
    max_island = max(island_sizes.values()) if island_sizes else 0
    
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                neighbor_colors = set()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                        neighbor_colors.add(grid[nr][nc])
                size = 1 + sum(island_sizes[clr] for clr in neighbor_colors)
                max_island = max(max_island, size)
    return max_island

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [[1, 0], [0, 1]]
    assert optimal_solution(grid) == 3
    print("Done.")
