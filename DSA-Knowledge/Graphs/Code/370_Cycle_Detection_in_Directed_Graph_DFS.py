"""
LeetCode Link: https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
Problem Name: Cycle Detection in Directed Graph (DFS)
Description: Detect cycle in directed graph using DFS. Keep tracking recursive stack path.

Folder: Graphs
File: 370_Cycle_Detection_in_Directed_Graph_DFS.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[int]]) -> bool:
    visited = [False] * v
    path_visited = [False] * v
    
    def dfs(node):
        visited[node] = True
        path_visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif path_visited[neighbor]:
                return True
        path_visited[node] = False
        return False
        
    for i in range(v):
        if not visited[i]:
            if dfs(i):
                return True
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[1], [2], [0]] # Cycle 0-1-2-0
    assert optimal_solution(3, adj) == True
    print("Done.")
