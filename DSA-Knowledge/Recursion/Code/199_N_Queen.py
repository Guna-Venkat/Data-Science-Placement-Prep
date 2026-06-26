"""
LeetCode Link: https://leetcode.com/problems/n-queens/
Problem Name: N-Queens
Description: Place N queens on a chessboard such that no two queens attack each other.

Folder: Recursion
File: 199_N_Queen.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Backtracking column by column. Use hash sets to track occupied rows, 
# main diagonals (r - c), and anti-diagonals (r + c) in O(1) checks.
# Time Complexity: O(N!)
# Space Complexity: O(N)
def optimal_solution(n: int) -> list[list[str]]:
    result = []
    board = [["."] * n for _ in range(n)]
    
    cols = set()
    diag1 = set() # (r - c)
    diag2 = set() # (r + c)
    
    def backtrack(r):
        if r == n:
            result.append(["".join(row) for row in board])
            return
            
        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue
                
            board[r][c] = "Q"
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
            
            backtrack(r + 1)
            
            board[r][c] = "."
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)

    backtrack(0)
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    res = optimal_solution(4)
    assert len(res) == 2
    print("Done.")
