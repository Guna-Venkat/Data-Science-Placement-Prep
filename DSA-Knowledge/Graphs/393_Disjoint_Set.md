# Disjoint Set

**Pattern:** Disjoint Set Union (DSU) / Union-Find

**Recognition:**
- Dynamically track partitions/connectivity in a set of elements.
- Detect cycles in undirected graphs.
- Minimum Spanning Tree algorithms (specifically Kruskal's).
- Query whether two elements belong to the same component, or merge two components.

**Optimal Code (Python):**
```python
class DisjointSet:
    def __init__(self, n: int):
        # Supports 0-based and 1-based indexing of size n
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        # Path compression optimization
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union_by_rank(self, u: int, v: int) -> bool:
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u == root_v:
            return False  # Already in the same set (cycle detected if adding edge u-v)
            
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1
            
        return True

    def union_by_size(self, u: int, v: int) -> bool:
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u == root_v:
            return False
            
        if self.size[root_u] < self.size[root_v]:
            self.parent[root_u] = root_v
            self.size[root_v] += self.size[root_u]
        else:
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]
            
        return True
```

**Killer Edge:**
- Performing union operations on the same node (e.g., self-loop `union(u, u)`).
- Off-by-one errors when initializing for 1-based indexed graphs (initialize parent array of size `n + 1`).

**Mistake:**
- Omitting path compression in `find()`, resulting in tree degeneration into a linked list and search operations degrading to $O(N)$.
- Doing `parent[u] = v` instead of `parent[root_u] = root_v`, which breaks the tree structure by bypassing the representatives.
