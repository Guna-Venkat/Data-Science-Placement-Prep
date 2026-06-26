"""
LeetCode Link: https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
Problem Name: BFS Traversal of Graph
Description: Print Breadth-First Search traversal of a graph.

Folder: Graphs
File: 355_Traversal_Techniques.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[int]]) -> list[int]:
    bfs = []
    visited = [False] * v
    queue = [0]
    visited[0] = True
    
    while queue:
        node = queue.pop(0)
        bfs.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return bfs

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[1, 2], [0, 3], [0, 3], [1, 2]]
    assert optimal_solution(4, adj) == [0, 1, 2, 3]
    print("Done.")
