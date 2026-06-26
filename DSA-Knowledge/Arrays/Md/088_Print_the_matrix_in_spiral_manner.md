# Print the matrix in spiral manner

## Difficulty
Medium

---

## Pattern
Boundary Simulation

---

## Recognition Clues
- Print/Return all elements of an $M \times N$ matrix in spiral order.\n- Starts from top-left, goes clockwise inwards.

---

## Core Insight
- Maintain four boundaries: `top`, `bottom`, `left`, `right`.\n- Traverse: top row, right column, bottom row (if boundaries permit), left column (if boundaries permit).\n- Shrink boundaries after each traversal step.

---

## Interview Explanation
1. **Brute Force Idea**: The simulation approach is the only way to solve this. There is no simple formula to jump coordinates.
2. **Why Inefficient**: We must visit every cell once, so $O(M \cdot N)$ is optimal.
3. **Key Observation**: We can model the spiral path as a series of concentric rectangular layers. By keeping pointers to the current boundaries of these layers, we can traverse them layer by layer.
4. **Optimal Solution Intuition**:
   - Set `top = 0`, `bottom = M - 1`, `left = 0`, `right = N - 1`.
   - Loop while `top <= bottom` and `left <= right`:
     - Traverse left-to-right along the `top` row, then increment `top`.
     - Traverse top-to-bottom along the `right` column, then decrement `right`.
     - If `top <= bottom`, traverse right-to-left along the `bottom` row, then decrement `bottom`.
     - If `left <= right`, traverse bottom-to-top along the `left` column, then increment `left`.
5. **Time Complexity**: $O(M \cdot N)$ (each cell is visited exactly once).
6. **Space Complexity**: $O(1)$ auxiliary space.

---

## Brute Force
- **Idea**: Simulate coordinate traversal using direction vectors and a visited matrix.
- **Code**:
```python
def spiralOrder_visited(matrix):
    if not matrix: return []
    R, C = len(matrix), len(matrix[0])
    seen = [[False] * C for _ in range(R)]
    ans = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = c = di = 0
    for _ in range(R * C):
        ans.append(matrix[r][c])
        seen[r][c] = True
        cr, cc = r + dr[di], c + dc[di]
        if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
            r, c = cr, cc
        else:
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]
    return ans
```
- **TC**: $O(M \cdot N)$
- **SC**: $O(M \cdot N)$ due to the visited matrix.

---

## Optimal Approach
- **Algorithm**: Boundary tracking simulation.
- **Why it works**: Updating boundary markers (`top`, `bottom`, `left`, `right`) prevents visiting cells twice, eliminating the need for a visited matrix.
- **Complexity**: Time: $O(M \cdot N)$, Space: $O(1)$ auxiliary space.

---

## Optimal Code
```python
def spiralOrder(matrix):
    if not matrix:
        return []
        
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    ans = []
    
    while top <= bottom and left <= right:
        # 1. Traverse top row (left to right)
        for j in range(left, right + 1):
            ans.append(matrix[top][j])
        top += 1
        
        # 2. Traverse right column (top to bottom)
        for i in range(top, bottom + 1):
            ans.append(matrix[i][right])
        right -= 1
        
        # 3. Traverse bottom row (right to left)
        if top <= bottom:
            for j in range(right, left - 1, -1):
                ans.append(matrix[bottom][j])
            bottom -= 1
            
        # 4. Traverse left column (bottom to top)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
            
    return ans
```

---

## Test Cases
- **Normal Case**: Input: `matrix = [[1,2,3],[4,5,6],[7,8,9]]`\n- Output: `[1,2,3,6,9,8,7,4,5]`
- **Hard Case**: Input: `matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]`\n- Output: `[1,2,3,4,8,12,11,10,9,5,6,7]`
- **Edge Case**: Input: `matrix = [[42]]`\n- Output: `[42]`

---

## Common Mistakes
- Forgetting to check the guard conditions `if top <= bottom` and `if left <= right` inside the loop, leading to duplicate visits to the center row/column in non-square matrices.\n- Off-by-one errors in decrementing boundary ranges.

---

## Killer Edge Cases
- Single row or single column matrix.\n- Square vs rectangular matrix shapes.\n- Single element matrix.

---

## Follow-Up Variants
- Print Spiral $\rightarrow$ Generate Spiral Matrix II (given $N$, generate $N \times N$ grid in spiral order).

---

## Similar Problems
- Spiral Matrix II (LeetCode 59)\n- Diagonal Traverse

---

## Theory Connections
- State Machine Simulation: The control flow handles multiple boundary invariants. This boundary contraction pattern is also used in matrix transpose, block multiplication, and parallel sub-grid processing.

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
