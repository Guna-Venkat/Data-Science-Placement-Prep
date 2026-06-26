"""
LeetCode Link: https://leetcode.com/problems/rotting-oranges/
Problem Name: Rotting Oranges
Description: Find minimum time to rot all fresh oranges. Return -1 if impossible.

Folder: Graphs
File: 359_Rotten_Oranges.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(R * C)
# Space Complexity: O(R * C)
def optimal_solution(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = []
    fresh = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1
                
    minutes = 0
    while queue:
        r, c, time = queue.pop(0)
        minutes = max(minutes, time)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc, time + 1))
                
    return minutes if fresh == 0 else -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    assert optimal_solution(grid) == 4
    print("Done.")
