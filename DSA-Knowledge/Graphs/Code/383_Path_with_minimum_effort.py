"""
LeetCode Link: https://leetcode.com/problems/path-with-minimum-effort/
Problem Name: Path with Minimum Effort
Description: Find path from top-left to bottom-right minimizing maximum absolute difference between consecutive cells.

Folder: Graphs
File: 383_Path_with_minimum_effort.py
"""

import heapq

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Dijkstra using effort as weight metric.
# Time Complexity: O(R * C log (R * C))
# Space Complexity: O(R * C)
def optimal_solution(heights: list[list[int]]) -> int:
    rows, cols = len(heights), len(heights[0])
    efforts = [[float('inf')] * cols for _ in range(rows)]
    efforts[0][0] = 0
    pq = [(0, 0, 0)] # (effort, r, c)
    
    while pq:
        effort, r, c = heapq.heappop(pq)
        if r == rows - 1 and c == cols - 1:
            return effort
        if effort > efforts[r][c]:
            continue
            
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                diff = max(effort, abs(heights[nr][nc] - heights[r][c]))
                if efforts[nr][nc] > diff:
                    efforts[nr][nc] = diff
                    heapq.heappush(pq, (diff, nr, nc))
    return 0

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    assert optimal_solution(heights) == 2
    print("Done.")
