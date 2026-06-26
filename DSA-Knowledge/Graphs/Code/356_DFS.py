"""
LeetCode Link: https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
Problem Name: DFS Traversal of Graph
Description: Print Depth-First Search traversal of a graph.

Folder: Graphs
File: 356_DFS.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[int]]) -> list[int]:
    dfs_result = []
    visited = [False] * v
    
    def dfs(node):
        visited[node] = True
        dfs_result.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
                
    dfs(0)
    return dfs_result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[1, 2], [0], [0]]
    assert optimal_solution(3, adj) == [0, 1, 2]
    print("Done.")
