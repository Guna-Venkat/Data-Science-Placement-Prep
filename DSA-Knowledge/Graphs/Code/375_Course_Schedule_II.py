"""
LeetCode Link: https://leetcode.com/problems/course-schedule-ii/
Problem Name: Course Schedule II
Description: Return order in which courses should be taken.

Folder: Graphs
File: 375_Course_Schedule_II.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
def optimal_solution(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    adj = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for dest, src in prerequisites:
        adj[src].append(dest)
        indegree[dest] += 1
        
    queue = [i for i in range(numCourses) if indegree[i] == 0]
    order = []
    while queue:
        node = queue.pop(0)
        order.append(node)
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                
    return order if len(order) == numCourses else []

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(2, [[1,0]]) == [0, 1]
    print("Done.")
