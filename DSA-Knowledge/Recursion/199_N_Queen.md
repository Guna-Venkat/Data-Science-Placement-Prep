# N-Queen Problem

**Pattern:** Backtracking (State Space DFS Search)

**Recognition:**
- Place `N` non-attacking queens on an `N x N` chessboard.
- Classic constraint-satisfaction problem.
- Instead of checking the entire board for safety ($O(N)$), optimize validation to $O(1)$ lookup checks by tracking active attack paths using hash sets for columns (`col`), main diagonals (`row - col`), and anti-diagonals (`row + col`).

**Optimal Code (Python):**
```python
def solveNQueens(n: int) -> list[list[str]]:
    ans = []
    board = [["."] * n for _ in range(n)]
    
    # Hash sets to track occupied lines of attack in O(1) time
    cols = set()
    diagonals = set()      # row - col remains constant for main diagonals
    anti_diagonals = set() # row + col remains constant for anti-diagonals
    
    def backtrack(row: int) -> None:
        if row == n:
            # Found a valid configuration, capture current board state
            ans.append(["".join(r) for r in board])
            return
            
        for col in range(n):
            if col in cols or (row - col) in diagonals or (row + col) in anti_diagonals:
                continue
                
            # Place queen and update lines of attack
            cols.add(col)
            diagonals.add(row - col)
            anti_diagonals.add(row + col)
            board[row][col] = "Q"
            
            # Recurse to place queen in the next row
            backtrack(row + 1)
            
            # Backtrack: remove queen and restore state
            cols.remove(col)
            diagonals.remove(row - col)
            anti_diagonals.remove(row + col)
            board[row][col] = "."

    backtrack(0)
    return ans
```

**Killer Edge:**
- $N = 1$ (returns single configuration `[["Q"]]`).
- $N = 2$ or $N = 3$ (no valid solutions exist, returns empty list `[]`).

**Mistake:**
- Forgetting to revert the state (backtrack step) for the diagonal/column sets, which prevents other valid branches from being explored correctly.
- Scanning the board coordinates manually inside the validation step, which adds an unnecessary $O(N)$ overhead to each placement check.
