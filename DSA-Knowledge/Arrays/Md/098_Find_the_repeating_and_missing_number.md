# Find the repeating and missing number

## Difficulty
Medium

---

## Pattern
Mathematical Equations / Bitwise XOR

---

## Recognition Clues
- Given an unsorted array of size $N$. Elements are in range $[1, N]$.\n- One number appears twice (repeating) and one number is missing.\n- Goal is to find both in $O(N)$ time and $O(1)$ space.

---

## Core Insight
- **Mathematical Approach**: Let the repeating number be $A$ and missing number be $B$.\n- Calculate difference of sums: $\sum arr_i - \sum i = A - B$.\n- Calculate difference of squared sums: $\sum arr_i^2 - \sum i^2 = A^2 - B^2 = (A-B)(A+B)$.\n- Solve the system of equations for $A$ and $B$.

---

## Interview Explanation
1. **Brute Force Idea**: Use a frequency array or hash map to count the occurrences of each number from $1$ to $N$. The number with count 2 is repeating; the number with count 0 is missing.
2. **Why Inefficient**: Allocating a frequency array requires $O(N)$ space.
3. **Key Observation**: We can set up algebraic equations representing sum and sum of squares. Since we know the ideal sum of $[1, N]$ and the actual sum of the array, the difference gives us $A - B$. Similarly, the difference of squared sums gives us $A^2 - B^2$, which we can divide by $A - B$ to find $A + B$.
4. **Optimal Solution Intuition (Math)**:
   - Let `sum_n = N*(N+1)//2` and `sum_n2 = N*(N+1)*(2N+1)//6`.
   - Calculate `sum_arr = sum(arr)` and `sum_arr2 = sum(x*x for x in arr)`.
   - `val1 = sum_arr - sum_n` (this is $A - B$).
   - `val2 = sum_arr2 - sum_n2` (this is $A^2 - B^2$).
   - `val2 = val2 // val1` (this is $A + B$).
   - Solve: `A = (val1 + val2) // 2` and `B = val2 - A`.
5. **Time Complexity**: $O(N)$ (two running sum scans).
6. **Space Complexity**: $O(1)$ auxiliary space.

---

## Brute Force
- **Idea**: Use a count array of size $N+1$ to track frequencies.
- **Code**:
```python
def findRepeatingAndMissing_brute(arr):
    n = len(arr)
    freq = [0] * (n + 1)
    for x in arr:
        freq[x] += 1
    rep, mis = -1, -1
    for i in range(1, n + 1):
        if freq[i] == 2:
            rep = i
        elif freq[i] == 0:
            mis = i
    return [rep, mis]
```
- **TC**: $O(N)$
- **SC**: $O(N)$

---

## Optimal Approach
- **Algorithm**: Algebraic sum difference calculation.
- **Why it works**: Using summation invariants of the first $N$ integers and their squares provides a solvable system of equations, bypassing extra frequency arrays.
- **Complexity**: Time: $O(N)$, Space: $O(1)$.

---

## Optimal Code
```python
def findRepeatingAndMissing(arr):
    n = len(arr)
    
    # 1. Calculate ideal sums
    sum_n = n * (n + 1) // 2
    sum_n2 = n * (n + 1) * (2 * n + 1) // 6
    
    # 2. Calculate actual sums
    sum_arr = sum(arr)
    sum_arr2 = sum(x * x for x in arr)
    
    # val1 = A - B
    val1 = sum_arr - sum_n
    
    # val2 = A^2 - B^2
    val2 = sum_arr2 - sum_n2
    
    # A + B = (A^2 - B^2) / (A - B)
    val2 = val2 // val1
    
    # Solve for A (repeating) and B (missing)
    a = (val1 + val2) // 2
    b = val2 - a
    
    return [a, b]
```

---

## Test Cases
- **Normal Case**: Input: `arr = [3, 1, 2, 5, 3]`\n- Output: `[3, 4]` (repeating is 3, missing is 4)
- **Hard Case**: Input: `arr = [4, 3, 6, 2, 1, 1]`\n- Output: `[1, 5]`
- **Edge Case**: Input: `arr = [2, 2]`\n- Output: `[2, 1]`

---

## Common Mistakes
- Integer overflow in C++/Java when computing the sum of squares. Use 64-bit data types (`long long` in C++).\n- Swapping the output order (returning missing first instead of repeating).

---

## Killer Edge Cases
- Missing number is 1 or $N$.\n- Array size is 2.\n- Repeating number is larger than missing number or vice-versa.

---

## Follow-Up Variants
- Find Repeating and Missing $\rightarrow$ Find Duplicate Number (using Floyd's Tortoise and Hare).

---

## Similar Problems
- Find the Duplicate Number (LeetCode 287)\n- First Missing Positive (LeetCode 41)

---

## Theory Connections
- Algebraic Invariants: Modeling array permutations and corruptions as sum properties. When arithmetic overflow is a barrier, the Bitwise XOR method acts as a robust fallback.

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
