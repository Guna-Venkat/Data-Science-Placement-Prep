"""
LeetCode Link: https://www.geeksforgeeks.org/problems/the-painters-partition-problem1353/1
Problem Name: Painter's Partition
Description: Paint boards of varying lengths among K painters to minimize max time.

Folder: Binary_Search
File: 125_Painters_Partition.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Identical logic to Book Allocation / Split Array Largest Sum.
# Time Complexity: O(N log(sum - max))
# Space Complexity: O(1)
def optimal_solution(boards: list[int], k: int) -> int:
    if k > len(boards):
        return -1
        
    def get_painters_count(max_len):
        painters = 1
        curr_len = 0
        for x in boards:
            if curr_len + x <= max_len:
                curr_len += x
            else:
                painters += 1
                curr_len = x
        return painters

    low, high = max(boards), sum(boards)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if get_painters_count(mid) <= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([10, 20, 30, 40], 2), 60)
    ]
    for idx, ((boards, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(boards, k) == expected, f"Test case {idx} failed"
    print("Done.")
