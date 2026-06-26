"""
LeetCode Link: N/A
Problem Name: Disjoint Set (Union-Find)
Description: Implement Disjoint Set class with Rank and Path Compression.

Folder: Graphs
File: 393_Disjoint_Set.py
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
        self.parent[i] = self.find(self.parent[i]) # Path compression
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

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    ds = DisjointSet(5)
    ds.union(0, 1)
    ds.union(1, 2)
    assert ds.find(0) == ds.find(2)
    assert ds.find(0) != ds.find(3)
    print("Done.")
