"""
LeetCode Link: https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1
Problem Name: Minimum Multiplications to Reach End
Description: Find minimal multiplications mod 100000 to reach end starting from start.

Folder: Graphs
File: 387_Minimum_multiplications_to_reach_end.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: BFS over states mod 100000.
# Time Complexity: O(100000)
# Space Complexity: O(100000)
def optimal_solution(arr: list[int], start: int, end: int) -> int:
    MOD = 100000
    dist = [-1] * MOD
    dist[start] = 0
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        if node == end:
            return dist[node]
        for val in arr:
            nxt = (node * val) % MOD
            if dist[nxt] == -1:
                dist[nxt] = dist[node] + 1
                queue.append(nxt)
    return -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([2, 5, 7], 3, 30) == 2 # 3 * 2 * 5 = 30
    print("Done.")
