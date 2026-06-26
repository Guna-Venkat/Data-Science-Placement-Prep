import os

SOLUTIONS = {
    "180_Recursive_Implementation_of_atoi.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/string-to-integer-atoi/
Problem Name: Recursive Implementation of atoi
Description: Convert a string to an integer recursively.

Folder: Recursion
File: 180_Recursive_Implementation_of_atoi.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(N) recursion stack
def optimal_solution(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
        
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
        
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    def convert(idx, current_val):
        if idx >= len(s) or not s[idx].isdigit():
            return current_val
        digit = int(s[idx])
        new_val = current_val * 10 + digit
        # Overflow checks
        if sign * new_val > INT_MAX:
            return INT_MAX
        if sign * new_val < INT_MIN:
            return INT_MIN
        return convert(idx + 1, new_val)

    return sign * convert(0, 0)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("42") == 42
    assert optimal_solution("   -42") == -42
    assert optimal_solution("4193 with words") == 4193
    print("Done.")
""",

    "181_Powx_n.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/powx-n/
Problem Name: Pow(x, n)
Description: Compute x raised to the power n.

Folder: Recursion
File: 181_Powx_n.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary Exponentiation. Compute x^(n/2) and multiply.
# Time Complexity: O(log n)
# Space Complexity: O(log n) recursion stack
def optimal_solution(x: float, n: int) -> float:
    def helper(base, exp):
        if exp == 0:
            return 1.0
        half = helper(base, exp // 2)
        if exp % 2 == 0:
            return half * half
        else:
            return half * half * base

    if n < 0:
        return 1.0 / helper(x, -n)
    return helper(x, n)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert abs(optimal_solution(2.0, 10) - 1024.0) < 1e-9
    assert abs(optimal_solution(2.1, 3) - 9.261) < 1e-9
    assert abs(optimal_solution(2.0, -2) - 0.25) < 1e-9
    print("Done.")
""",

    "182_Count_Good_Numbers.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/count-good-numbers/
Problem Name: Count Good Numbers
Description: A digit string is good if digits at even indices are even, and prime at odd indices.
Count good strings of length n modulo 10^9 + 7.

Folder: Recursion
File: 182_Count_Good_Numbers.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Count of even positions = ceil(n/2), count of odd positions = floor(n/2).
# Choice at even = 5 (0, 2, 4, 6, 8). Choice at odd = 4 (2, 3, 5, 7).
# Calculate 5^even * 4^odd modulo 10^9 + 7.
# Time Complexity: O(log n)
# Space Complexity: O(log n) stack depth
def optimal_solution(n: int) -> int:
    MOD = 10**9 + 7
    
    def power(base, exp):
        if exp == 0:
            return 1
        half = power(base, exp // 2)
        ans = (half * half) % MOD
        if exp % 2 != 0:
            ans = (ans * base) % MOD
        return ans

    evens = (n + 1) // 2
    odds = n // 2
    return (power(5, evens) * power(4, odds)) % MOD

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution(1) == 5
    assert optimal_solution(4) == 400
    assert optimal_solution(50) == 564908303
    print("Done.")
""",

    "183_Sort_a_stack_using_recursion.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/sort-a-stack/1
Problem Name: Sort a Stack using Recursion
Description: Sort a stack of numbers using only recursion and no loops.

Folder: Recursion
File: 183_Sort_a_stack_using_recursion.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: 
# 1. Pop top element, recursively sort remaining stack.
# 2. Insert popped element back into sorted stack in correct sorted position.
# Time Complexity: O(N^2)
# Space Complexity: O(N) recursion stack
def insert_sorted(stack: list[int], val: int):
    if not stack or stack[-1] <= val:
        stack.append(val)
        return
    temp = stack.pop()
    insert_sorted(stack, val)
    stack.append(temp)

def optimal_solution(stack: list[int]) -> list[int]:
    if not stack:
        return stack
    temp = stack.pop()
    optimal_solution(stack)
    insert_sorted(stack, temp)
    return stack

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([3, 2, 1]) == [1, 2, 3]
    assert optimal_solution([11, 2, 32, 3, 41]) == [2, 3, 11, 32, 41]
    print("Done.")
""",

    "184_Reverse_a_Stack.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/reverse-a-stack/1
Problem Name: Reverse a Stack
Description: Reverse a stack recursively without loops.

Folder: Recursion
File: 184_Reverse_a_Stack.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Pop top, recursively reverse remaining stack, then insert popped element at bottom.
# Time Complexity: O(N^2)
# Space Complexity: O(N) recursion stack
def insert_at_bottom(stack: list[int], val: int):
    if not stack:
        stack.append(val)
        return
    temp = stack.pop()
    insert_at_bottom(stack, val)
    stack.append(temp)

def optimal_solution(stack: list[int]) -> list[int]:
    if not stack:
        return stack
    temp = stack.pop()
    optimal_solution(stack)
    insert_at_bottom(stack, temp)
    return stack

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([3, 2, 1]) == [1, 2, 3] # reversed stack representation
    print("Done.")
""",

    "185_Generate_Binary_Strings_Without_Consecutive_1s.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/generate-all-binary-strings/1
Problem Name: Generate Binary Strings Without Consecutive 1s
Description: Generate all binary strings of length K without consecutive 1s.

Folder: Recursion
File: 185_Generate_Binary_Strings_Without_Consecutive_1s.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(2^K)
# Space Complexity: O(K) recursion stack
def optimal_solution(k: int) -> list[str]:
    result = []
    
    def generate(curr_str):
        if len(curr_str) == k:
            result.append(curr_str)
            return
            
        # We can always append '0'
        generate(curr_str + "0")
        
        # We can only append '1' if last char is not '1'
        if not curr_str or curr_str[-1] != "1":
            generate(curr_str + "1")

    generate("")
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert sorted(optimal_solution(3)) == sorted(["000", "001", "010", "100", "101"])
    print("Done.")
""",

    "186_Generate_Parentheses.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/generate-parentheses/
Problem Name: Generate Parentheses
Description: Generate all combinations of well-formed parentheses.

Folder: Recursion
File: 186_Generate_Parentheses.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep track of open and close counts. Can add '(' if open < n.
# Can add ')' if close < open.
# Time Complexity: O(4^n / sqrt(n)) Catalan number count
# Space Complexity: O(n) recursion stack
def optimal_solution(n: int) -> list[str]:
    result = []
    
    def backtrack(curr, open_count, close_count):
        if len(curr) == 2 * n:
            result.append(curr)
            return
            
        if open_count < n:
            backtrack(curr + "(", open_count + 1, close_count)
        if close_count < open_count:
            backtrack(curr + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert sorted(optimal_solution(3)) == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
    print("Done.")
""",

    "187_Power_Set.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/subsets/
Problem Name: Subsets (Power Set)
Description: Generate all subsets of a set of unique elements.

Folder: Recursion
File: 187_Power_Set.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Recursive backtracking with pick/non-pick choices.
# Time Complexity: O(2^N * N)
# Space Complexity: O(N) recursion stack
def optimal_solution(nums: list[int]) -> list[list[int]]:
    result = []
    
    def backtrack(idx, path):
        if idx == len(nums):
            result.append(path[:])
            return
            
        # Don't pick
        backtrack(idx + 1, path)
        # Pick
        path.append(nums[idx])
        backtrack(idx + 1, path)
        path.pop()

    backtrack(0, [])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    res = optimal_solution([1, 2])
    assert sorted(res) == sorted([[], [1], [2], [1, 2]])
    print("Done.")
""",

    "188_Learn_All_Patterns_of_Subsequences_Theory.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/subsets/
Problem Name: Subsequences Theory
Description: Explain and demonstrate picking/non-picking recursion patterns.

Folder: Recursion
File: 188_Learn_All_Patterns_of_Subsequences_Theory.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(2^N)
# Space Complexity: O(N) recursion stack
def optimal_solution(arr: list[int]) -> list[list[int]]:
    subsequences = []
    
    def dfs(idx, curr):
        if idx == len(arr):
            subsequences.append(list(curr))
            return
            
        # Pick
        curr.append(arr[idx])
        dfs(idx + 1, curr)
        curr.pop()
        
        # Don't pick
        dfs(idx + 1, curr)

    dfs(0, [])
    return subsequences

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert len(optimal_solution([1, 2, 3])) == 8
    print("Done.")
""",

    "189_Count_all_subsequences_with_sum_K.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1
Problem Name: Count Subsequences with Sum K
Description: Find total subsequences whose sum equals K.

Folder: Recursion
File: 189_Count_all_subsequences_with_sum_K.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Recursion with pick/non-pick. Return count from sub-calls.
# Time Complexity: O(2^N)
# Space Complexity: O(N) recursion stack
def optimal_solution(arr: list[int], k: int) -> int:
    def solve(idx, target):
        if target == 0:
            return 1
        if idx == len(arr) or target < 0:
            return 0
            
        # pick + non-pick
        pick = solve(idx + 1, target - arr[idx])
        non_pick = solve(idx + 1, target)
        return pick + non_pick

    return solve(0, k)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 1], 2) == 2 # [1, 1] and [2]
    print("Done.")
""",

    "190_Check_if_there_exists_a_subsequence_with_sum_K.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555635/1
Problem Name: Subset Sum Problem
Description: Check if there exists a subsequence whose sum equals K.

Folder: Recursion
File: 190_Check_if_there_exists_a_subsequence_with_sum_K.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Base cases check. Short circuit evaluations (OR conditions).
# Time Complexity: O(2^N)
# Space Complexity: O(N) recursion stack
def optimal_solution(arr: list[int], k: int) -> bool:
    def solve(idx, target):
        if target == 0:
            return True
        if idx == len(arr) or target < 0:
            return False
            
        # Pick or Don't pick
        return solve(idx + 1, target - arr[idx]) or solve(idx + 1, target)

    return solve(0, k)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([1, 2, 3], 5) == True
    assert optimal_solution([1, 2, 3], 7) == False
    print("Done.")
""",

    "191_Combination_Sum.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/combination-sum/
Problem Name: Combination Sum
Description: Find all unique combinations of candidates where candidates sum to target.
Repeated selection allowed.

Folder: Recursion
File: 191_Combination_Sum.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Backtracking with reuse. Keep index pointer `idx` same for recursive reuse.
# Time Complexity: O(2^T * K) where T is target / min candidate
# Space Complexity: O(T) stack depth
def optimal_solution(candidates: list[int], target: int) -> list[list[int]]:
    result = []
    
    def backtrack(idx, target, path):
        if target == 0:
            result.append(list(path))
            return
        if idx == len(candidates) or target < 0:
            return
            
        # Pick current element
        path.append(candidates[idx])
        backtrack(idx, target - candidates[idx], path)
        path.pop()
        
        # Skip current element
        backtrack(idx + 1, target, path)

    backtrack(0, target, [])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    res = optimal_solution([2, 3, 6, 7], 7)
    assert sorted(res) == sorted([[2, 2, 3], [7]])
    print("Done.")
""",

    "192_Combination_Sum_II.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/combination-sum-ii/
Problem Name: Combination Sum II
Description: Find all unique combinations in candidates where elements sum to target.
Each candidate used once.

Folder: Recursion
File: 192_Combination_Sum_II.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Sort candidates. In loop, skip adjacent duplicates to prevent duplicate paths.
# Time Complexity: O(2^N * N)
# Space Complexity: O(N)
def optimal_solution(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    result = []
    
    def backtrack(idx, target, path):
        if target == 0:
            result.append(list(path))
            return
        if target < 0:
            return
            
        for i in range(idx, len(candidates)):
            # skip duplicate elements
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
                
            path.append(candidates[i])
            backtrack(i + 1, target - candidates[i], path)
            path.pop()

    backtrack(0, target, [])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    res = optimal_solution([10, 1, 2, 7, 6, 1, 5], 8)
    assert sorted(res) == sorted([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
    print("Done.")
""",

    "193_Subsets_I.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/subset-sums2234/1
Problem Name: Subset Sums (Subsets I)
Description: Generate sum of all possible subsets.

Folder: Recursion
File: 193_Subsets_I.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(2^N)
# Space Complexity: O(N) recursion stack
def optimal_solution(arr: list[int]) -> list[int]:
    result = []
    
    def backtrack(idx, curr_sum):
        if idx == len(arr):
            result.append(curr_sum)
            return
            
        # pick
        backtrack(idx + 1, curr_sum + arr[idx])
        # don't pick
        backtrack(idx + 1, curr_sum)

    backtrack(0, 0)
    result.sort()
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution([2, 3]) == [0, 2, 3, 5]
    print("Done.")
""",

    "194_Subsets_II.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/subsets-ii/
Problem Name: Subsets II
Description: Generate all unique subsets (duplicates allowed in input array).

Folder: Recursion
File: 194_Subsets_II.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Sort. Loop over index space. Skip duplicates `i > idx and nums[i] == nums[i-1]`.
# Time Complexity: O(2^N * N)
# Space Complexity: O(N)
def optimal_solution(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    
    def backtrack(idx, path):
        result.append(list(path))
        
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    res = optimal_solution([1, 2, 2])
    assert sorted(res) == sorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
    print("Done.")
""",

    "195_Combination_Sum_III.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/combination-sum-iii/
Problem Name: Combination Sum III
Description: Find all combinations of k numbers that sum to n using numbers 1 to 9.

Folder: Recursion
File: 195_Combination_Sum_III.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(9! / (k! * (9-k)!)) combinations
# Space Complexity: O(k) stack depth
def optimal_solution(k: int, n: int) -> list[list[int]]:
    result = []
    
    def backtrack(num, target, path):
        if len(path) == k:
            if target == 0:
                result.append(list(path))
            return
        if num > 9 or target < 0:
            return
            
        # pick
        path.append(num)
        backtrack(num + 1, target - num, path)
        path.pop()
        
        # don't pick
        backtrack(num + 1, target, path)

    backtrack(1, n, [])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    res = optimal_solution(3, 7)
    assert res == [[1, 2, 4]]
    print("Done.")
""",

    "196_Letter_Combinations_of_a_Phone_Number.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Problem Name: Letter Combinations of a Phone Number
Description: Return all letter combinations that a phone number digits string represents.

Folder: Recursion
File: 196_Letter_Combinations_of_a_Phone_Number.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(4^N * N) where N is length of digits string
# Space Complexity: O(N)
def optimal_solution(digits: str) -> list[str]:
    if not digits:
        return []
        
    mapping = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    
    result = []
    
    def backtrack(idx, path):
        if idx == len(digits):
            result.append("".join(path))
            return
            
        for char in mapping[digits[idx]]:
            path.append(char)
            backtrack(idx + 1, path)
            path.pop()

    backtrack(0, [])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert sorted(optimal_solution("23")) == sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    print("Done.")
""",

    "197_Palindrome_partitioning.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/palindrome-partitioning/
Problem Name: Palindrome Partitioning
Description: Partition a string such that every substring of the partition is a palindrome.

Folder: Recursion
File: 197_Palindrome_partitioning.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Try cutting string at indices. If prefix is palindrome, recursively partition remaining.
# Time Complexity: O(2^N * N)
# Space Complexity: O(N)
def optimal_solution(s: str) -> list[list[str]]:
    result = []
    
    def is_palindrome(val):
        return val == val[::-1]

    def backtrack(idx, path):
        if idx == len(s):
            result.append(list(path))
            return
            
        for i in range(idx, len(s)):
            part = s[idx:i+1]
            if is_palindrome(part):
                path.append(part)
                backtrack(i + 1, path)
                path.pop()

    backtrack(0, [])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    res = optimal_solution("aab")
    assert sorted(res) == sorted([["a", "a", "b"], ["aa", "b"]])
    print("Done.")
""",

    "198_Word_Search.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/word-search/
Problem Name: Word Search
Description: Return True if a word exists in a 2D board.

Folder: Recursion
File: 198_Word_Search.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: DFS backtracking. Mark cells visited by changing value, then restore (backtrack).
# Time Complexity: O(R * C * 4^L) where L is length of word
# Space Complexity: O(L) recursion stack depth
def optimal_solution(board: list[list[str]], word: str) -> bool:
    if not board:
        return False
        
    rows = len(board)
    cols = len(board[0])
    
    def dfs(r, c, idx):
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
            return False
            
        temp = board[r][c]
        board[r][c] = "#" # mark visited
        
        # Directions
        found = (dfs(r+1, c, idx+1) or
                 dfs(r-1, c, idx+1) or
                 dfs(r, c+1, idx+1) or
                 dfs(r, c-1, idx+1))
                 
        board[r][c] = temp # backtrack
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert optimal_solution(board, "ABCCED") == True
    assert optimal_solution(board, "SEE") == True
    assert optimal_solution(board, "ABCB") == False
    print("Done.")
""",

    "199_N_Queen.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/n-queens/
Problem Name: N-Queens
Description: Place N queens on a chessboard such that no two queens attack each other.

Folder: Recursion
File: 199_N_Queen.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Backtracking column by column. Use hash sets to track occupied rows, 
# main diagonals (r - c), and anti-diagonals (r + c) in O(1) checks.
# Time Complexity: O(N!)
# Space Complexity: O(N)
def optimal_solution(n: int) -> list[list[str]]:
    result = []
    board = [["."] * n for _ in range(n)]
    
    cols = set()
    diag1 = set() # (r - c)
    diag2 = set() # (r + c)
    
    def backtrack(r):
        if r == n:
            result.append(["".join(row) for row in board])
            return
            
        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue
                
            board[r][c] = "Q"
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
            
            backtrack(r + 1)
            
            board[r][c] = "."
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)

    backtrack(0)
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    res = optimal_solution(4)
    assert len(res) == 2
    print("Done.")
""",

    "200_Rat_in_a_Maze.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
Problem Name: Rat in a Maze
Description: Find all sorted paths for a rat to go from (0,0) to (N-1,N-1) in a grid of 0s and 1s.

Folder: Recursion
File: 200_Rat_in_a_Maze.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: DFS backtracking. Move in alphabetical order (D, L, R, U) to get sorted result paths.
# Time Complexity: O(3^(N^2))
# Space Complexity: O(N^2)
def optimal_solution(maze: list[list[int]]) -> list[str]:
    if not maze or maze[0][0] == 0:
        return []
        
    n = len(maze)
    result = []
    
    # Directions: Down, Left, Right, Up
    dirs = [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]
    
    def solve(r, c, path):
        if r == n - 1 and c == n - 1:
            result.append("".join(path))
            return
            
        temp = maze[r][c]
        maze[r][c] = 0 # mark visited
        
        for dr, dc, char in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == 1:
                path.append(char)
                solve(nr, nc, path)
                path.pop()
                
        maze[r][c] = temp # backtrack

    solve(0, 0, [])
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 1, 1]]
    assert optimal_solution(maze) == ["DDRDRR", "DRDDRR"]
    print("Done.")
""",

    "201_Word_Break.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/word-break/
Problem Name: Word Break
Description: Check if a string can be segmented into dictionary words.

Folder: Recursion
File: 201_Word_Break.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Backtracking with Memoization.
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def optimal_solution(s: str, wordDict: list[str]) -> bool:
    words = set(wordDict)
    memo = {}
    
    def solve(idx):
        if idx == len(s):
            return True
        if idx in memo:
            return memo[idx]
            
        for i in range(idx, len(s)):
            if s[idx:i+1] in words:
                if solve(i + 1):
                    memo[idx] = True
                    return True
        memo[idx] = False
        return False

    return solve(0)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert optimal_solution("leetcode", ["leet", "code"]) == True
    assert optimal_solution("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    print("Done.")
""",

    "202_M_Coloring_Problem.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1
Problem Name: M-Coloring Problem
Description: Color a graph using at most M colors such that no adjacent vertices have the same color.

Folder: Recursion
File: 202_M_Coloring_Problem.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Assign colors vertex by vertex. Check adjacency safety. Backtrack if unsafe.
# Time Complexity: O(M^V)
# Space Complexity: O(V)
def optimal_solution(graph: list[list[int]], m: int, v: int) -> bool:
    # graph representation is adjacency matrix
    colors = [0] * v
    
    def is_safe(node, color):
        for i in range(v):
            if graph[node][i] == 1 and colors[i] == color:
                return False
        return True

    def solve(node):
        if node == v:
            return True
            
        for c in range(1, m + 1):
            if is_safe(node, c):
                colors[node] = c
                if solve(node + 1):
                    return True
                colors[node] = 0 # backtrack
        return False

    return solve(0)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    # 4 vertices triangle graph with one disconnected node or similar
    graph = [[0, 1, 1, 1],
             [1, 0, 1, 0],
             [1, 1, 0, 1],
             [1, 0, 1, 0]]
    assert optimal_solution(graph, 3, 4) == True
    print("Done.")
""",

    "203_Sudoku_Solver.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/sudoku-solver/
Problem Name: Sudoku Solver
Description: Solve a Sudoku puzzle in place.

Folder: Recursion
File: 203_Sudoku_Solver.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Try placing digits 1-9 on empty cells. Validate row, col, and 3x3 box constraint.
# Time Complexity: O(9^(N^2)) -> Constant O(1) for a 9x9 board
# Space Complexity: O(1)
def optimal_solution(board: list[list[str]]) -> bool:
    def is_valid(r, c, char):
        for i in range(9):
            if board[r][i] == char:
                return False
            if board[i][c] == char:
                return False
            # 3x3 box
            box_r = 3 * (r // 3) + i // 3
            box_c = 3 * (c // 3) + i % 3
            if board[box_r][box_c] == char:
                return False
        return True

    def solve():
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for char in "123456789":
                        if is_valid(r, c, char):
                            board[r][c] = char
                            if solve():
                                return True
                            board[r][c] = "." # backtrack
                    return False
        return True

    solve()
    return True

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    optimal_solution(board)
    assert board[0][2] == "4"
    print("Done.")
""",

    "204_Expression_Add_Operators.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/expression-add-operators/
Problem Name: Expression Add Operators
Description: Add operators (+, -, *) to digits to make value equal to target.

Folder: Recursion
File: 204_Expression_Add_Operators.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Backtracking. Track index, path expression, current total value, 
# and the value of the last computed term (vital to handle '*' order of operations).
# Time Complexity: O(4^N)
# Space Complexity: O(N)
def optimal_solution(num: str, target: int) -> list[str]:
    result = []
    
    def backtrack(idx, expr, curr_val, last_term):
        if idx == len(num):
            if curr_val == target:
                result.append("".join(expr))
            return
            
        for i in range(idx, len(num)):
            # Skip leading zeros
            if i > idx and num[idx] == "0":
                break
                
            part = num[idx:i+1]
            val = int(part)
            
            if idx == 0:
                backtrack(i + 1, [part], val, val)
            else:
                # Addition
                expr.append("+")
                expr.append(part)
                backtrack(i + 1, expr, curr_val + val, val)
                expr.pop(); expr.pop()
                
                # Subtraction
                expr.append("-")
                expr.append(part)
                backtrack(i + 1, expr, curr_val - val, -val)
                expr.pop(); expr.pop()
                
                # Multiplication
                expr.append("*")
                expr.append(part)
                backtrack(i + 1, expr, curr_val - last_term + (last_term * val), last_term * val)
                expr.pop(); expr.pop()

    backtrack(0, [], 0, 0)
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    assert sorted(optimal_solution("123", 6)) == sorted(["1+2+3", "1*2*3"])
    assert sorted(optimal_solution("232", 8)) == sorted(["2*3+2", "2+3*2"])
    print("Done.")
"""
}

def main():
    target_dir = os.path.join(".", "DSA-Knowledge", "Recursion", "Code")
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
        
    print("All Recursion code solutions populated successfully!")

if __name__ == "__main__":
    main()
