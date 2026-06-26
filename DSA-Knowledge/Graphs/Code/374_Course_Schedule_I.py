"""
LeetCode Link: https://leetcode.com/problems/course-schedule/
Problem Name: Course Schedule I
Description: Check if courses can be completed given prerequisite pair list.

Folder: Graphs
File: 374_Course_Schedule_I.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
def optimal_solution(numCourses: int, prerequisites: list[list[int]]) -> bool:
    adj = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for dest, src in prerequisites:
        adj[src].append(dest)
        indegree[dest] += 1
        
    queue = [i for i in range(numCourses) if indegree[i] == 0]
    count = 0
    while queue:
        node = queue.pop(0)
        count += 1
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return count == numCourses

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(2, [[1, 0]]) == True
    assert optimal_solution(2, [[1, 0], [0, 1]]) == False
    print("Done.")
