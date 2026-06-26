# Floyd-Warshall Algorithm

**Pattern:** Graph All-Pairs Shortest Path (Dynamic Programming)

**Recognition:**
- Find shortest paths between all pairs of vertices in a weighted directed graph.
- Handles negative edge weights (unlike Dijkstra) but not negative cycles.
- Small number of vertices ($V \le 400$), allowing for $O(V^3)$ time complexity.

**Optimal Code (Python):**
```python
def floydWarshall(matrix: list[list[int]]) -> None:
    n = len(matrix)
    
    # Preprocess: convert -1 (no edge) to infinity, set self-loops to 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == -1:
                matrix[i][j] = float('inf')
            if i == j:
                matrix[i][j] = 0
                
    # DP transitions: k is the intermediate vertex
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] != float('inf') and matrix[k][j] != float('inf'):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
                    
    # Postprocess: convert infinity back to -1 for representation
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == float('inf'):
                matrix[i][j] = -1
```

**Killer Edge:**
- Presence of a negative cycle (can be detected if `matrix[i][i] < 0` for any `i` after running the algorithm).
- Disconnected nodes with no path between them.

**Mistake:**
- Placing the loop for the intermediate vertex `k` as the inner-most loop. The `k` loop must be the **outer-most** loop to ensure all subpaths are correctly built step-by-step.
- Not checking if intermediate paths are unreachable (`matrix[i][k] == inf`), which could result in incorrect relaxations when subtracting negative weights.
