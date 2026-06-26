"""
LeetCode Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
Problem Name: Cheapest Flight Within K Stops
Description: Find cheapest price from src to dst with at most K stops.

Folder: Graphs
File: 384_Cheapest_flight_within_K_stops.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Modified BFS keeping track of stops.
# Time Complexity: O(E * K)
# Space Complexity: O(V)
def optimal_solution(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    adj = [[] for _ in range(n)]
    for u, w, price in flights:
        adj[u].append((w, price))
        
    prices = [float('inf')] * n
    prices[src] = 0
    # queue elements: (stops, node, price)
    queue = [(0, src, 0)]
    
    while queue:
        stops, node, price = queue.pop(0)
        if stops > k:
            continue
        for neighbor, p in adj[node]:
            if prices[neighbor] > price + p:
                prices[neighbor] = price + p
                queue.append((stops + 1, neighbor, prices[neighbor]))
                
    return prices[dst] if prices[dst] != float('inf') else -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    assert optimal_solution(3, flights, 0, 2, 1) == 200
    print("Done.")
