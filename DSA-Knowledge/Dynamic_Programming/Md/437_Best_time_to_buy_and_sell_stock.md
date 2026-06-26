# Best Time to Buy and Sell Stock

**Pattern:** Linear Scan / Single Pass (Greedy / DP Variant)

**Recognition:**
- Find maximum profit from buying on one day and selling on a future day.
- Single transaction allowed.
- Keep track of the minimum price observed so far and check potential profit at each step.

**Optimal Code (Python):**
```python
def maxProfit(prices: list[int]) -> int:
    if not prices:
        return 0
        
    max_profit = 0
    min_price = prices[0]
    
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
        
    return max_profit
```

**Killer Edge:**
- Prices are in strictly decreasing order (e.g., `[7, 6, 5, 4, 3, 1]`) -> returns `0`.
- Array has a single element -> returns `0` (cannot buy and sell on the same day).
- All identical prices.

**Mistake:**
- Selling a stock before buying it (buying at a future index and selling at a past index).
- Initializing `min_price` to `0` (if price values are positive, `0` will never be updated and profit will be calculated incorrectly).
