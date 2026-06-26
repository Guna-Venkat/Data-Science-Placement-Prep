"""
LeetCode Link: https://leetcode.com/problems/number-of-operations-to-make-network-connected/
Problem Name: Number of Operations to Make Network Connected
Description: Find minimal operations (cables moved) to connect all computers.

Folder: Graphs
File: 395_Number_of_operations_to_make_network_connected.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Union-Find to count redundant cables and connected components.
# Time Complexity: O(E alpha(V))
# Space Complexity: O(V)
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

def optimal_solution(n: int, connections: list[list[int]]) -> int:
    if len(connections) < n - 1:
        return -1
        
    ds = DisjointSet(n)
    components = n
    for u, w in connections:
        if ds.union(u, w):
            components -= 1
            
    return components - 1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(4, [[0,1],[0,2],[1,2]]) == 1
    print("Done.")
