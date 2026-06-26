"""
LeetCode Link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
Problem Name: Find the City with the Smallest Number of Neighbors at a Threshold Distance
Description: Find city with smallest neighbors reachable within distanceThreshold.

Folder: Graphs
File: 390_Find_the_city_with_the_smallest_number_of_neighbors.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Floyd-Warshall to find shortest path matrix.
# Time Complexity: O(V^3)
# Space Complexity: O(V^2)
def optimal_solution(n: int, edges: list[list[int]], distanceThreshold: int) -> int:
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, w, d in edges:
        dist[u][w] = d
        dist[w][u] = d
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    min_count = float('inf')
    best_city = -1
    for i in range(n):
        count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
        if count <= min_count:
            min_count = count
            best_city = i
    return best_city

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
    assert optimal_solution(4, edges, 4) == 3
    print("Done.")
