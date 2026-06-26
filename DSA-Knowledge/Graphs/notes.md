# Graphs - Topic Notes

## Patterns Learned

### 1. BFS and DFS Traversals
*   **Queue vs Stack**: BFS uses a queue (level-by-level shortest paths on unweighted graphs), DFS uses a recursive stack (deep exploration, pathfinding).
*   **Cycle Detection**:
    *   *Undirected Graph*: Keep track of current node and parent. If neighbor is visited and is not parent, cycle detected.
    *   *Directed Graph*: Keep tracking path visited list. If neighbor is on current DFS path, cycle detected.

### 2. Topological Sort (DAGs Only)
*   **DFS ordering**: Push node to stack after visiting all neighbors. Topo order is stack popped in reverse.
*   **Kahn's Algorithm (BFS)**: Compute indegrees of all nodes. Initialize queue with nodes having indegree 0. Pop, decrement neighbors' indegree. If any reaches 0, append to queue.
*   **Cycle Detection**: If Kahn's topo sort count is not equal to V, a cycle exists.

### 3. Shortest Paths Algorithms
*   **Dijkstra's Algorithm (Non-Negative Weights)**: Use min-heap to extract min distance node. Relax edges. Complexity: $O(E \log V)$.
*   **Bellman-Ford (Negative Weights Allowed)**: Relax all edges $V-1$ times. On $V$-th time, if any distance relaxes further, a negative cycle exists. Complexity: $O(V \cdot E)$.
*   **Floyd-Warshall (All Pairs Shortest Path)**: Dynamic programming grid update. Complexity: $O(V^3)$.

### 4. Minimum Spanning Trees (MST)
*   **Prim's Algorithm**: Start from arbitrary node. Pop min-weight edge using min-heap. Add to tree, push neighbors.
*   **Kruskal's Algorithm**: Sort all edges by weight. Sequentially union vertices using Disjoint Set. Skip if already in same component.

### 5. Disjoint Set Union (DSU)
*   **Operations**: `find(i)` and `union(i, j)`.
*   **Optimizations**: Path compression makes tree flat; Union by Rank/Size keeps tree height minimal. Complexity: $O(\alpha(N))$ (nearly constant).

### 6. Tarjan's Bridge and Articulation Finder
*   Maintain discovery time `tin` and lowest reachable time `low` using DFS.
*   **Bridge**: If `low[neighbor] > tin[node]`, edge is a bridge.
*   **Articulation Point**: If `low[neighbor] >= tin[node]` (and node is not root), node is an articulation point.

---

## Common Mistakes in Graphs

1.  **Duplicate Queue Insertion**: Forgetting to mark nodes as visited immediately upon adding to queue in BFS, leading to redundant checks and TLE/Memory limits.
2.  **Kahn's Algorithm Indegree tracking**: Missing updates to indegrees when building the graph or comparing node ranges.
3.  **Directed Cycle Check with Undirected Logic**: Attempting to use simple parent-checking logic on directed graphs, which incorrectly detects cycles on safe diamond-shaped structures.

---

## Edge Cases Specific to Graphs

*   **Disconnected Components**: Always run traversals from a loop $0 \dots V-1$ to ensure all components are visited.
*   **Self Loops and Multi-edges**: Check and handle self-loops or multi-edges appropriately in Union-Find or path cost calculations.
*   **Negative Cycles**: If a negative cycle exists, Dijkstra's algorithm will loop infinitely or yield incorrect distances. Use Bellman-Ford to check.
