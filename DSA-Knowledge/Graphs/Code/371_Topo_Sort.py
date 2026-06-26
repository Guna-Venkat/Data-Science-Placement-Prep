"""
LeetCode Link: https://www.geeksforgeeks.org/problems/topological-sort/1
Problem Name: Topological Sort (DFS)
Description: Topo sort of Directed Acyclic Graph (DAG) using DFS.

Folder: Graphs
File: 371_Topo_Sort.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[int]]) -> list[int]:
    visited = [False] * v
    stack = []
    
    def dfs(node):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)
        
    for i in range(v):
        if not visited[i]:
            dfs(i)
            
    return stack[::-1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[], [], [3], [1], [0, 1], [0, 2]]
    res = optimal_solution(6, adj)
    # verify topological sort properties
    pos = {val: idx for idx, val in enumerate(res)}
    assert pos[5] < pos[2]
    assert pos[2] < pos[3]
    print("Done.")
