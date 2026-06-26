"""
LeetCode Link: https://leetcode.com/problems/number-of-provinces/
Problem Name: Connected Components
Description: Count number of connected components in undirected graph.

Folder: Graphs
File: 354_Connected_Components.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: dict[int, list[int]]) -> int:
    visited = set()
    count = 0
    
    def dfs(node):
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)
                
    for i in range(v):
        if i not in visited:
            count += 1
            visited.add(i)
            dfs(i)
    return count

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = {0: [1], 1: [0], 2: []}
    assert optimal_solution(3, adj) == 2
    print("Done.")
