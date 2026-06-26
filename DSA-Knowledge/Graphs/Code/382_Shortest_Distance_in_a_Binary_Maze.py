"""
LeetCode Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/
Problem Name: Shortest Distance in a Binary Maze
Description: Find shortest path from top-left to bottom-right in binary maze.

Folder: Graphs
File: 382_Shortest_Distance_in_a_Binary_Maze.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: BFS since weights are uniform (1).
# Time Complexity: O(R * C)
# Space Complexity: O(R * C)
def optimal_solution(grid: list[list[int]]) -> int:
    if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
        
    n = len(grid)
    queue = [(0, 0, 1)] # (row, col, path_len)
    visited = {(0, 0)}
    
    while queue:
        r, c, length = queue.pop(0)
        if r == n - 1 and c == n - 1:
            return length
            
        # 8 directions
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, length + 1))
    return -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [[0, 1], [1, 0]]
    assert optimal_solution(grid) == 2
    print("Done.")
