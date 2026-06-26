"""
LeetCode Link: https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
Problem Name: Inversion Count
Description: Count number of inversion pairs (i < j and arr[i] > arr[j]).

Folder: Arrays
File: 099_Count_Inversions.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Modify Merge Sort to count crossing inversions during merge phase.
# Time Complexity: O(N log N)
# Space Complexity: O(N) for merge arrays
def optimal_solution(arr: list[int]) -> int:
    def merge_and_count(temp, left, mid, right):
        inv_count = 0
        i = left
        j = mid + 1
        k = left
        
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1
            
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
            
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
            
        for loop_var in range(left, right + 1):
            arr[loop_var] = temp[loop_var]
            
        return inv_count

    def merge_sort(temp, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += merge_sort(temp, left, mid)
            inv_count += merge_sort(temp, mid + 1, right)
            inv_count += merge_and_count(temp, left, mid, right)
        return inv_count

    temp = [0] * len(arr)
    return merge_sort(temp, 0, len(arr) - 1)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([2, 4, 1, 3, 5], 3),
        ([1, 20, 6, 4, 5], 5)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr[:]) == expected, f"Test case {idx} failed"
        
    print("Done.")
