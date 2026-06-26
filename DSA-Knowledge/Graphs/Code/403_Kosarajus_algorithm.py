"""
LeetCode Link: https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1
Problem Name: Kosaraju's Algorithm (SCC)
Description: Count strongly connected components (SCC) in directed graph.

Folder: Graphs
File: 403_Kosarajus_algorithm.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight:
# 1. DFS to push nodes to stack by finishing times.
# 2. Transpose graph.
# 3. Pop stack, run DFS on transpose graph.
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[int]]) -> int:
    visited = [False] * v
    stack = []
    
    def dfs1(node):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs1(neighbor)
        stack.append(node)
        
    for i in range(v):
        if not visited[i]:
            dfs1(i)
            
    # Transpose Graph
    rev_adj = [[] for _ in range(v)]
    for u in range(v):
        for w in adj[u]:
            rev_adj[w].append(u)
            
    visited = [False] * v
    scc_count = 0
    
    def dfs2(node):
        visited[node] = True
        for neighbor in rev_adj[node]:
            if not visited[neighbor]:
                dfs2(neighbor)
                
    while stack:
        node = stack.pop()
        if not visited[node]:
            scc_count += 1
            dfs2(node)
            
    return scc_count

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[2, 3], [0], [1], [4], []]
    assert optimal_solution(5, adj) == 3 # {0,1,2}, {3}, {4}
    print("Done.")
