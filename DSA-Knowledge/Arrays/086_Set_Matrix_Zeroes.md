# Set Matrix Zeroes

## Difficulty
Medium

---

## Pattern
Vector Tracking / In-place Matrix

---

## Recognition Clues
- If an element in an $M \times N$ matrix is 0, set its entire row and column to 0.\n- Must perform this in-place.

---

## Core Insight
- If we set rows/columns to 0 immediately, we will lose track of which zeros were original and which were propagated.\n- We can use the first row and the first column of the matrix itself to store the zero states for the rest of the matrix.\n- Use two extra variables to store if the first row and column themselves need to be zeroed.

---

## Interview Explanation
1. **Brute Force Idea**: Create a copy of the matrix. For every zero in the original matrix, set the corresponding row and column to zero in the copy. Copy it back.
2. **Why Inefficient**: Creating a copy takes $O(M \cdot N)$ space. Alternatively, tracking rows and columns using two arrays takes $O(M + N)$ space.
3. **Key Observation**: We can use the first row and column of the matrix as our tracking arrays, saving that space.
4. **Optimal Solution Intuition**:
   - Check if the first row contains any zeros (store in `row0` boolean).
   - Check if the first column contains any zeros (store in `col0` boolean).
   - Scan the rest of the matrix `matrix[1...M-1][1...N-1]`. If `matrix[i][j] == 0`, set `matrix[i][0] = 0` and `matrix[0][j] = 0`.
   - Iterate through the submatrix and update `matrix[i][j] = 0` if `matrix[i][0] == 0` or `matrix[0][j] == 0`.
   - Finally, zero out the first row and column if `row0` or `col0` are True.
5. **Time Complexity**: $O(M \cdot N)$ (two scans of the matrix).
6. **Space Complexity**: $O(1)$ auxiliary space.

---

## Brute Force
- **Idea**: Use auxiliary arrays of size $M$ and $N$ to track which rows and columns should be zeroed.
- **Code**:
```python
def setZeroes_brute(matrix):
    r, c = len(matrix), len(matrix[0])
    rows = [False] * r
    cols = [False] * c
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                rows[i] = True
                cols[j] = True
    for i in range(r):
        for j in range(c):
            if rows[i] or cols[j]:
                matrix[i][j] = 0
```
- **TC**: $O(M \cdot N)$
- **SC**: $O(M + N)$

---

## Optimal Approach
- **Algorithm**: In-place state marking using first row and column.
- **Why it works**: Repurposing the matrix's boundaries as tracking cells avoids extra allocation, bringing auxiliary space down to $O(1)$.
- **Complexity**: Time: $O(M \cdot N)$, Space: $O(1)$ auxiliary space.

---

## Optimal Code
```python
def setZeroes(matrix):
    r, c = len(matrix), len(matrix[0])
    row0 = False
    col0 = False
    
    # 1. Determine if first row or first column has zero
    for i in range(r):
        if matrix[i][0] == 0:
            col0 = True
    for j in range(c):
        if matrix[0][j] == 0:
            row0 = True
            
    # 2. Use first row and column to mark zero states
    for i in range(1, r):
        for j in range(1, c):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
                
    # 3. Set cells to zero based on marks
    for i in range(1, r):
        for j in range(1, c):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
                
    # 4. Zero out first row and column if needed
    if col0:
        for i in range(r):
            matrix[i][0] = 0
    if row0:
        for j in range(c):
            matrix[0][j] = 0
```

---

## Test Cases
- **Normal Case**: Input: `matrix = [[1,1,1],[1,0,1],[1,1,1]]`\n- Output: `[[1,0,1],[0,0,0],[1,0,1]]`
- **Hard Case**: Input: `matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]`\n- Output: `[[0,0,0,0],[0,4,5,0],[0,3,1,0]]`
- **Edge Case**: Input: `matrix = [[1]]`\n- Output: `[[1]]`

---

## Common Mistakes
- Updating the first row/column cells immediately while scanning, which falsely propagates zeros to other rows/columns.\n- Forgetting to handle the first row and column state updates separately at the end.

---

## Killer Edge Cases
- Matrix has only 1 row or 1 column.\n- All elements are already 0.\n- No zeros in the matrix.

---

## Follow-Up Variants
- Set Matrix Zeroes $\rightarrow$ Set Matrix Zeroes with cell value constraints.

---

## Similar Problems
- Game of Life\n- Rotate Image

---

## Theory Connections
- State Encoding: Storing tracking flags in-place by reusing existing cells. This is a common design pattern in system-level memory optimizations where bit-packing or flag-sharing is required.

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
