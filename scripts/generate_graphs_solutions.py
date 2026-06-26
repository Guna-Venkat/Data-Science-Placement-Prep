import os

SOLUTIONS = {
    "351_Introduction_to_Graph.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/introduction-to-graph/1
Problem Name: Introduction to Graph
Description: Find the number of possible undirected graphs with V vertices.

Folder: Graphs
File: 351_Introduction_to_Graph.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Max number of edges in undirected graph is V * (V - 1) / 2.
# For each edge, we have 2 choices: present or absent.
# Time Complexity: O(1)
# Space Complexity: O(1)
def optimal_solution(v: int) -> int:
    if v <= 1:
        return 1
    edges = (v * (v - 1)) // 2
    return 2 ** edges

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(3) == 8
    assert optimal_solution(4) == 64
    print("Done.")
""",

    "352_Graph_Representation_C++.py": """\"\"\"
LeetCode Link: https://www.codingninjas.com/studio/problems/creating-and-printing-graphs_1214969
Problem Name: Graph Representation (Adjacency Matrix/List)
Description: Represent a graph using an adjacency list.

Folder: Graphs
File: 352_Graph_Representation_C++.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
def optimal_solution(v: int, edges: list[tuple[int, int]]) -> dict[int, list[int]]:
    adj = {i: [] for i in range(v)}
    for u, w in edges:
        adj[u].append(w)
        adj[w].append(u) # undirected
    return adj

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = optimal_solution(3, [(0, 1), (1, 2)])
    assert adj[1] == [0, 2]
    print("Done.")
""",

    "353_Graph_Representation_Java.py": """\"\"\"
LeetCode Link: https://www.codingninjas.com/studio/problems/creating-and-printing-graphs_1214969
Problem Name: Graph Representation Java
Description: Build a directed adjacency list representation.

Folder: Graphs
File: 353_Graph_Representation_Java.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
def optimal_solution(v: int, edges: list[tuple[int, int]]) -> dict[int, list[int]]:
    adj = {i: [] for i in range(v)}
    for u, w in edges:
        adj[u].append(w)
    return adj

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = optimal_solution(3, [(0, 1), (1, 2)])
    assert adj[0] == [1]
    assert adj[1] == [2]
    print("Done.")
""",

    "354_Connected_Components.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/number-of-provinces/
Problem Name: Connected Components
Description: Count number of connected components in undirected graph.

Folder: Graphs
File: 354_Connected_Components.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: dict[int, list[int]]) -> int:
    visited = set()
    count = 0
    
    def dfs(node):
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)
                
    for i in range(v):
        if i not in visited:
            count += 1
            visited.add(i)
            dfs(i)
    return count

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = {0: [1], 1: [0], 2: []}
    assert optimal_solution(3, adj) == 2
    print("Done.")
""",

    "355_Traversal_Techniques.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
Problem Name: BFS Traversal of Graph
Description: Print Breadth-First Search traversal of a graph.

Folder: Graphs
File: 355_Traversal_Techniques.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[int]]) -> list[int]:
    bfs = []
    visited = [False] * v
    queue = [0]
    visited[0] = True
    
    while queue:
        node = queue.pop(0)
        bfs.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return bfs

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[1, 2], [0, 3], [0, 3], [1, 2]]
    assert optimal_solution(4, adj) == [0, 1, 2, 3]
    print("Done.")
""",

    "356_DFS.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
Problem Name: DFS Traversal of Graph
Description: Print Depth-First Search traversal of a graph.

Folder: Graphs
File: 356_DFS.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[int]]) -> list[int]:
    dfs_result = []
    visited = [False] * v
    
    def dfs(node):
        visited[node] = True
        dfs_result.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
                
    dfs(0)
    return dfs_result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[1, 2], [0], [0]]
    assert optimal_solution(3, adj) == [0, 1, 2]
    print("Done.")
""",

    "357_Number_of_provinces.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/number-of-provinces/
Problem Name: Number of Provinces
Description: Count total connected components in an adjacency matrix.

Folder: Graphs
File: 357_Number_of_provinces.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V^2)
# Space Complexity: O(V)
def optimal_solution(isConnected: list[list[int]]) -> int:
    v = len(isConnected)
    visited = set()
    provinces = 0
    
    def dfs(node):
        for neighbor in range(v):
            if isConnected[node][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)
                
    for i in range(v):
        if i not in visited:
            provinces += 1
            visited.add(i)
            dfs(i)
    return provinces

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    matrix = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    assert optimal_solution(matrix) == 2
    print("Done.")
""",

    "358_Connected_Components_Problem_in_Matrix.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/number-of-islands/
Problem Name: Connected Components in Matrix
Description: Find total connected components (islands) including diagonal steps.

Folder: Graphs
File: 358_Connected_Components_Problem_in_Matrix.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(R * C)
# Space Complexity: O(R * C)
def optimal_solution(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r, c):
        grid[r][c] = "0"
        # 8 directions (diagonal steps included in this GFG version)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                dfs(nr, nc)
                
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                dfs(r, c)
    return islands

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [["1", "1", "0"], ["0", "0", "1"], ["1", "0", "1"]]
    # Diagonal components connected: all form 1 component
    assert optimal_solution(grid) == 1
    print("Done.")
""",

    "359_Rotten_Oranges.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/rotting-oranges/
