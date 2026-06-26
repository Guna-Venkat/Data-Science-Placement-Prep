"""
LeetCode Link: https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1
Problem Name: Floyd Warshall Algorithm
Description: All-pairs shortest path in-place grid update.

Folder: Graphs
File: 389_Floyd_warshall_algorithm.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V^3)
# Space Complexity: O(1) in-place updates
def optimal_solution(matrix: list[list[int]]) -> None:
    v = len(matrix)
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if matrix[i][k] != -1 and matrix[k][j] != -1:
                    val = matrix[i][k] + matrix[k][j]
                    if matrix[i][j] == -1 or matrix[i][j] > val:
                        matrix[i][j] = val

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    matrix = [[0, 2, -1], [-1, 0, 3], [1, -1, 0]]
    optimal_solution(matrix)
    assert matrix[0][2] == 5 # 0-1-2 path
    print("Done.")
