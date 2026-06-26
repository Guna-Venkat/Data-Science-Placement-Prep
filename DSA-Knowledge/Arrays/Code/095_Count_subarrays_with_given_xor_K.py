"""
LeetCode Link: https://www.interviewbit.com/problems/subarray-with-given-xor/
Problem Name: Subarrays with Given XOR
Description: Find the number of subarrays having XOR sum equal to B (or K).

Folder: Arrays
File: 095_Count_subarrays_with_given_xor_K.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Similar to Prefix Sum. If XR ^ Y = K, then Y = XR ^ K. Look up prefix XOR frequency.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(A: list[int], B: int) -> int:
    prefix_xor = {0: 1}
    curr_xor = 0
    count = 0
    
    for x in A:
        curr_xor ^= x
        target = curr_xor ^ B
        if target in prefix_xor:
            count += prefix_xor[target]
        prefix_xor[curr_xor] = prefix_xor.get(curr_xor, 0) + 1
        
    return count

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (([4, 2, 2, 6, 4], 6), 4),
        (([5, 6, 7, 8, 9], 5), 2)
    ]
    
    for idx, ((arr, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr, k) == expected, f"Test case {idx} failed"
        
    print("Done.")
