"""
LeetCode Link: https://www.geeksforgeeks.org/problems/alien-dictionary/1
Problem Name: Alien Dictionary
Description: Find alphabetical order of characters in alien language.

Folder: Graphs
File: 377_Alien_Dictionary.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Compare adjacent words. Build dependency graph. Topo Sort characters.
# Time Complexity: O(N * L + K)
# Space Complexity: O(K)
def optimal_solution(words: list[str], k: int) -> str:
    adj = {i: [] for i in range(k)}
    indegree = {i: 0 for i in range(k)}
    
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                idx1 = ord(c1) - ord('a')
                idx2 = ord(c2) - ord('a')
                if idx2 not in adj[idx1]:
                    adj[idx1].append(idx2)
                    indegree[idx2] += 1
                break
                
    queue = [i for i in range(k) if indegree[i] == 0]
    order = []
    while queue:
        node = queue.pop(0)
        order.append(chr(node + ord('a')))
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                
    return "".join(order)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(["baa", "abcd", "abca", "cab", "cada"], 4) == "bdac"
    print("Done.")
