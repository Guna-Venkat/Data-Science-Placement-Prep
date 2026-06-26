"""
LeetCode Link: https://leetcode.com/problems/surrounded-regions/
Problem Name: Surrounded Regions
Description: Capture surrounded regions ('O') by converting them to 'X'. Border 'O's cannot be captured.

Folder: Graphs
File: 364_Surrounded_Regions.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Find border 'O's. Run DFS to mark connected 'O's as '#'. Convert rest to 'X', '#' to 'O'.
# Time Complexity: O(R * C)
# Space Complexity: O(R * C) recursion stack
def optimal_solution(board: list[list[str]]) -> None:
    if not board:
        return
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c):
        board[r][c] = "#"
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                dfs(nr, nc)
                
    for r in range(rows):
        if board[r][0] == "O": dfs(r, 0)
        if board[r][cols - 1] == "O": dfs(r, cols - 1)
    for c in range(cols):
        if board[0][c] == "O": dfs(0, c)
        if board[rows - 1][c] == "O": dfs(rows - 1, c)
        
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "#":
                board[r][c] = "O"

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    optimal_solution(board)
    assert board[1][1] == "X"
    assert board[3][1] == "O" # boundary O kept
    print("Done.")
