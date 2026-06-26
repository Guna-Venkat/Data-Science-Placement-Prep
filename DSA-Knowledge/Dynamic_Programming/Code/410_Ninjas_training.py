"""
LeetCode Link: https://www.codingninjas.com/studio/problems/ninja-s-training_3621003
Problem Name: Ninja's Training
Description: Ninja performs 1 of 3 activities daily. Cannot perform same activity on consecutive days. Maximize merit points.

Folder: Dynamic_Programming
File: 410_Ninjas_training.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N * 4 * 3) = O(N)
# Space Complexity: O(1)
def optimal_solution(points: list[list[int]]) -> int:
    prev = [0] * 4
    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0][0], max(points[0][1], points[0][2]))
    
    n = len(points)
    for day in range(1, n):
        temp = [0] * 4
        for last in range(4):
            temp[last] = 0
            for task in range(3):
                if task != last:
                    pts = points[day][task] + prev[task]
                    temp[last] = max(temp[last], pts)
        prev = temp
    return prev[3]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    points = [[1, 2, 5], [3, 1, 1], [3, 3, 3]]
    assert optimal_solution(points) == 11
    print("Done.")
