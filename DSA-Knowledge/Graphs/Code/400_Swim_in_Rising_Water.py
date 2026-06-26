"""
LeetCode Link: https://leetcode.com/problems/swim-in-rising-water/
Problem Name: Swim in Rising Water
Description: Find minimal time to swim from top-left to bottom-right on grid where water level rises.

Folder: Graphs
File: 400_Swim_in_Rising_Water.py
"""

import heapq

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Dijkstra's keeping track of path minimax weight.
# Time Complexity: O(N^2 log N)
# Space Complexity: O(N^2)
def optimal_solution(grid: list[list[int]]) -> int:
    n = len(grid)
    pq = [(grid[0][0], 0, 0)] # (elevation, r, c)
    visited = {(0, 0)}
    
    while pq:
        elevation, r, c = heapq.heappop(pq)
        if r == n - 1 and c == n - 1:
            return elevation
            
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                visited.add((nr, nc))
                heapq.heappush(pq, (max(elevation, grid[nr][nc]), nr, nc))
    return 0

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [[0,2],[1,3]]
    assert optimal_solution(grid) == 3
    print("Done.")
