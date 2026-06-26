"""
LeetCode Link: https://leetcode.com/problems/word-search/
Problem Name: Word Search
Description: Return True if a word exists in a 2D board.

Folder: Recursion
File: 198_Word_Search.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: DFS backtracking. Mark cells visited by changing value, then restore (backtrack).
# Time Complexity: O(R * C * 4^L) where L is length of word
# Space Complexity: O(L) recursion stack depth
def optimal_solution(board: list[list[str]], word: str) -> bool:
    if not board:
        return False
        
    rows = len(board)
    cols = len(board[0])
    
    def dfs(r, c, idx):
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
            return False
            
        temp = board[r][c]
        board[r][c] = "#" # mark visited
        
        # Directions
        found = (dfs(r+1, c, idx+1) or
                 dfs(r-1, c, idx+1) or
                 dfs(r, c+1, idx+1) or
                 dfs(r, c-1, idx+1))
                 
        board[r][c] = temp # backtrack
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert optimal_solution(board, "ABCCED") == True
    assert optimal_solution(board, "SEE") == True
    assert optimal_solution(board, "ABCB") == False
    print("Done.")
