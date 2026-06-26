"""
LeetCode Link: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
Problem Name: Number of Ways to Arrive at Destination
Description: Find total paths that yield shortest distance from 0 to N-1.

Folder: Graphs
File: 386_Number_of_ways_to_arrive_at_destination.py
"""

import heapq

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Dijkstra's keeping dynamic paths count.
# Time Complexity: O(E log V)
# Space Complexity: O(V)
def optimal_solution(n: int, roads: list[list[int]]) -> int:
    MOD = 10**9 + 7
    adj = [[] for _ in range(n)]
    for u, w, d in roads:
        adj[u].append((w, d))
        adj[w].append((u, d))
        
    dist = [float('inf')] * n
    ways = [0] * n
    dist[0] = 0
    ways[0] = 1
    pq = [(0, 0)] # (distance, node)
    
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in adj[node]:
            if dist[neighbor] > d + weight:
                dist[neighbor] = d + weight
                ways[neighbor] = ways[node]
                heapq.heappush(pq, (dist[neighbor], neighbor))
            elif dist[neighbor] == d + weight:
                ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
    return ways[-1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    assert optimal_solution(7, roads) == 4
    print("Done.")
