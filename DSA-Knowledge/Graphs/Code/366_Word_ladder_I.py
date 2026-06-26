"""
LeetCode Link: https://leetcode.com/problems/word-ladder/
Problem Name: Word Ladder I
Description: Find shortest transformation sequence length from beginWord to endWord.

Folder: Graphs
File: 366_Word_ladder_I.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: BFS level order. Mutate characters to find matches.
# Time Complexity: O(N * L * 26) where L is word length
# Space Complexity: O(N)
def optimal_solution(beginWord: str, endWord: str, wordList: list[str]) -> int:
    words = set(wordList)
    if endWord not in words:
        return 0
        
    queue = [(beginWord, 1)]
    while queue:
        word, steps = queue.pop(0)
        if word == endWord:
            return steps
            
        for i in range(len(word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                next_word = word[:i] + char + word[i+1:]
                if next_word in words:
                    words.remove(next_word)
                    queue.append((next_word, steps + 1))
    return 0

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    print("Done.")
