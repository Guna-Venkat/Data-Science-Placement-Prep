# Longest Common Subsequence

**Pattern:** Multi-dimensional Dynamic Programming (DP on Strings / Subsequences)

**Recognition:**
- Given two sequences, find the length of the longest subsequence present in both.
- Subsequence elements do not need to be contiguous but must preserve relative ordering.
- Decision tree at each step: if characters match, include them; if they don't, skip one character from either string.

**Optimal Code (Python):**
```python
def lcs(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    # Space optimized: only keep track of previous and current rows
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr[:]
        
    return prev[m]
```

**Killer Edge:**
- One or both strings are empty (returns `0`).
- No matching characters between the two strings (returns `0`).
- Both strings are identical (returns length of the string).

**Mistake:**
- Using 2D DP array with size $O(N \cdot M)$ when space can be optimized to $O(\min(N, M))$ by making the smaller string represent columns.
- Mismatching indices: comparing `s1[i]` with `s2[j]` instead of `s1[i - 1]` with `s2[j - 1]` due to index shifting.
