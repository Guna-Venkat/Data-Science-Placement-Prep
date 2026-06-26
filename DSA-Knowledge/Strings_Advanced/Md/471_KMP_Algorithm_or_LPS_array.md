# KMP Algorithm / LPS Array

**Pattern:** String Matching / Prefix Function (Knuth-Morris-Pratt)

**Recognition:**
- Find all occurrences of a pattern `pat` of length `M` in text `txt` of length `N` in $O(N + M)$ time.
- Avoid backtracking the text index `i` by utilizing a precomputed Longest Prefix Suffix (`LPS`) array.
- `lps[i]` stores the length of the longest proper prefix of `pat[0...i]` which is also a suffix of `pat[0...i]`.

**Optimal Code (Python):**
```python
def computeLPSArray(pat: str) -> list[int]:
    m = len(pat)
    lps = [0] * m
    length = 0  # length of the previous longest prefix suffix
    i = 1
    
    while i < m:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def KMP(pat: str, txt: str) -> list[int]:
    n, m = len(txt), len(pat)
    if m == 0:
        return []
        
    lps = computeLPSArray(pat)
    i = 0  # index for txt
    j = 0  # index for pat
    indices = []
    
    while i < n:
        if pat[j] == txt[i]:
            i += 1
            j += 1
            
        if j == m:
            indices.append(i - j)
            j = lps[j - 1]
        elif i < n and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return indices
```

**Killer Edge:**
- Overlapping pattern matches in text (e.g., searching for `aba` in `ababa` returns indices `[0, 2]`).
- Pattern is longer than the text.
- Repeated character chains (e.g. `pat = "aaaa"`, `txt = "aaaaaaaa"`).

**Mistake:**
- Backtracking the text pointer `i` manually during mismatch. KMP's signature advantage is that `i` **never** moves backwards.
- Setting `j = 0` after finding a mismatch instead of using `j = lps[j - 1]`, reducing the performance to brute force $O(N \cdot M)$ on pathological inputs.
