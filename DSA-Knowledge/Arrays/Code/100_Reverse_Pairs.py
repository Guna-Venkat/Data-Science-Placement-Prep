"""
LeetCode Link: https://leetcode.com/problems/reverse-pairs/
Problem Name: Reverse Pairs
Description: Given an integer array nums, return the number of reverse pairs (i < j and nums[i] > 2 * nums[j]).

Folder: Arrays
File: 100_Reverse_Pairs.py
"""

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Modify Merge Sort to count reverse pairs. 
# Time Complexity: O(N log N)
# Space Complexity: O(N)
def optimal_solution(nums: list[int]) -> int:
    def merge_sort(low, high):
        if low >= high:
            return 0
        mid = (low + high) // 2
        count = merge_sort(low, mid) + merge_sort(mid + 1, high)
        count += count_pairs(low, mid, high)
        merge(low, mid, high)
        return count

    def count_pairs(low, mid, high):
        count = 0
        right = mid + 1
        for i in range(low, mid + 1):
            while right <= high and nums[i] > 2 * nums[right]:
                right += 1
            count += (right - (mid + 1))
        return count

    def merge(low, mid, high):
        temp = []
        left = low
        right = mid + 1
        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        while left <= mid:
            temp.append(nums[left])
            left += 1
        while right <= high:
            temp.append(nums[right])
            right += 1
        for i in range(low, high + 1):
            nums[i] = temp[i - low]

    return merge_sort(0, len(nums) - 1)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([1, 3, 2, 3, 1], 2),
        ([2, 4, 3, 5, 1], 3)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr[:]) == expected, f"Test case {idx} failed"
        
    print("Done.")
