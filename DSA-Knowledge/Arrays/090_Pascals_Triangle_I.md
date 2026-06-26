# Pascals Triangle I

## Difficulty
Medium

---

## Pattern
Combinatorics / Dynamic Programming

---

## Recognition Clues
- Generate the first $N$ rows of Pascal's Triangle.\n- Each number is the sum of the two numbers directly above it.

---

## Core Insight
- Row $i$ has $i+1$ elements.\n- The first and last elements of each row are always 1.\n- The element at `row[j]` is equal to `prev_row[j-1] + prev_row[j]`.

---

## Interview Explanation
1. **Brute Force Idea**: Compute each element using the combinatorics formula $C(n, r) = rac{n!}{r!(n-r)!}$.
2. **Why Inefficient**: Computing factorials is slow and prone to overflow in fixed-width arithmetic.
3. **Key Observation**: The triangle has a simple recurrence relation. The value at index $j$ in row $i$ is the sum of indices $j-1$ and $j$ in row $i-1$. We can build the triangle row by row using this DP property.
4. **Optimal Solution Intuition**:
   - Create an empty list `ans`.
   - Loop `i` from 0 to $N-1$:
     - Initialize a row of size $i+1$ containing all 1s.
     - Loop `j` from 1 to `i-1`:
       - Set `row[j] = ans[i-1][j-1] + ans[i-1][j]`.
     - Append the row to `ans`.
5. **Time Complexity**: $O(N^2)$ (generating $N(N+1)/2$ cells).
6. **Space Complexity**: $O(N^2)$ (to store the generated triangle).

---

## Brute Force
- **Idea**: Compute each cell using combinatorial factorials $C(n, r)$.
- **Code**:
```python
import math
def generate_pascal_factorial(numRows):
    ans = []
    for i in range(numRows):
        row = []
        for j in range(i + 1):
            val = math.factorial(i) // (math.factorial(j) * math.factorial(i - j))
            row.append(val)
        ans.append(row)
    return ans
```
- **TC**: $O(N^3)$ due to factorial computations.
- **SC**: $O(N^2)$

---

## Optimal Approach
- **Algorithm**: Dynamic programming row generation.
- **Why it works**: Reusing calculated row values from the previous row reduces cell computation to a single addition, avoiding factorials.
- **Complexity**: Time: $O(N^2)$, Space: $O(N^2)$.

---

## Optimal Code
```python
def generatePascal(numRows):
    ans = []
    
    for i in range(numRows):
        # Initialize row with 1s
        row = [1] * (i + 1)
        
        # Fill middle elements using prev row values
        for j in range(1, i):
            row[j] = ans[i-1][j-1] + ans[i-1][j]
            
        ans.append(row)
        
    return ans
```

---

## Test Cases
- **Normal Case**: Input: `numRows = 5`\n- Output: `[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]`
- **Hard Case**: Input: `numRows = 1`\n- Output: `[[1]]`
- **Edge Case**: Input: `numRows = 2`\n- Output: `[[1],[1,1]]`

---

## Common Mistakes
- Off-by-one errors in inner loop range boundaries.\n- Not allocating 1s at the head and tail of each row.

---

## Killer Edge Cases
- numRows = 1\n- Large numRows values (python handles arbitrary large integers, but other languages might overflow).

---

## Follow-Up Variants
- Pascal's Triangle I (generate all) $\rightarrow$ Pascal's Triangle II (return only $K$-th row).

---

## Similar Problems
- Pascals Triangle II (LeetCode 119)\n- Triangle (LeetCode 120)

---

## Theory Connections
- Binomial Coefficients: The $k$-th element in the $n$-th row is equal to $\binom{n}{k}$. Pascal's recurrence relation matches the mathematical identity $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$.

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
