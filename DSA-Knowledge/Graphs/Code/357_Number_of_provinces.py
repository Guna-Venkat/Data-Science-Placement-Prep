"""
LeetCode Link: https://leetcode.com/problems/number-of-provinces/
Problem Name: Number of Provinces
Description: Count total connected components in an adjacency matrix.

Folder: Graphs
File: 357_Number_of_provinces.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V^2)
# Space Complexity: O(V)
def optimal_solution(isConnected: list[list[int]]) -> int:
    v = len(isConnected)
    visited = set()
    provinces = 0
    
    def dfs(node):
        for neighbor in range(v):
            if isConnected[node][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)
                
    for i in range(v):
        if i not in visited:
            provinces += 1
            visited.add(i)
            dfs(i)
    return provinces

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    matrix = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    assert optimal_solution(matrix) == 2
    print("Done.")
