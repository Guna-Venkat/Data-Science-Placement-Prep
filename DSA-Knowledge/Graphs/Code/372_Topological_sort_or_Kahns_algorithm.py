"""
LeetCode Link: https://www.geeksforgeeks.org/problems/topological-sort/1
Problem Name: Topological Sort (Kahn's Algorithm BFS)
Description: Topo sort using Kahn's algorithm (indegree).

Folder: Graphs
File: 372_Topological_sort_or_Kahns_algorithm.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[int]]) -> list[int]:
    indegree = [0] * v
    for i in range(v):
        for neighbor in adj[i]:
            indegree[neighbor] += 1
            
    queue = [i for i in range(v) if indegree[i] == 0]
    topo = []
    
    while queue:
        node = queue.pop(0)
        topo.append(node)
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return topo

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[], [], [3], [1], [0, 1], [0, 2]]
    res = optimal_solution(6, adj)
    assert len(res) == 6
    print("Done.")
