"""
LeetCode Link: https://leetcode.com/problems/sudoku-solver/
Problem Name: Sudoku Solver
Description: Solve a Sudoku puzzle in place.

Folder: Recursion
File: 203_Sudoku_Solver.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Try placing digits 1-9 on empty cells. Validate row, col, and 3x3 box constraint.
# Time Complexity: O(9^(N^2)) -> Constant O(1) for a 9x9 board
# Space Complexity: O(1)
def optimal_solution(board: list[list[str]]) -> bool:
    def is_valid(r, c, char):
        for i in range(9):
            if board[r][i] == char:
                return False
            if board[i][c] == char:
                return False
            # 3x3 box
            box_r = 3 * (r // 3) + i // 3
            box_c = 3 * (c // 3) + i % 3
            if board[box_r][box_c] == char:
                return False
        return True

    def solve():
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for char in "123456789":
                        if is_valid(r, c, char):
                            board[r][c] = char
                            if solve():
                                return True
                            board[r][c] = "." # backtrack
                    return False
        return True

    solve()
    return True

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    optimal_solution(board)
    assert board[0][2] == "4"
    print("Done.")
