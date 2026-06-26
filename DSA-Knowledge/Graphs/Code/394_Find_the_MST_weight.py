"""
LeetCode Link: https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1
Problem Name: Find the MST weight (Kruskal's Algorithm)
Description: Kruskal's algorithm to compute MST weight using Union-Find.

Folder: Graphs
File: 394_Find_the_MST_weight.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

def optimal_solution(v: int, edges: list[list[int]]) -> int:
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(v)
    mst_weight = 0
    for u, w, wt in edges:
        if ds.union(u, w):
            mst_weight += wt
    return mst_weight

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    edges = [[0, 1, 2], [1, 2, 3], [0, 2, 1]]
    assert optimal_solution(3, edges) == 3
    print("Done.")
