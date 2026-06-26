# Bellman-Ford Algorithm

**Pattern:** Graph Shortest Path (Dynamic Programming / Edge Relaxation)

**Recognition:**
- Find shortest paths from a single source in a weighted graph containing negative edge weights.
- Detect the presence of negative weight cycles.
- Principal property: in a graph with `V` vertices, the shortest path between any two vertices can contain at most `V - 1` edges.

**Optimal Code (Python):**
```python
def bellmanFord(V: int, edges: list[list[int]], S: int) -> list[int]:
    # edges list elements are: [u, v, weight]
    # Initialize distances. Using 1e8 as infinity per standard competitive programming conventions.
    dist = [int(1e8)] * V
    dist[S] = 0
    
    # Relax all edges V - 1 times
    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] != int(1e8) and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                
    # Check for negative weight cycles by relaxing edges one more time
    for u, v, w in edges:
        if dist[u] != int(1e8) and dist[u] + w < dist[v]:
            # A negative cycle exists if we can still find a shorter path
            return [-1]
            
    return dist
```

**Killer Edge:**
- Graph contains a negative cycle reachable from the source S (returns `[-1]`).
- Source node is part of a disconnected component but other components contain negative cycles.
- Vertices with infinite distances (must not relax their outgoing edges).

**Mistake:**
- Relaxing edges outgoing from vertices with distance infinity (`dist[u] == 1e8`). If `w` is negative, `inf + w` becomes less than `inf`, which is incorrect.
- Running the relaxation outer loop only $V-2$ times or cycle check immediately inside the loop.
