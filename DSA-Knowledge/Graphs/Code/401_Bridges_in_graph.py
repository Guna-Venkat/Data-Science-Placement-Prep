"""
LeetCode Link: https://leetcode.com/problems/critical-connections-in-a-network/
Problem Name: Critical Connections in a Network (Bridges)
Description: Find bridges in undirected graph using Tarjan's DFS bridge finder.

Folder: Graphs
File: 401_Bridges_in_graph.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(n: int, connections: list[list[int]]) -> list[list[int]]:
    adj = [[] for _ in range(n)]
    for u, w in connections:
        adj[u].append(w)
        adj[w].append(u)
        
    tin = [-1] * n
    low = [-1] * n
    timer = 0
    bridges = []
    
    def dfs(node, parent):
        nonlocal timer
        tin[node] = low[node] = timer
        timer += 1
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            if tin[neighbor] == -1:
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > tin[node]:
                    bridges.append([node, neighbor])
            else:
                low[node] = min(low[node], tin[neighbor])
                
    dfs(0, -1)
    return bridges

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    connections = [[0,1],[1,2],[2,0],[1,3]]
    res = optimal_solution(4, connections)
    assert res == [[1, 3]] or res == [[3, 1]]
    print("Done.")
