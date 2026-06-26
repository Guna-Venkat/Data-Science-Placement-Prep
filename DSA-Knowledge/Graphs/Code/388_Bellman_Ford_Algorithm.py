"""
LeetCode Link: https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1
Problem Name: Bellman Ford Algorithm
Description: Shortest path from source allowing negative weight edges. Returns -1 if negative cycle exists.

Folder: Graphs
File: 388_Bellman_Ford_Algorithm.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Relax all edges V-1 times. Run 1 more relaxation to check for negative cycles.
# Time Complexity: O(V * E)
# Space Complexity: O(V)
def optimal_solution(v: int, edges: list[list[int]], src: int) -> list[int]:
    dist = [10**8] * v
    dist[src] = 0
    
    for _ in range(v - 1):
        for u, w, d in edges:
            if dist[u] != 10**8 and dist[u] + d < dist[w]:
                dist[w] = dist[u] + d
                
    # Check for negative cycle
    for u, w, d in edges:
        if dist[u] != 10**8 and dist[u] + d < dist[w]:
            return [-1]
            
    return dist

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    edges = [[0, 1, 9]]
    assert optimal_solution(2, edges, 0) == [0, 9]
    print("Done.")
