"""
LeetCode Link: https://www.codingninjas.com/studio/problems/creating-and-printing-graphs_1214969
Problem Name: Graph Representation Java
Description: Build a directed adjacency list representation.

Folder: Graphs
File: 353_Graph_Representation_Java.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
def optimal_solution(v: int, edges: list[tuple[int, int]]) -> dict[int, list[int]]:
    adj = {i: [] for i in range(v)}
    for u, w in edges:
        adj[u].append(w)
    return adj

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = optimal_solution(3, [(0, 1), (1, 2)])
    assert adj[0] == [1]
    assert adj[1] == [2]
    print("Done.")
