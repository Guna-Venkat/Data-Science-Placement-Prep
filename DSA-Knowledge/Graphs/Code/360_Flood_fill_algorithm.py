"""
LeetCode Link: https://leetcode.com/problems/flood-fill/
Problem Name: Flood Fill
Description: Change color of pixel and its 4-direction neighbors to target color.

Folder: Graphs
File: 360_Flood_fill_algorithm.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(R * C)
# Space Complexity: O(R * C) recursion stack
def optimal_solution(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    start_color = image[sr][sc]
    if start_color == color:
        return image
        
    rows, cols = len(image), len(image[0])
    
    def dfs(r, c):
        image[r][c] = color
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == start_color:
                dfs(nr, nc)
                
    dfs(sr, sc)
    return image

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    image = [[1,1,1],[1,1,0],[1,0,1]]
    res = optimal_solution(image, 1, 1, 2)
    assert res[1][1] == 2
    assert res[1][2] == 0
    print("Done.")
