"""
LeetCode Link: https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1
Problem Name: Prim's Algorithm (MST)
Description: Find total weight of MST using Prim's algorithm (min heap).

Folder: Graphs
File: 392_Prims_Algorithm.py
"""

import heapq

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(E log V)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[tuple[int, int]]]) -> int:
    visited = [False] * v
    pq = [(0, 0)] # (weight, node)
    mst_weight = 0
    
    while pq:
        w, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        mst_weight += w
        for neighbor, weight in adj[node]:
            if not visited[neighbor]:
                heapq.heappush(pq, (weight, neighbor))
    return mst_weight

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[(1, 2), (2, 1)], [(0, 2), (2, 3)], [(0, 1), (1, 3)]]
    assert optimal_solution(3, adj) == 3
    print("Done.")