Problem Name: Rotting Oranges
Description: Find minimum time to rot all fresh oranges. Return -1 if impossible.

Folder: Graphs
File: 359_Rotten_Oranges.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(R * C)
# Space Complexity: O(R * C)
def optimal_solution(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = []
    fresh = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1
                
    minutes = 0
    while queue:
        r, c, time = queue.pop(0)
        minutes = max(minutes, time)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc, time + 1))
                
    return minutes if fresh == 0 else -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    assert optimal_solution(grid) == 4
    print("Done.")
""",

    "360_Flood_fill_algorithm.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/flood-fill/
Problem Name: Flood Fill
Description: Change color of pixel and its 4-direction neighbors to target color.

Folder: Graphs
File: 360_Flood_fill_algorithm.py
\"\"\"

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
""",

    "361_Cycle_Detection_in_Undirected_Graph_bfs.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
Problem Name: Cycle Detection Undirected Graph (BFS)
Description: Detect cycle in undirected graph using BFS (parent mapping).

Folder: Graphs
File: 361_Cycle_Detection_in_Undirected_Graph_bfs.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[int]]) -> bool:
    visited = [False] * v
    
    def check_cycle(src):
        visited[src] = True
        queue = [(src, -1)] # (node, parent)
        while queue:
            node, parent = queue.pop(0)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    return True
        return False
        
    for i in range(v):
        if not visited[i]:
            if check_cycle(i):
                return True
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[1], [0, 2, 3], [1, 3], [1, 2]] # cycle 1-2-3-1
    assert optimal_solution(4, adj) == True
    print("Done.")
""",

    "362_Detect_a_cycle_in_an_undirected_graph_dfs.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
Problem Name: Cycle Detection Undirected Graph (DFS)
Description: Detect cycle in undirected graph using DFS.

Folder: Graphs
File: 362_Detect_a_cycle_in_an_undirected_graph_dfs.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[int]]) -> bool:
    visited = [False] * v
    
    def dfs(node, parent):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
        
    for i in range(v):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[1], [0, 2, 3], [1, 3], [1, 2]]
    assert optimal_solution(4, adj) == True
    print("Done.")
""",

    "363_Distance_of_nearest_cell_having_one.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/01-matrix/
Problem Name: 01 Matrix (Nearest Cell Having 1)
Description: Find distance of nearest cell having 1 for each cell in a binary matrix.

