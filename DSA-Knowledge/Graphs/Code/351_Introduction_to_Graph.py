"""
LeetCode Link: https://www.geeksforgeeks.org/problems/introduction-to-graph/1
Problem Name: Introduction to Graph
Description: Find the number of possible undirected graphs with V vertices.

Folder: Graphs
File: 351_Introduction_to_Graph.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Max number of edges in undirected graph is V * (V - 1) / 2.
# For each edge, we have 2 choices: present or absent.
# Time Complexity: O(1)
# Space Complexity: O(1)
def optimal_solution(v: int) -> int:
    if v <= 1:
        return 1
    edges = (v * (v - 1)) // 2
    return 2 ** edges

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(3) == 8
    assert optimal_solution(4) == 64
    print("Done.")
