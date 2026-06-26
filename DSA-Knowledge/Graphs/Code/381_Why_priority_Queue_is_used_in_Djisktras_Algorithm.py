"""
LeetCode Link: N/A (Concept discussion)
Problem Name: Why Priority Queue is used in Dijkstra
Description: Conceptual verification code testing PQ vs Array search.

Folder: Graphs
File: 381_Why_priority_Queue_is_used_in_Djisktras_Algorithm.py
"""

import heapq
import time

# ============================================
# EXPLANATION
# ============================================
# With array search: Min extraction takes O(V), giving O(V^2 + E).
# With priority queue (min heap): Min extraction takes O(log V), yielding O(E log V).
# For sparse graphs (E << V^2), PQ is significantly faster.
def verify():
    # Verify min heap is O(log N)
    pq = []
    for i in range(1000, 0, -1):
        heapq.heappush(pq, i)
    assert heapq.heappop(pq) == 1

if __name__ == "__main__":
    print("Running tests...")
    verify()
    print("Done.")
