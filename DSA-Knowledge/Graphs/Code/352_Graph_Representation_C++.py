"""
LeetCode Link: https://www.codingninjas.com/studio/problems/creating-and-printing-graphs_1214969
Problem Name: Graph Representation (Adjacency Matrix/List)
Description: Represent a graph using an adjacency list.

Folder: Graphs
File: 352_Graph_Representation_C++.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
def optimal_solution(v: int, edges: list[tuple[int, int]]) -> dict[int, list[int]]:
    adj = {i: [] for i in range(v)}
    for u, w in edges:
        adj[u].append(w)
        adj[w].append(u) # undirected
    return adj

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = optimal_solution(3, [(0, 1), (1, 2)])
    assert adj[1] == [0, 2]
    print("Done.")
