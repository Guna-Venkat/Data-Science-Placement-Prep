"""
LeetCode Link: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
Problem Name: Most Stones Removed with Same Row or Column
Description: Maximize stones removed if two share row or column.

Folder: Graphs
File: 396_Most_stones_removed_with_same_row_or_column.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Treat row and column indices as graph nodes. Union rows and cols.
# Time Complexity: O(N alpha(max_idx))
# Space Complexity: O(max_idx)
class DisjointSet:
    def __init__(self):
        self.parent = {}
    def find(self, i):
        if i not in self.parent:
            self.parent[i] = i
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

def optimal_solution(stones: list[list[int]]) -> int:
    ds = DisjointSet()
    for r, c in stones:
        # Offset column coordinates to prevent clash with rows
        ds.union(r, c + 10001)
        
    unique_roots = set(ds.find(x) for x in ds.parent)
    return len(stones) - len(unique_roots)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    assert optimal_solution(stones) == 5
    print("Done.")
