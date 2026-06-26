"""
LeetCode Link: https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
Problem Name: Cycle Detection Directed Graph (BFS)
Description: Detect cycle in directed graph using Kahn's algorithm (BFS). If Topo Sort size != V, cycle exists.

Folder: Graphs
File: 373_Detect_a_cycle_in_a_directed_graph_BFS.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[int]]) -> bool:
    indegree = [0] * v
    for i in range(v):
        for neighbor in adj[i]:
            indegree[neighbor] += 1
            
    queue = [i for i in range(v) if indegree[i] == 0]
    count = 0
    
    while queue:
        node = queue.pop(0)
        count += 1
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                
    return count != v

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[1], [2], [0]] # Cycle
    assert optimal_solution(3, adj) == True
    print("Done.")