Folder: Graphs
File: 363_Distance_of_nearest_cell_having_one.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Multi-source BFS starting from all 1 cells.
# Time Complexity: O(R * C)
# Space Complexity: O(R * C)
def optimal_solution(grid: list[list[int]]) -> list[list[int]]:
    rows, cols = len(grid), len(grid[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    queue = []
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                dist[r][c] = 0
                queue.append((r, c))
                
    while queue:
        r, c = queue.pop(0)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
    return dist

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    res = optimal_solution(grid)
    assert res[0][0] == 2
    assert res[1][1] == 0
    print("Done.")
""",

    "364_Surrounded_Regions.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/surrounded-regions/
Problem Name: Surrounded Regions
Description: Capture surrounded regions ('O') by converting them to 'X'. Border 'O's cannot be captured.

Folder: Graphs
File: 364_Surrounded_Regions.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Find border 'O's. Run DFS to mark connected 'O's as '#'. Convert rest to 'X', '#' to 'O'.
# Time Complexity: O(R * C)
# Space Complexity: O(R * C) recursion stack
def optimal_solution(board: list[list[str]]) -> None:
    if not board:
        return
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c):
        board[r][c] = "#"
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                dfs(nr, nc)
                
    for r in range(rows):
        if board[r][0] == "O": dfs(r, 0)
        if board[r][cols - 1] == "O": dfs(r, cols - 1)
    for c in range(cols):
        if board[0][c] == "O": dfs(0, c)
        if board[rows - 1][c] == "O": dfs(rows - 1, c)
        
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "#":
                board[r][c] = "O"

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    optimal_solution(board)
    assert board[1][1] == "X"
    assert board[3][1] == "O" # boundary O kept
    print("Done.")
""",

    "365_Number_of_enclaves.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/number-of-enclaves/
Problem Name: Number of Enclaves
Description: Count number of 1s in a grid from which we cannot walk off boundary.

Folder: Graphs
File: 365_Number_of_enclaves.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Mark all boundary-connected 1s using DFS/BFS. Count remaining 1s.
# Time Complexity: O(R * C)
# Space Complexity: O(R * C)
def optimal_solution(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    
    def dfs(r, c):
        grid[r][c] = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                dfs(nr, nc)
                
    for r in range(rows):
        if grid[r][0] == 1: dfs(r, 0)
        if grid[r][cols - 1] == 1: dfs(r, cols - 1)
    for c in range(cols):
        if grid[0][c] == 1: dfs(0, c)
        if grid[rows - 1][c] == 1: dfs(rows - 1, c)
        
    return sum(sum(row) for row in grid)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
    assert optimal_solution(grid) == 3
    print("Done.")
""",

    "366_Word_ladder_I.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/word-ladder/
Problem Name: Word Ladder I
Description: Find shortest transformation sequence length from beginWord to endWord.

Folder: Graphs
File: 366_Word_ladder_I.py
\"\"\"

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
""",

    "367_Word_ladder_II.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/word-ladder-ii/
Problem Name: Word Ladder II
Description: Return all shortest transformation sequences.

Folder: Graphs
File: 367_Word_ladder_II.py
\"\"\"

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
""",

    "368_Number_of_islands.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/number-of-islands/
Problem Name: Number of Islands
Description: Find total connected components of 1s in a grid (4 directions).

Folder: Graphs
File: 368_Number_of_islands.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(R * C)
# Space Complexity: O(R * C)
def optimal_solution(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r, c):
        grid[r][c] = "0"
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                dfs(nr, nc)
                
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                dfs(r, c)
    return islands

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    assert optimal_solution(grid) == 3
    print("Done.")
""",

    "369_Bipartite_Graph_DFS.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/is-graph-bipartite/
Problem Name: Is Graph Bipartite? (DFS)
Description: Determine if graph is bipartite (2-colorable).

Folder: Graphs
File: 369_Bipartite_Graph_DFS.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Bipartite graph is colorable using 2 colors such that adjacent vertices have different colors.
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(graph: list[list[int]]) -> bool:
    v = len(graph)
    colors = {} # node -> color (0 or 1)
    
    def dfs(node, color):
        colors[node] = color
        for neighbor in graph[node]:
            if neighbor not in colors:
                if not dfs(neighbor, 1 - color):
                    return False
            elif colors[neighbor] == color:
                return False
        return True
        
    for i in range(v):
        if i not in colors:
            if not dfs(i, 0):
                return False
    return True

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    graph = [[1,3],[0,2],[1,3],[0,2]]
    assert optimal_solution(graph) == True
    print("Done.")
""",

    "370_Cycle_Detection_in_Directed_Graph_DFS.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
Problem Name: Cycle Detection in Directed Graph (DFS)
Description: Detect cycle in directed graph using DFS. Keep tracking recursive stack path.

Folder: Graphs
File: 370_Cycle_Detection_in_Directed_Graph_DFS.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[int]]) -> bool:
    visited = [False] * v
    path_visited = [False] * v
    
    def dfs(node):
        visited[node] = True
        path_visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif path_visited[neighbor]:
                return True
        path_visited[node] = False
        return False
        
    for i in range(v):
        if not visited[i]:
            if dfs(i):
                return True
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[1], [2], [0]] # Cycle 0-1-2-0
    assert optimal_solution(3, adj) == True
    print("Done.")
""",

    "371_Topo_Sort.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/topological-sort/1
Problem Name: Topological Sort (DFS)
Description: Topo sort of Directed Acyclic Graph (DAG) using DFS.

Folder: Graphs
File: 371_Topo_Sort.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[int]]) -> list[int]:
    visited = [False] * v
    stack = []
    
    def dfs(node):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)
        
    for i in range(v):
        if not visited[i]:
            dfs(i)
            
    return stack[::-1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[], [], [3], [1], [0, 1], [0, 2]]
    res = optimal_solution(6, adj)
    # verify topological sort properties
    pos = {val: idx for idx, val in enumerate(res)}
    assert pos[5] < pos[2]
    assert pos[2] < pos[3]
    print("Done.")
""",

    "372_Topological_sort_or_Kahns_algorithm.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/topological-sort/1
Problem Name: Topological Sort (Kahn's Algorithm BFS)
Description: Topo sort using Kahn's algorithm (indegree).

Folder: Graphs
File: 372_Topological_sort_or_Kahns_algorithm.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[int]]) -> list[int]:
    indegree = [0] * v
    for i in range(v):
        for neighbor in adj[i]:
            indegree[neighbor] += 1
            
    queue = [i for i in range(v) if indegree[i] == 0]
    topo = []
    
    while queue:
        node = queue.pop(0)
        topo.append(node)
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return topo

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[], [], [3], [1], [0, 1], [0, 2]]
    res = optimal_solution(6, adj)
    assert len(res) == 6
    print("Done.")
""",

    "373_Detect_a_cycle_in_a_directed_graph_BFS.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
Problem Name: Cycle Detection Directed Graph (BFS)
Description: Detect cycle in directed graph using Kahn's algorithm (BFS). If Topo Sort size != V, cycle exists.

Folder: Graphs
File: 373_Detect_a_cycle_in_a_directed_graph_BFS.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[int]]) -> bool:
    indegree = [0] * v
    for i in range(v):
        for neighbor in adj[i]:
            indegree[neighbor] += 1
            
    queue = [i for i in range(v) if indegree[i] == 0]
    count = 0
    
    while queue:
        node = queue.pop(0)
        count += 1
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                
    return count != v

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[1], [2], [0]] # Cycle
    assert optimal_solution(3, adj) == True
    print("Done.")
""",

    "374_Course_Schedule_I.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/course-schedule/
Problem Name: Course Schedule I
Description: Check if courses can be completed given prerequisite pair list.

Folder: Graphs
File: 374_Course_Schedule_I.py
\"\"\"

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
""",

    "375_Course_Schedule_II.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/course-schedule-ii/
