# Matrix Chain Multiplication

**Pattern:** Interval Dynamic Programming (DP on Ranges)

**Recognition:**
- Find the most efficient way to multiply a chain of matrices.
- Given array of dimensions where matrix $i$ has dimensions $arr[i-1] \times arr[i]$.
- Subproblem defined by partition interval: `dp[i][j]` is the minimum cost to multiply matrices from index `i` to `j`. Splitting points `k` range from `i` to `j-1`.

**Optimal Code (Python):**
```python
def matrixMultiplication(N: int, arr: list[int]) -> int:
    # dp[i][j] represents the minimum operations to multiply matrices from index i to j
    dp = [[0] * N for _ in range(N)]
    
    # l is the length of the matrix chain
    for l in range(2, N):
        for i in range(1, N - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            # Try all partition points k between i and j
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                dp[i][j] = min(dp[i][j], cost)
                
    return dp[1][N - 1]
```

**Killer Edge:**
- $N = 2$ (only one matrix exists, returns `0` since no multiplications are needed).
- Dimension values are large (cost calculation can exceed integer capacity in some languages, python handles arbitrarily large integers).

**Mistake:**
- Incorrect loop bounds: starting the chain length loop from `1` instead of `2` (single matrices do not require multiplication, cost is 0).
- Incorrect dimension indexing: using `arr[i] * arr[k] * arr[j]` instead of `arr[i - 1] * arr[k] * arr[j]`.
