# Dijkstra's Algorithm

**Pattern:** Graph Shortest Path (Greedy / Min-Heap Breadth First Search)

**Recognition:**
- Find the shortest path from a single source to all other vertices.
- Weighted graph with strictly non-negative edge weights.
- Employs a Min-Heap (priority queue) to greedily expand nodes with the smallest tentative distance.

**Optimal Code (Python):**
```python
import heapq

def dijkstra(V: int, adj: list[list[list[int]]], S: int) -> list[int]:
    # adj[u] contains pairs of [v, weight]
    dist = [float('inf')] * V
    dist[S] = 0
    
    # Priority Queue stores tuples: (distance, vertex)
    pq = [(0, S)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        # Optimization: skip processing if we have already found a shorter path to u
        if d > dist[u]:
            continue
            
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    return dist
```

**Killer Edge:**
- Graph has disconnected components (unreachable nodes maintain `float('inf')`).
- Graph contains negative edge weights (Dijkstra's greedy choice fails; Bellman-Ford should be used instead).
- Multi-edges between the same pair of nodes (correctly handled by min-heap relaxation).

**Mistake:**
- Omitting the `if d > dist[u]: continue` check, causing redundant updates for already relaxed nodes and risking TLE on dense graphs.
- Pushing the vertex first instead of distance in priority queue (`(u, d)` instead of `(d, u)`), which causes heapq to sort by vertex indices instead of distance.
