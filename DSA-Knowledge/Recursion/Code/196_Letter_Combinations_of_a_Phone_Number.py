"""
LeetCode Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Problem Name: Letter Combinations of a Phone Number
Description: Return all letter combinations that a phone number digits string represents.

Folder: Recursion
File: 196_Letter_Combinations_of_a_Phone_Number.py
"""

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
