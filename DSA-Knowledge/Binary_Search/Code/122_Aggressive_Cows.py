"""
LeetCode Link: https://www.geeksforgeeks.org/aggressive-cows-problem/
Problem Name: Aggressive Cows
Description: Place C cows in stalls such that the minimum distance between any two of them is maximized.

Folder: Binary_Search
File: 122_Aggressive_Cows.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Sort stalls. Binary search on minimum distance.
# Range is [1, max(stalls) - min(stalls)].
# Time Complexity: O(N log N + N log(range))
# Space Complexity: O(1)
def optimal_solution(stalls: list[int], k: int) -> int:
    stalls.sort()
    
    def can_place(dist):
        count = 1
        last_placed = stalls[0]
        for i in range(1, len(stalls)):
            if stalls[i] - last_placed >= dist:
                count += 1
                last_placed = stalls[i]
                if count >= k:
                    return True
        return False

    low, high = 1, stalls[-1] - stalls[0]
    ans = 1
    while low <= high:
        mid = (low + high) // 2
        if can_place(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([1, 2, 4, 8, 9], 3), 3)
    ]
    for idx, ((stalls, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(stalls, k) == expected, f"Test case {idx} failed"
    print("Done.")