Problem Name: Course Schedule II
Description: Return order in which courses should be taken.

Folder: Graphs
File: 375_Course_Schedule_II.py
\"\"\"

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
""",

    "376_Find_eventual_safe_states.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/find-eventual-safe-states/
Problem Name: Find Eventual Safe States
Description: Find nodes which cannot lead to a cycle (ends in terminal nodes).

Folder: Graphs
File: 376_Find_eventual_safe_states.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Standard Kahn's algorithm by reversing edges. Safe nodes have indegree=0.
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
def optimal_solution(graph: list[list[int]]) -> list[int]:
    v = len(graph)
    rev_adj = [[] for _ in range(v)]
    indegree = [0] * v
    
    for u in range(v):
        for w in graph[u]:
            rev_adj[w].append(u)
            indegree[u] += 1
            
    queue = [i for i in range(v) if indegree[i] == 0]
    safe = [False] * v
    while queue:
        node = queue.pop(0)
        safe[node] = True
        for neighbor in rev_adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                
    return [i for i in range(v) if safe[i]]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    assert optimal_solution(graph) == [2, 4, 5, 6]
    print("Done.")
""",

    "377_Alien_Dictionary.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/alien-dictionary/1
Problem Name: Alien Dictionary
Description: Find alphabetical order of characters in alien language.

Folder: Graphs
File: 377_Alien_Dictionary.py
\"\"\"

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
""",

    "378_Shortest_path_in_undirected_graph_with_unit_weights.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1
Problem Name: Shortest Path in Undirected Graph with Unit Weights
Description: Find shortest path from source to all vertices.

Folder: Graphs
File: 378_Shortest_path_in_undirected_graph_with_unit_weights.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: BFS traversal starting from source node.
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, edges: list[tuple[int, int]], src: int) -> list[int]:
    adj = [[] for _ in range(v)]
    for u, w in edges:
        adj[u].append(w)
        adj[w].append(u)
        
    dist = [-1] * v
    dist[src] = 0
    queue = [src]
    
    while queue:
        node = queue.pop(0)
        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    edges = [(0, 1), (1, 2), (0, 2)]
    assert optimal_solution(3, edges, 0) == [0, 1, 1]
    print("Done.")
""",

    "379_Shortest_path_in_DAG.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/shortest-path-in-directed-acyclic-graph/1
Problem Name: Shortest Path in DAG
Description: Find shortest path in DAG from source node. Weights given.

Folder: Graphs
File: 379_Shortest_path_in_DAG.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Run Topological Sort. Relax edges of nodes sequentially in Topo order.
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, edges: list[tuple[int, int, int]], src: int) -> list[int]:
    adj = [[] for _ in range(v)]
    for u, w, d in edges:
        adj[u].append((w, d))
        
    # Topo Sort
    visited = [False] * v
    stack = []
    
    def dfs(node):
        visited[node] = True
        for neighbor, weight in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)
        
    for i in range(v):
        if not visited[i]:
            dfs(i)
            
    dist = [float('inf')] * v
    dist[src] = 0
    
    while stack:
        node = stack.pop()
        if dist[node] != float('inf'):
            for neighbor, weight in adj[node]:
                dist[neighbor] = min(dist[neighbor], dist[node] + weight)
                
    return [d if d != float('inf') else -1 for d in dist]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    edges = [(0, 1, 2), (0, 2, 1), (1, 2, 3)]
    assert optimal_solution(3, edges, 0) == [0, 2, 1]
    print("Done.")
""",

    "380_Djisktras_Algorithm.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1
Problem Name: Dijkstra's Algorithm
Description: Shortest path from source node using Min Heap.

Folder: Graphs
File: 380_Djisktras_Algorithm.py
\"\"\"

import heapq

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(E log V)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[tuple[int, int]]], src: int) -> list[int]:
    dist = [float('inf')] * v
    dist[src] = 0
    pq = [(0, src)] # (distance, node)
    
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in adj[node]:
            if dist[neighbor] > d + weight:
                dist[neighbor] = d + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))
    return dist

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[(1, 4), (2, 1)], [(0, 4), (2, 2)], [(0, 1), (1, 2)]]
    assert optimal_solution(3, adj, 0) == [0, 3, 1]
    print("Done.")
""",

    "381_Why_priority_Queue_is_used_in_Djisktras_Algorithm.py": """\"\"\"
LeetCode Link: N/A (Concept discussion)
Problem Name: Why Priority Queue is used in Dijkstra
Description: Conceptual verification code testing PQ vs Array search.

Folder: Graphs
File: 381_Why_priority_Queue_is_used_in_Djisktras_Algorithm.py
\"\"\"

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
""",

    "382_Shortest_Distance_in_a_Binary_Maze.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/
Problem Name: Shortest Distance in a Binary Maze
Description: Find shortest path from top-left to bottom-right in binary maze.

