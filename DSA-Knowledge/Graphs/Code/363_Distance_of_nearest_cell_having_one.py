"""
LeetCode Link: https://leetcode.com/problems/01-matrix/
Problem Name: 01 Matrix (Nearest Cell Having 1)
Description: Find distance of nearest cell having 1 for each cell in a binary matrix.

Folder: Graphs
File: 363_Distance_of_nearest_cell_having_one.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Multi-source BFS starting from all 1 cells.
# Time Complexity: O(R * C)
# Space Complexity: O(R * C)
def optimal_solution(grid: list[list[int]]) -> list[list[int]]:
    rows, cols = len(grid), len(grid[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    queue = []
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                dist[r][c] = 0
                queue.append((r, c))
                
    while queue:
        r, c = queue.pop(0)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
    return dist

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    res = optimal_solution(grid)
    assert res[0][0] == 2
    assert res[1][1] == 0
    print("Done.")
