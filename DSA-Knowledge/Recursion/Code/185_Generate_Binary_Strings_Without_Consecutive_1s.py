"""
LeetCode Link: https://www.geeksforgeeks.org/problems/generate-all-binary-strings/1
Problem Name: Generate Binary Strings Without Consecutive 1s
Description: Generate all binary strings of length K without consecutive 1s.

Folder: Recursion
File: 185_Generate_Binary_Strings_Without_Consecutive_1s.py
"""

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
