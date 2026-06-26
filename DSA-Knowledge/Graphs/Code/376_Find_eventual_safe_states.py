"""
LeetCode Link: https://leetcode.com/problems/find-eventual-safe-states/
Problem Name: Find Eventual Safe States
Description: Find nodes which cannot lead to a cycle (ends in terminal nodes).

Folder: Graphs
File: 376_Find_eventual_safe_states.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Standard Kahn's algorithm by reversing edges. Safe nodes have indegree=0.
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
def optimal_solution(graph: list[list[int]]) -> list[int]:
    v = len(graph)
    rev_adj = [[] for _ in range(v)]
    indegree = [0] * v
    
    for u in range(v):
        for w in graph[u]:
            rev_adj[w].append(u)
            indegree[u] += 1
            
    queue = [i for i in range(v) if indegree[i] == 0]
    safe = [False] * v
    while queue:
        node = queue.pop(0)
        safe[node] = True
        for neighbor in rev_adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                
    return [i for i in range(v) if safe[i]]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    assert optimal_solution(graph) == [2, 4, 5, 6]
    print("Done.")
