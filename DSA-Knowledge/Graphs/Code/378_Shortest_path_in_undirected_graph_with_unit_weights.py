"""
LeetCode Link: https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1
Problem Name: Shortest Path in Undirected Graph with Unit Weights
Description: Find shortest path from source to all vertices.

Folder: Graphs
File: 378_Shortest_path_in_undirected_graph_with_unit_weights.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: BFS traversal starting from source node.
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, edges: list[tuple[int, int]], src: int) -> list[int]:
    adj = [[] for _ in range(v)]
    for u, w in edges:
        adj[u].append(w)
        adj[w].append(u)
        
    dist = [-1] * v
    dist[src] = 0
    queue = [src]
    
    while queue:
        node = queue.pop(0)
        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    edges = [(0, 1), (1, 2), (0, 2)]
    assert optimal_solution(3, edges, 0) == [0, 1, 1]
    print("Done.")
