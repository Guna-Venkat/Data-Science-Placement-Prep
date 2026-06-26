"""
LeetCode Link: https://leetcode.com/problems/is-graph-bipartite/
Problem Name: Is Graph Bipartite? (DFS)
Description: Determine if graph is bipartite (2-colorable).

Folder: Graphs
File: 369_Bipartite_Graph_DFS.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Bipartite graph is colorable using 2 colors such that adjacent vertices have different colors.
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(graph: list[list[int]]) -> bool:
    v = len(graph)
    colors = {} # node -> color (0 or 1)
    
    def dfs(node, color):
        colors[node] = color
        for neighbor in graph[node]:
            if neighbor not in colors:
                if not dfs(neighbor, 1 - color):
                    return False
            elif colors[neighbor] == color:
                return False
        return True
        
    for i in range(v):
        if i not in colors:
            if not dfs(i, 0):
                return False
    return True

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    graph = [[1,3],[0,2],[1,3],[0,2]]
    assert optimal_solution(graph) == True
    print("Done.")
