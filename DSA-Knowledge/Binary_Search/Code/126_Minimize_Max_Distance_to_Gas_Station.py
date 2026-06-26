"""
LeetCode Link: https://www.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1
Problem Name: Minimize Max Distance to Gas Station
Description: Minimize maximum distance between adjacent gas stations after adding K new stations.

Folder: Binary_Search
File: 126_Minimize_Max_Distance_to_Gas_Station.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary search on the maximum distance using a floating point search.
# Time Complexity: O(N * log(range / 10^-6))
# Space Complexity: O(1)
def optimal_solution(stations: list[int], k: int) -> float:
    def count_needed(dist):
        needed = 0
        for i in range(len(stations) - 1):
            diff = stations[i+1] - stations[i]
            needed += int(diff / dist)
        return needed

    low = 0.0
    high = float(stations[-1] - stations[0])
    eps = 1e-6
    
    while high - low > eps:
        mid = (low + high) / 2.0
        if count_needed(mid) <= k:
            high = mid
        else:
            low = mid
            
    return round(high, 6)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 9
    expected = 0.5
    assert abs(optimal_solution(stations, k) - expected) < 1e-3, "Test failed"
    print("Done.")
