"""
LeetCode Link: https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
Problem Name: Cycle Detection Undirected Graph (DFS)
Description: Detect cycle in undirected graph using DFS.

Folder: Graphs
File: 362_Detect_a_cycle_in_an_undirected_graph_dfs.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[int]]) -> bool:
    visited = [False] * v
    
    def dfs(node, parent):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
        
    for i in range(v):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[1], [0, 2, 3], [1, 3], [1, 2]]
    assert optimal_solution(4, adj) == True
    print("Done.")
