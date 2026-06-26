"""
LeetCode Link: https://www.geeksforgeeks.org/problems/shortest-path-in-directed-acyclic-graph/1
Problem Name: Shortest Path in DAG
Description: Find shortest path in DAG from source node. Weights given.

Folder: Graphs
File: 379_Shortest_path_in_DAG.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Run Topological Sort. Relax edges of nodes sequentially in Topo order.
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, edges: list[tuple[int, int, int]], src: int) -> list[int]:
    adj = [[] for _ in range(v)]
    for u, w, d in edges:
        adj[u].append((w, d))
        
    # Topo Sort
    visited = [False] * v
    stack = []
    
    def dfs(node):
        visited[node] = True
        for neighbor, weight in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)
        
    for i in range(v):
        if not visited[i]:
            dfs(i)
            
    dist = [float('inf')] * v
    dist[src] = 0
    
    while stack:
        node = stack.pop()
        if dist[node] != float('inf'):
            for neighbor, weight in adj[node]:
                dist[neighbor] = min(dist[neighbor], dist[node] + weight)
                
    return [d if d != float('inf') else -1 for d in dist]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    edges = [(0, 1, 2), (0, 2, 1), (1, 2, 3)]
    assert optimal_solution(3, edges, 0) == [0, 2, 1]
    print("Done.")
