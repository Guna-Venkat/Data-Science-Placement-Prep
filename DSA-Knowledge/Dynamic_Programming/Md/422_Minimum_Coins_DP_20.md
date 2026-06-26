# Minimum Coins

**Pattern:** Dynamic Programming (Unbounded Knapsack / Coin Change Variant)

**Recognition:**
- Minimize the total number of items (coins) to achieve a target value.
- Items can be reused an infinite number of times (unbounded supply).
- Optimal substructure: the minimum coins for sum `V` depends on the minimum coins for `V - coin`.

**Optimal Code (Python):**
```python
def minCoins(coins: list[int], V: int) -> int:
    # dp[i] stores the minimum coins required to make change for amount i
    dp = [float('inf')] * (V + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0
    
    for i in range(1, V + 1):
        for coin in coins:
            if i - coin >= 0:
                sub_res = dp[i - coin]
                if sub_res != float('inf'):
                    dp[i] = min(dp[i], sub_res + 1)
                    
    return dp[V] if dp[V] != float('inf') else -1
```

**Killer Edge:**
- Target value `V` is 0 (returns `0`).
- No combination of coins can sum up to `V` (returns `-1`).
- Large `V` with small coin values (requires $O(V \cdot \text{len(coins)})$ time complexity).

**Mistake:**
- Initializing DP array with a arbitrary large number (like `99999`) which can be smaller than the actual minimum coins if `V` is huge.
- Forgetting to check if `dp[i - coin]` is valid (`float('inf')`) before adding `1`, which would conceptually result in `inf + 1`.
