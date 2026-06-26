"""
LeetCode Link: https://leetcode.com/problems/word-ladder-ii/
Problem Name: Word Ladder II
Description: Return all shortest transformation sequences.

Folder: Graphs
File: 367_Word_ladder_II.py
"""

import collections

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: BFS to find shortest path layer by layer. Backtrack using DFS to build paths.
# Time Complexity: O(N * L * 26 + Paths)
# Space Complexity: O(N * L)
def optimal_solution(beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
    word_set = set(wordList)
    if endWord not in word_set:
        return []
        
    # BFS to map parents and distance
    dist = {beginWord: 0}
    parents = collections.defaultdict(list)
    queue = [beginWord]
    found = False
    
    while queue and not found:
        next_queue = []
        visited_this_level = set()
        for word in queue:
            if word == endWord:
                found = True
                break
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + char + word[i+1:]
                    if next_word in word_set:
                        if next_word not in dist:
                            dist[next_word] = dist[word] + 1
                            next_queue.append(next_word)
                            parents[next_word].append(word)
                            visited_this_level.add(next_word)
                        elif dist[next_word] == dist[word] + 1:
                            parents[next_word].append(word)
                            
        # Commit to global word list removal only after level completes
        word_set -= visited_this_level
        queue = next_queue
        
    # DFS to reconstruct paths
    res = []
    def dfs(word, path):
        if word == beginWord:
            res.append(path[::-1])
            return
        for parent in parents[word]:
            dfs(parent, path + [parent])
            
    if found:
        dfs(endWord, [endWord])
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    res = optimal_solution("hit", "cog", ["hot","dot","dog","lot","log","cog"])
    assert len(res) > 0
    print("Done.")
