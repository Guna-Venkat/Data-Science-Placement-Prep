"""
LeetCode Link: https://www.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1
Problem Name: M-Coloring Problem
Description: Color a graph using at most M colors such that no adjacent vertices have the same color.

Folder: Recursion
File: 202_M_Coloring_Problem.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Assign colors vertex by vertex. Check adjacency safety. Backtrack if unsafe.
# Time Complexity: O(M^V)
# Space Complexity: O(V)
def optimal_solution(graph: list[list[int]], m: int, v: int) -> bool:
    # graph representation is adjacency matrix
    colors = [0] * v
    
    def is_safe(node, color):
        for i in range(v):
            if graph[node][i] == 1 and colors[i] == color:
                return False
        return True

    def solve(node):
        if node == v:
            return True
            
        for c in range(1, m + 1):
            if is_safe(node, c):
                colors[node] = c
                if solve(node + 1):
                    return True
                colors[node] = 0 # backtrack
        return False

    return solve(0)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    # 4 vertices triangle graph with one disconnected node or similar
    graph = [[0, 1, 1, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 1],
             [1, 0, 1, 0]]
    assert optimal_solution(graph, 3, 4) == True
    print("Done.")