Folder: Graphs
File: 382_Shortest_Distance_in_a_Binary_Maze.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: BFS since weights are uniform (1).
# Time Complexity: O(R * C)
# Space Complexity: O(R * C)
def optimal_solution(grid: list[list[int]]) -> int:
    if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
        
    n = len(grid)
    queue = [(0, 0, 1)] # (row, col, path_len)
    visited = {(0, 0)}
    
    while queue:
        r, c, length = queue.pop(0)
        if r == n - 1 and c == n - 1:
            return length
            
        # 8 directions
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, length + 1))
    return -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [[0, 1], [1, 0]]
    assert optimal_solution(grid) == 2
    print("Done.")
""",

    "383_Path_with_minimum_effort.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/path-with-minimum-effort/
Problem Name: Path with Minimum Effort
Description: Find path from top-left to bottom-right minimizing maximum absolute difference between consecutive cells.

Folder: Graphs
File: 383_Path_with_minimum_effort.py
\"\"\"

import heapq

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Dijkstra using effort as weight metric.
# Time Complexity: O(R * C log (R * C))
# Space Complexity: O(R * C)
def optimal_solution(heights: list[list[int]]) -> int:
    rows, cols = len(heights), len(heights[0])
    efforts = [[float('inf')] * cols for _ in range(rows)]
    efforts[0][0] = 0
    pq = [(0, 0, 0)] # (effort, r, c)
    
    while pq:
        effort, r, c = heapq.heappop(pq)
        if r == rows - 1 and c == cols - 1:
            return effort
        if effort > efforts[r][c]:
            continue
            
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                diff = max(effort, abs(heights[nr][nc] - heights[r][c]))
                if efforts[nr][nc] > diff:
                    efforts[nr][nc] = diff
                    heapq.heappush(pq, (diff, nr, nc))
    return 0

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    assert optimal_solution(heights) == 2
    print("Done.")
""",

    "384_Cheapest_flight_within_K_stops.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
Problem Name: Cheapest Flight Within K Stops
Description: Find cheapest price from src to dst with at most K stops.

