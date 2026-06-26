"""
LeetCode Link: https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
Problem Name: Rat in a Maze
Description: Find all sorted paths for a rat to go from (0,0) to (N-1,N-1) in a grid of 0s and 1s.

Folder: Recursion
File: 200_Rat_in_a_Maze.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: DFS backtracking. Move in alphabetical order (D, L, R, U) to get sorted result paths.
# Time Complexity: O(3^(N^2))
# Space Complexity: O(N^2)
def optimal_solution(maze: list[list[int]]) -> list[str]:
    if not maze or maze[0][0] == 0:
        return []
        
    n = len(maze)
    result = []
    
    # Directions: Down, Left, Right, Up
    dirs = [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]
    
    def solve(r, c, path):
        if r == n - 1 and c == n - 1:
            result.append("".join(path))
            return
            
        temp = maze[r][c]
        maze[r][c] = 0 # mark visited
        
        for dr, dc, char in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == 1:
                path.append(char)
                solve(nr, nc, path)
                path.pop()
                
        maze[r][c] = temp # backtrack

    solve(0, 0, [])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 1, 1]]
    assert optimal_solution(maze) == ["DDRDRR", "DRDDRR"]
    print("Done.")
