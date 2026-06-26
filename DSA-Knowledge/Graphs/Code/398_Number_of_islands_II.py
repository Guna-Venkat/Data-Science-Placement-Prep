"""
LeetCode Link: https://www.geeksforgeeks.org/problems/number-of-islands-ii/1
Problem Name: Number of Islands II
Description: Online queries. Count islands dynamically as land cells are populated.

Folder: Graphs
File: 398_Number_of_islands_II.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(Q alpha(R * C))
# Space Complexity: O(R * C)
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False

def optimal_solution(r: int, c: int, queries: list[list[int]]) -> list[int]:
    ds = DisjointSet(r * c)
    grid = [[0] * c for _ in range(r)]
    islands_count = 0
    res = []
    
    for row, col in queries:
        if grid[row][col] == 1:
            res.append(islands_count)
            continue
            
        grid[row][col] = 1
        islands_count += 1
        node = row * c + col
        
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < r and 0 <= nc < c and grid[nr][nc] == 1:
                neighbor = nr * c + nc
                if ds.union(node, neighbor):
                    islands_count -= 1
        res.append(islands_count)
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    queries = [[0,0], [0,1], [1,2], [2,1]]
    assert optimal_solution(3, 3, queries) == [1, 1, 2, 3]
    print("Done.")
