"""
LeetCode Link: https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1
Problem Name: Dijkstra's Algorithm
Description: Shortest path from source node using Min Heap.

Folder: Graphs
File: 380_Djisktras_Algorithm.py
"""

import heapq

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(E log V)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[tuple[int, int]]], src: int) -> list[int]:
    dist = [float('inf')] * v
    dist[src] = 0
    pq = [(0, src)] # (distance, node)
    
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in adj[node]:
            if dist[neighbor] > d + weight:
                dist[neighbor] = d + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))
    return dist

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[(1, 4), (2, 1)], [(0, 4), (2, 2)], [(0, 1), (1, 2)]]
    assert optimal_solution(3, adj, 0) == [0, 3, 1]
    print("Done.")
