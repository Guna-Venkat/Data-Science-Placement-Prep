# Rotate matrix by 90 degrees

## Difficulty
Medium

---

## Pattern
Transpose and Reverse

---

## Recognition Clues
- Rotate an $N \times N$ 2D matrix by 90 degrees clockwise.\n- Must be rotated in-place (no auxiliary matrix allowed).

---

## Core Insight
- Transposing a matrix swaps elements across the diagonal: `matrix[i][j] <-> matrix[j][i]`.\n- Reversing each row of a transposed matrix results in a 90-degree clockwise rotation.

---

## Interview Explanation
1. **Brute Force Idea**: Create an auxiliary matrix of size $N \times N$. Copy element `matrix[i][j]` to `temp[j][N-1-i]`. Copy `temp` back.
2. **Why Inefficient**: Requires $O(N^2)$ extra space.
3. **Key Observation**: A 90-degree clockwise rotation is mathematically equivalent to transposing the matrix and then reversing each row horizontally.
4. **Optimal Solution Intuition**:
   - Transpose: Loop `i` from 0 to $N-1$ and `j` from `i + 1` to $N-1$. Swap `matrix[i][j]` with `matrix[j][i]`.
   - Reverse Rows: Loop through each row and reverse it in-place.
5. **Time Complexity**: $O(N^2)$ (each cell is swapped twice).
6. **Space Complexity**: $O(1)$ auxiliary space.

---

## Brute Force
- **Idea**: Use an auxiliary matrix of same dimensions to map rotated indices.
- **Code**:
```python
def rotate_brute(matrix):
    n = len(matrix)
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][n - 1 - i] = matrix[i][j]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = temp[i][j]
```
- **TC**: $O(N^2)$
- **SC**: $O(N^2)$

---

## Optimal Approach
- **Algorithm**: In-place transpose followed by row reversal.
- **Why it works**: Combining linear swaps across the diagonal and horizontal reflections produces the rotation rotation without allocating temporary grids.
- **Complexity**: Time: $O(N^2)$, Space: $O(1)$ auxiliary space.

---

## Optimal Code
```python
def rotate(matrix):
    n = len(matrix)
    
    # 1. Transpose the matrix (swap values across diagonal)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # 2. Reverse each row in-place
    for i in range(n):
        matrix[i].reverse()
```

---

## Test Cases
- **Normal Case**: Input: `matrix = [[1,2,3],[4,5,6],[7,8,9]]`\n- Output: `[[7,4,1],[8,5,2],[9,6,3]]`
- **Hard Case**: Input: `matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]`\n- Output: `[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]`
- **Edge Case**: Input: `matrix = [[1]]`\n- Output: `[[1]]`

---

## Common Mistakes
- Transposing the entire matrix instead of just the upper/lower triangle (swapping `(i, j)` twice returns elements to their starting positions).\n- Reversing columns instead of rows (which rotates 90 degrees counter-clockwise instead of clockwise).

---

## Killer Edge Cases
- Matrix has size $1 \times 1$.\n- Matrix contains identical values.\n- Matrix contains negative numbers.

---

## Follow-Up Variants
- Rotate 90 Clockwise $\rightarrow$ Rotate 90 Counter-Clockwise (transpose first, then reverse columns, or reverse rows first then transpose).

---

## Similar Problems
- Set Matrix Zeroes\n- Diagonal Traverse

---

## Theory Connections
- Affine Transformations / Linear Algebra: Clockwise 90-degree rotation is a composition of reflection (reversing) and transposition (reflecting across the main diagonal). Matrix operations of this type form the core of 2D/3D image processing packages.

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
