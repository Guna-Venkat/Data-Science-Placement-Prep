# Stock Buy and Sell

## Difficulty
Easy

---

## Pattern
Iterative / Single Pass (Greedy)

---

## Recognition Clues
- Determine the maximum profit obtainable from buying and selling a single stock.\n- Must buy before selling.

---

## Core Insight
- We want to find indices $i < j$ such that $prices[j] - prices[i]$ is maximized.\n- At any day $j$, the optimal day to have bought in the past is the day with the minimum price seen so far in $prices[0...j]$.

---

## Interview Explanation
1. **Brute Force Idea**: Compare every pair of days $(i, j)$ where $j > i$. Compute the profit $prices[j] - prices[i]$, and track the maximum profit.
2. **Why Inefficient**: Comparing all pairs takes $O(N^2)$ time.
3. **Key Observation**: If we sell on day $i$, the maximum profit is achieved if we bought at the lowest price seen between day 0 and day $i-1$.
4. **Optimal Solution Intuition**: Keep a running minimum price `min_price`. As we iterate through prices, update `min_price = min(min_price, price)`. Compute potential profit `price - min_price` and update `max_profit = max(max_profit, profit)`.
5. **Time Complexity**: $O(N)$.
6. **Space Complexity**: $O(1)$.

---

## Brute Force
- **Idea**: Compare all possible buy and sell pairs.
- **Code**:
```python
def max_profit_brute(prices):
    max_prof = 0
    n = len(prices)
    for i in range(n):
        for j in range(i + 1, n):
            max_prof = max(max_prof, prices[j] - prices[i])
    return max_prof
```
- **TC**: $O(N^2)$
- **SC**: $O(1)$

---

## Optimal Approach
- **Algorithm**: Single pass minimum-tracking.
- **Why it works**: Minimizing the purchase price dynamically gives the maximum margin for any potential sell date.
- **Complexity**: Time: $O(N)$, Space: $O(1)$.

---

## Optimal Code
```python
def maxProfit(prices):
    if not prices:
        return 0
        
    min_price = prices[0]
    max_prof = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_prof = max(max_prof, price - min_price)
        
    return max_prof
```

---

## Test Cases
- **Normal Case**: Input: `prices = [7, 1, 5, 3, 6, 4]`\n- Output: `5` (buy at 1, sell at 6)
- **Hard Case**: Input: `prices = [7, 6, 4, 3, 1]`\n- Output: `0` (monotonically decreasing, no profit)
- **Edge Case**: Input: `prices = [1, 2]`\n- Output: `1`

---

## Common Mistakes
- Buying and selling on the same day.\n- Selling before buying.

---

## Killer Edge Cases
- Prices are in descending order.\n- All prices are identical.\n- Single price element.

---

## Follow-Up Variants
- Stock Buy and Sell I $\rightarrow$ Stock Buy and Sell II (multiple transactions allowed)

---

## Similar Problems
- Best Time to Buy and Sell Stock II\n- Best Time to Buy and Sell Stock with Cooldown

---

## Theory Connections
- Greedy Choice Property: Local optimal choices (tracking the minimum price so far) lead to a global optimal solution (maximum margin profit).

---

## Personal Progress

**Confidence**
- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4
- [ ] 5

**Time Bucket**
- [ ] <10 min
- [ ] 10-20
- [ ] 20-40
- [ ] 40+

**Status**
- [ ] Not Attempted
- [ ] Hint Used
- [ ] Solved
- [ ] Mastered

**Revision Count**: 
**Last Revised**: 
**Next Review**: 

---

## Notes
