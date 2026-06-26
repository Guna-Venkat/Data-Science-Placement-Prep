"""
LeetCode Link: https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
Problem Name: Cycle Detection Undirected Graph (BFS)
Description: Detect cycle in undirected graph using BFS (parent mapping).

Folder: Graphs
File: 361_Cycle_Detection_in_Undirected_Graph_bfs.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[int]]) -> bool:
    visited = [False] * v
    
    def check_cycle(src):
        visited[src] = True
        queue = [(src, -1)] # (node, parent)
        while queue:
            node, parent = queue.pop(0)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    return True
        return False
        
    for i in range(v):
        if not visited[i]:
            if check_cycle(i):
                return True
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[1], [0, 2, 3], [1, 3], [1, 2]] # cycle 1-2-3-1
    assert optimal_solution(4, adj) == True
    print("Done.")
