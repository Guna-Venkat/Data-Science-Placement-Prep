"""
LeetCode Link: https://leetcode.com/problems/network-delay-time/
Problem Name: Network Delay Time
Description: Find minimum time to send signal to all V nodes from K. Return -1 if impossible.

Folder: Graphs
File: 385_Network_Delay_Time.py
"""

import heapq

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(E log V)
# Space Complexity: O(V)
def optimal_solution(times: list[list[int]], n: int, k: int) -> int:
    adj = [[] for _ in range(n + 1)]
    for u, w, d in times:
        adj[u].append((w, d))
        
    dist = [float('inf')] * (n + 1)
    dist[k] = 0
    pq = [(0, k)]
    
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in adj[node]:
            if dist[neighbor] > d + weight:
                dist[neighbor] = d + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))
                
    max_dist = max(dist[1:])
    return max_dist if max_dist != float('inf') else -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    times = [[2,1,1],[2,3,1],[3,4,1]]
    assert optimal_solution(times, 4, 2) == 2
    print("Done.")
