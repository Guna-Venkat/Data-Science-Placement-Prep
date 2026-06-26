"""
LeetCode Link: https://www.geeksforgeeks.org/problems/articulation-point-1/1
Problem Name: Articulation Points in Graph
Description: Find articulation points (nodes whose removal increases connected components).

Folder: Graphs
File: 402_Articulation_point_in_graph.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(n: int, adj: list[list[int]]) -> list[int]:
    tin = [-1] * n
    low = [-1] * n
    is_articulation = [False] * n
    timer = 0
    
    def dfs(node, parent):
        nonlocal timer
        tin[node] = low[node] = timer
        timer += 1
        children = 0
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            if tin[neighbor] == -1:
                children += 1
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if parent != -1 and low[neighbor] >= tin[node]:
                    is_articulation[node] = True
            else:
                low[node] = min(low[node], tin[neighbor])
        if parent == -1 and children > 1:
            is_articulation[node] = True
            
    for i in range(n):
        if tin[i] == -1:
            dfs(i, -1)
            
    res = [i for i in range(n) if is_articulation[i]]
    return res if res else [-1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    # Graph: 0-1-2 and 1-3
    adj = [[1], [0, 2, 3], [1], [1]]
    assert optimal_solution(4, adj) == [1]
    print("Done.")
