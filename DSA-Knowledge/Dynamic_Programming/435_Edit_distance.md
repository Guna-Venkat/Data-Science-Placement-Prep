# Edit Distance

**Pattern:** Multi-dimensional Dynamic Programming (DP on Strings / Sequence Alignment)

**Recognition:**
- Find minimum edit operations (Insert, Delete, Replace) to convert string A to string B.
- Transition options: if `s1[i-1] == s2[j-1]`, no operation required. Else, minimize cost over Insert (`dp[i][j-1]`), Delete (`dp[i-1][j]`), and Replace (`dp[i-1][j-1]`).

**Optimal Code (Python):**
```python
def minDistance(word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)
    # Space optimized: only keep previous and current row
    prev = list(range(m + 1))
    curr = [0] * (m + 1)
    
    for i in range(1, n + 1):
        curr[0] = i  # Base case: converting word1[0...i] to empty string word2[0] takes i deletes
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(
                    prev[j],     # Delete
                    curr[j - 1], # Insert
                    prev[j - 1]  # Replace
                )
        prev = curr[:]
        
    return prev[m]
```

**Killer Edge:**
- One string is completely empty (requires deleting all characters of the other, return `len(other)`).
- Both strings are empty (returns `0`).
- No common characters or exact length mismatch.

**Mistake:**
- Forgetting to initialize the first element of the current row `curr[0] = i` inside the outer loop.
- Counting the cost offset incorrectly when shifting indices to accommodate 1-based indexing for DP.