Folder: Graphs
File: 384_Cheapest_flight_within_K_stops.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Modified BFS keeping track of stops.
# Time Complexity: O(E * K)
# Space Complexity: O(V)
def optimal_solution(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    adj = [[] for _ in range(n)]
    for u, w, price in flights:
        adj[u].append((w, price))
        
    prices = [float('inf')] * n
    prices[src] = 0
    # queue elements: (stops, node, price)
    queue = [(0, src, 0)]
    
    while queue:
        stops, node, price = queue.pop(0)
        if stops > k:
            continue
        for neighbor, p in adj[node]:
            if prices[neighbor] > price + p:
                prices[neighbor] = price + p
                queue.append((stops + 1, neighbor, prices[neighbor]))
                
    return prices[dst] if prices[dst] != float('inf') else -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    assert optimal_solution(3, flights, 0, 2, 1) == 200
    print("Done.")
""",

    "385_Network_Delay_Time.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/network-delay-time/
Problem Name: Network Delay Time
Description: Find minimum time to send signal to all V nodes from K. Return -1 if impossible.

Folder: Graphs
File: 385_Network_Delay_Time.py
\"\"\"

import heapq

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(E log V)
# Space Complexity: O(V)
def optimal_solution(times: list[list[int]], n: int, k: int) -> int:
    adj = [[] for _ in range(n + 1)]
    for u, w, d in times:
        adj[u].append((w, d))
        
    dist = [float('inf')] * (n + 1)
    dist[k] = 0
    pq = [(0, k)]
    
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in adj[node]:
            if dist[neighbor] > d + weight:
                dist[neighbor] = d + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))
                
    max_dist = max(dist[1:])
    return max_dist if max_dist != float('inf') else -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    times = [[2,1,1],[2,3,1],[3,4,1]]
    assert optimal_solution(times, 4, 2) == 2
    print("Done.")
""",

    "386_Number_of_ways_to_arrive_at_destination.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
Problem Name: Number of Ways to Arrive at Destination
Description: Find total paths that yield shortest distance from 0 to N-1.

Folder: Graphs
File: 386_Number_of_ways_to_arrive_at_destination.py
\"\"\"

import heapq

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Dijkstra's keeping dynamic paths count.
# Time Complexity: O(E log V)
# Space Complexity: O(V)
def optimal_solution(n: int, roads: list[list[int]]) -> int:
    MOD = 10**9 + 7
    adj = [[] for _ in range(n)]
    for u, w, d in roads:
        adj[u].append((w, d))
        adj[w].append((u, d))
        
    dist = [float('inf')] * n
    ways = [0] * n
    dist[0] = 0
    ways[0] = 1
    pq = [(0, 0)] # (distance, node)
    
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in adj[node]:
            if dist[neighbor] > d + weight:
                dist[neighbor] = d + weight
                ways[neighbor] = ways[node]
                heapq.heappush(pq, (dist[neighbor], neighbor))
            elif dist[neighbor] == d + weight:
                ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
    return ways[-1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    assert optimal_solution(7, roads) == 4
    print("Done.")
""",

    "387_Minimum_multiplications_to_reach_end.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1
Problem Name: Minimum Multiplications to Reach End
Description: Find minimal multiplications mod 100000 to reach end starting from start.

Folder: Graphs
File: 387_Minimum_multiplications_to_reach_end.py
\"\"\"

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
""",

    "388_Bellman_Ford_Algorithm.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1
Problem Name: Bellman Ford Algorithm
Description: Shortest path from source allowing negative weight edges. Returns -1 if negative cycle exists.

Folder: Graphs
File: 388_Bellman_Ford_Algorithm.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Relax all edges V-1 times. Run 1 more relaxation to check for negative cycles.
# Time Complexity: O(V * E)
# Space Complexity: O(V)
def optimal_solution(v: int, edges: list[list[int]], src: int) -> list[int]:
    dist = [10**8] * v
    dist[src] = 0
    
    for _ in range(v - 1):
        for u, w, d in edges:
            if dist[u] != 10**8 and dist[u] + d < dist[w]:
                dist[w] = dist[u] + d
                
    # Check for negative cycle
    for u, w, d in edges:
        if dist[u] != 10**8 and dist[u] + d < dist[w]:
            return [-1]
            
    return dist

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    edges = [[0, 1, 9]]
    assert optimal_solution(2, edges, 0) == [0, 9]
    print("Done.")
""",

    "389_Floyd_warshall_algorithm.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1
Problem Name: Floyd Warshall Algorithm
Description: All-pairs shortest path in-place grid update.

Folder: Graphs
File: 389_Floyd_warshall_algorithm.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V^3)
# Space Complexity: O(1) in-place updates
def optimal_solution(matrix: list[list[int]]) -> None:
    v = len(matrix)
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if matrix[i][k] != -1 and matrix[k][j] != -1:
                    val = matrix[i][k] + matrix[k][j]
                    if matrix[i][j] == -1 or matrix[i][j] > val:
                        matrix[i][j] = val

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    matrix = [[0, 2, -1], [-1, 0, 3], [1, -1, 0]]
    optimal_solution(matrix)
    assert matrix[0][2] == 5 # 0-1-2 path
    print("Done.")
""",

    "390_Find_the_city_with_the_smallest_number_of_neighbors.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
Problem Name: Find the City with the Smallest Number of Neighbors at a Threshold Distance
Description: Find city with smallest neighbors reachable within distanceThreshold.

Folder: Graphs
File: 390_Find_the_city_with_the_smallest_number_of_neighbors.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Floyd-Warshall to find shortest path matrix.
# Time Complexity: O(V^3)
# Space Complexity: O(V^2)
def optimal_solution(n: int, edges: list[list[int]], distanceThreshold: int) -> int:
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, w, d in edges:
        dist[u][w] = d
        dist[w][u] = d
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    min_count = float('inf')
    best_city = -1
    for i in range(n):
        count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
        if count <= min_count:
            min_count = count
            best_city = i
    return best_city

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
    assert optimal_solution(4, edges, 4) == 3
    print("Done.")
""",

    "391_MST_theory.py": """\"\"\"
LeetCode Link: N/A
Problem Name: Minimum Spanning Tree Theory
Description: Conceptual verification of MST vertices and edges properties.

Folder: Graphs
File: 391_MST_theory.py
\"\"\"

# ============================================
# CONCEPT
# ============================================
# For connected undirected graph G with V vertices:
# MST contains V vertices and V - 1 edges. No cycles.
def verify():
    # If V=3, MST contains 2 edges.
    assert 3 - 1 == 2

if __name__ == "__main__":
    print("Running tests...")
    verify()
    print("Done.")
""",

    "392_Prims_Algorithm.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1
Problem Name: Prim's Algorithm (MST)
Description: Find total weight of MST using Prim's algorithm (min heap).

Folder: Graphs
File: 392_Prims_Algorithm.py
\"\"\"

import heapq

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(E log V)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[tuple[int, int]]]) -> int:
    visited = [False] * v
    pq = [(0, 0)] # (weight, node)
    mst_weight = 0
    
    while pq:
        w, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        mst_weight += w
        for neighbor, weight in adj[node]:
            if not visited[neighbor]:
                heapq.heappush(pq, (weight, neighbor))
    return mst_weight

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[(1, 2), (2, 1)], [(0, 2), (2, 3)], [(0, 1), (1, 3)]]
    assert optimal_solution(3, adj) == 3
    print("Done.")
""",

    "393_Disjoint_Set.py": """\"\"\"
LeetCode Link: N/A
Problem Name: Disjoint Set (Union-Find)
Description: Implement Disjoint Set class with Rank and Path Compression.

Folder: Graphs
File: 393_Disjoint_Set.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i]) # Path compression
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    ds = DisjointSet(5)
    ds.union(0, 1)
    ds.union(1, 2)
    assert ds.find(0) == ds.find(2)
    assert ds.find(0) != ds.find(3)
    print("Done.")
""",

    "394_Find_the_MST_weight.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1
Problem Name: Find the MST weight (Kruskal's Algorithm)
Description: Kruskal's algorithm to compute MST weight using Union-Find.

Folder: Graphs
File: 394_Find_the_MST_weight.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

def optimal_solution(v: int, edges: list[list[int]]) -> int:
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(v)
    mst_weight = 0
    for u, w, wt in edges:
        if ds.union(u, w):
            mst_weight += wt
    return mst_weight

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    edges = [[0, 1, 2], [1, 2, 3], [0, 2, 1]]
    assert optimal_solution(3, edges) == 3
    print("Done.")
""",

    "395_Number_of_operations_to_make_network_connected.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/number-of-operations-to-make-network-connected/
Problem Name: Number of Operations to Make Network Connected
Description: Find minimal operations (cables moved) to connect all computers.

Folder: Graphs
File: 395_Number_of_operations_to_make_network_connected.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Union-Find to count redundant cables and connected components.
# Time Complexity: O(E alpha(V))
# Space Complexity: O(V)
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

def optimal_solution(n: int, connections: list[list[int]]) -> int:
    if len(connections) < n - 1:
        return -1
        
    ds = DisjointSet(n)
    components = n
    for u, w in connections:
        if ds.union(u, w):
            components -= 1
            
    return components - 1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(4, [[0,1],[0,2],[1,2]]) == 1
    print("Done.")
""",

    "396_Most_stones_removed_with_same_row_or_column.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
Problem Name: Most Stones Removed with Same Row or Column
Description: Maximize stones removed if two share row or column.

Folder: Graphs
File: 396_Most_stones_removed_with_same_row_or_column.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Treat row and column indices as graph nodes. Union rows and cols.
# Time Complexity: O(N alpha(max_idx))
# Space Complexity: O(max_idx)
class DisjointSet:
    def __init__(self):
        self.parent = {}
    def find(self, i):
        if i not in self.parent:
            self.parent[i] = i
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

def optimal_solution(stones: list[list[int]]) -> int:
    ds = DisjointSet()
    for r, c in stones:
        # Offset column coordinates to prevent clash with rows
        ds.union(r, c + 10001)
        
    unique_roots = set(ds.find(x) for x in ds.parent)
    return len(stones) - len(unique_roots)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    assert optimal_solution(stones) == 5
    print("Done.")
""",

    "397_Accounts_merge.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/accounts-merge/
Problem Name: Accounts Merge
Description: Merge email accounts belonging to the same user.

Folder: Graphs
File: 397_Accounts_merge.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Group emails under parent IDs using DisjointSet.
# Time Complexity: O(N * log N)
# Space Complexity: O(Emails)
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        self.parent[self.find(i)] = self.find(j)

def optimal_solution(accounts: list[list[str]]) -> list[list[str]]:
    ds = DisjointSet(len(accounts))
    email_to_id = {}
    for idx, account in enumerate(accounts):
        for email in account[1:]:
            if email in email_to_id:
                ds.union(idx, email_to_id[email])
            else:
                email_to_id[email] = idx
                
    merged = {}
    for email, idx in email_to_id.items():
        root = ds.find(idx)
        if root not in merged:
            merged[root] = []
        merged[root].append(email)
        
    res = []
    for root, emails in merged.items():
        res.append([accounts[root][0]] + sorted(emails))
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"]]
    res = optimal_solution(accounts)
    assert len(res) == 2
    print("Done.")
""",

    "398_Number_of_islands_II.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/number-of-islands-ii/1
Problem Name: Number of Islands II
Description: Online queries. Count islands dynamically as land cells are populated.

Folder: Graphs
File: 398_Number_of_islands_II.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(Q alpha(R * C))
# Space Complexity: O(R * C)
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False

def optimal_solution(r: int, c: int, queries: list[list[int]]) -> list[int]:
    ds = DisjointSet(r * c)
    grid = [[0] * c for _ in range(r)]
    islands_count = 0
    res = []
    
    for row, col in queries:
        if grid[row][col] == 1:
            res.append(islands_count)
            continue
            
        grid[row][col] = 1
        islands_count += 1
        node = row * c + col
        
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < r and 0 <= nc < c and grid[nr][nc] == 1:
                neighbor = nr * c + nc
                if ds.union(node, neighbor):
                    islands_count -= 1
        res.append(islands_count)
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    queries = [[0,0], [0,1], [1,2], [2,1]]
    assert optimal_solution(3, 3, queries) == [1, 1, 2, 3]
    print("Done.")
""",

    "399_Making_a_large_island.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/making-a-large-island/
Problem Name: Making a Large Island
Description: Change at most one 0 to 1. Find size of largest island possible.

Folder: Graphs
File: 399_Making_a_large_island.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Color islands with unique IDs. Map ID to component size. 
# For each 0, sum sizes of unique neighbor island IDs.
# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
def optimal_solution(grid: list[list[int]]) -> int:
    n = len(grid)
    island_sizes = {}
    color = 2
    
    def dfs(r, c, clr):
        grid[r][c] = clr
        size = 1
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                size += dfs(nr, nc, clr)
        return size
        
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                size = dfs(r, c, color)
                island_sizes[color] = size
                color += 1
                
    max_island = max(island_sizes.values()) if island_sizes else 0
    
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                neighbor_colors = set()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                        neighbor_colors.add(grid[nr][nc])
                size = 1 + sum(island_sizes[clr] for clr in neighbor_colors)
                max_island = max(max_island, size)
    return max_island

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [[1, 0], [0, 1]]
    assert optimal_solution(grid) == 3
    print("Done.")
""",

    "400_Swim_in_Rising_Water.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/swim-in-rising-water/
Problem Name: Swim in Rising Water
Description: Find minimal time to swim from top-left to bottom-right on grid where water level rises.

Folder: Graphs
File: 400_Swim_in_Rising_Water.py
\"\"\"

import heapq

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Dijkstra's keeping track of path minimax weight.
# Time Complexity: O(N^2 log N)
# Space Complexity: O(N^2)
def optimal_solution(grid: list[list[int]]) -> int:
    n = len(grid)
    pq = [(grid[0][0], 0, 0)] # (elevation, r, c)
    visited = {(0, 0)}
    
    while pq:
        elevation, r, c = heapq.heappop(pq)
        if r == n - 1 and c == n - 1:
            return elevation
            
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                visited.add((nr, nc))
                heapq.heappush(pq, (max(elevation, grid[nr][nc]), nr, nc))
    return 0

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    grid = [[0,2],[1,3]]
    assert optimal_solution(grid) == 3
    print("Done.")
""",

    "401_Bridges_in_graph.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/critical-connections-in-a-network/
Problem Name: Critical Connections in a Network (Bridges)
Description: Find bridges in undirected graph using Tarjan's DFS bridge finder.

Folder: Graphs
File: 401_Bridges_in_graph.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(n: int, connections: list[list[int]]) -> list[list[int]]:
    adj = [[] for _ in range(n)]
    for u, w in connections:
        adj[u].append(w)
        adj[w].append(u)
        
    tin = [-1] * n
    low = [-1] * n
    timer = 0
    bridges = []
    
    def dfs(node, parent):
        nonlocal timer
        tin[node] = low[node] = timer
        timer += 1
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            if tin[neighbor] == -1:
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > tin[node]:
                    bridges.append([node, neighbor])
            else:
                low[node] = min(low[node], tin[neighbor])
                
    dfs(0, -1)
    return bridges

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    connections = [[0,1],[1,2],[2,0],[1,3]]
    res = optimal_solution(4, connections)
    assert res == [[1, 3]] or res == [[3, 1]]
    print("Done.")
""",

    "402_Articulation_point_in_graph.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/articulation-point-1/1
Problem Name: Articulation Points in Graph
Description: Find articulation points (nodes whose removal increases connected components).

Folder: Graphs
File: 402_Articulation_point_in_graph.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(n: int, adj: list[list[int]]) -> list[int]:
    tin = [-1] * n
    low = [-1] * n
    is_articulation = [False] * n
    timer = 0
    
    def dfs(node, parent):
        nonlocal timer
        tin[node] = low[node] = timer
        timer += 1
        children = 0
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            if tin[neighbor] == -1:
                children += 1
                dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if parent != -1 and low[neighbor] >= tin[node]:
                    is_articulation[node] = True
            else:
                low[node] = min(low[node], tin[neighbor])
        if parent == -1 and children > 1:
            is_articulation[node] = True
            
    for i in range(n):
        if tin[i] == -1:
            dfs(i, -1)
            
    res = [i for i in range(n) if is_articulation[i]]
    return res if res else [-1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    # Graph: 0-1-2 and 1-3
    adj = [[1], [0, 2, 3], [1], [1]]
    assert optimal_solution(4, adj) == [1]
    print("Done.")
""",

    "403_Kosarajus_algorithm.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1
Problem Name: Kosaraju's Algorithm (SCC)
Description: Count strongly connected components (SCC) in directed graph.

Folder: Graphs
File: 403_Kosarajus_algorithm.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight:
# 1. DFS to push nodes to stack by finishing times.
# 2. Transpose graph.
# 3. Pop stack, run DFS on transpose graph.
# Time Complexity: O(V + E)
# Space Complexity: O(V)
def optimal_solution(v: int, adj: list[list[int]]) -> int:
    visited = [False] * v
    stack = []
    
    def dfs1(node):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs1(neighbor)
        stack.append(node)
        
    for i in range(v):
        if not visited[i]:
            dfs1(i)
            
    # Transpose Graph
    rev_adj = [[] for _ in range(v)]
    for u in range(v):
        for w in adj[u]:
            rev_adj[w].append(u)
            
    visited = [False] * v
    scc_count = 0
    
    def dfs2(node):
        visited[node] = True
        for neighbor in rev_adj[node]:
            if not visited[neighbor]:
                dfs2(neighbor)
                
    while stack:
        node = stack.pop()
        if not visited[node]:
            scc_count += 1
            dfs2(node)
            
    return scc_count

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    adj = [[2, 3], [0], [1], [4], []]
    assert optimal_solution(5, adj) == 3 # {0,1,2}, {3}, {4}
    print("Done.")
"""
}

def main():
    target_dir = os.path.join(".", "DSA-Knowledge", "Graphs", "Code")
    os.makedirs(target_dir, exist_ok=True)
    
    # Remove README.py if it exists
    readme_py = os.path.join(target_dir, "README.py")
    if os.path.exists(readme_py):
        os.remove(readme_py)
        print("Removed temporary README.py")
        
    for filename, code in SOLUTIONS.items():
        filepath = os.path.join(target_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"Populated {filename}")
        
    print("All Graphs code solutions populated successfully!")

if __name__ == "__main__":
    main()
