"""
LeetCode Link: https://leetcode.com/problems/maximal-rectangle/
Problem Name: Maximal Rectangle Area with all 1s
Description: Find largest rectangle area containing only 1s in a 2D matrix.

Folder: Dynamic_Programming
File: 457_Maximum_Rectangle_Area_with_all_1sDP_55.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: For each row, construct heights array (histogram). Find max area in histogram.
# Time Complexity: O(R * C)
# Space Complexity: O(C)
def max_histogram_area(heights):
    stack = []
    max_area = 0
    heights.append(0)
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else (i - stack[-1] - 1)
            max_area = max(max_area, height * width)
        stack.append(i)
    heights.pop()
    return max_area

def optimal_solution(matrix: list[list[str]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    cols = len(matrix[0])
    heights = [0] * cols
    max_rect = 0
    for row in matrix:
        for c in range(cols):
            heights[c] = heights[c] + 1 if row[c] == "1" else 0
        max_rect = max(max_rect, max_histogram_area(heights))
    return max_rect

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    assert optimal_solution(matrix) == 6
    print("Done.")
