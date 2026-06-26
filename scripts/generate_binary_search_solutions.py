import os

SOLUTIONS = {
    "102_Search_X_in_sorted_array.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/binary-search/
Problem Name: Binary Search
Description: Find target X in a sorted array. Return index if found, else -1.

Folder: Binary_Search
File: 102_Search_X_in_sorted_array.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([-1, 0, 3, 5, 9, 12], 9), 4),
        (([-1, 0, 3, 5, 9, 12], 2), -1)
    ]
    for idx, ((nums, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, target) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "103_Lower_Bound.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/implement-lower-bound/1
Problem Name: Lower Bound
Description: Find the index of the first element in sorted array which is >= X.

Folder: Binary_Search
File: 103_Lower_Bound.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int], x: int) -> int:
    low, high = 0, len(arr) - 1
    ans = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
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
        (([1, 2, 8, 10, 11, 12, 19], 0), 0),
        (([1, 2, 8, 10, 11, 12, 19], 5), 2),
        (([1, 2, 8, 10, 11, 12, 19], 20), 7)
    ]
    for idx, ((arr, x), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr, x) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "104_Upper_Bound.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/implement-upper-bound/1
Problem Name: Upper Bound
Description: Find the index of the first element in sorted array which is > X.

Folder: Binary_Search
File: 104_Upper_Bound.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int], x: int) -> int:
    low, high = 0, len(arr) - 1
    ans = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
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
        (([1, 2, 8, 10, 11, 12, 19], 0), 0),
        (([1, 2, 8, 10, 11, 12, 19], 8), 3),
        (([1, 2, 8, 10, 11, 12, 19], 20), 7)
    ]
    for idx, ((arr, x), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr, x) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "105_Search_insert_position.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/search-insert-position/
Problem Name: Search Insert Position
Description: Find index where target should be inserted in a sorted array to maintain order.

Folder: Binary_Search
File: 105_Search_insert_position.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Insertion index is exactly the Lower Bound of target.
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    ans = len(nums)
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
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
        (([1, 3, 5, 6], 5), 2),
        (([1, 3, 5, 6], 2), 1),
        (([1, 3, 5, 6], 7), 4)
    ]
    for idx, ((nums, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, target) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "106_Floor_and_Ceil_in_Sorted_Array.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1
Problem Name: Floor and Ceil
Description: Find floor (largest element <= x) and ceil (smallest element >= x).

Folder: Binary_Search
File: 106_Floor_and_Ceil_in_Sorted_Array.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int], x: int) -> tuple[int, int]:
    # Find Floor
    low, high = 0, len(arr) - 1
    floor = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            floor = arr[mid]
            low = mid + 1
        else:
            high = mid - 1
            
    # Find Ceil
    low, high = 0, len(arr) - 1
    ceil = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ceil = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
            
    return floor, ceil

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([1, 2, 8, 10, 11, 12, 19], 8), (8, 8)),
        (([1, 2, 8, 10, 11, 12, 19], 5), (2, 8)),
        (([1, 2, 8, 10, 11, 12, 19], 0), (-1, 1))
    ]
    for idx, ((arr, x), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr, x) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "107_First_and_last_occurrence.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Problem Name: Find First and Last Position of Element in Sorted Array
Description: Find the starting and ending index of a given target value in sorted array.

Folder: Binary_Search
File: 107_First_and_last_occurrence.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int], target: int) -> list[int]:
    def find_first():
        low, high = 0, len(nums) - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first

    def find_last():
        low, high = 0, len(nums) - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last

    return [find_first(), find_last()]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([5, 7, 7, 8, 8, 10], 8), [3, 4]),
        (([5, 7, 7, 8, 8, 10], 6), [-1, -1])
    ]
    for idx, ((nums, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, target) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "108_Count_Occurrences_in_a_Sorted_Array.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1
Problem Name: Number of Occurrence
Description: Count occurrences of a target number in sorted array.

Folder: Binary_Search
File: 108_Count_Occurrences_in_a_Sorted_Array.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Count = Last Occurrence - First Occurrence + 1
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int], x: int) -> int:
    def get_first():
        l, r = 0, len(arr) - 1
        first = -1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == x:
                first = mid
                r = mid - 1
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return first

    def get_last():
        l, r = 0, len(arr) - 1
        last = -1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == x:
                last = mid
                l = mid + 1
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return last

    f = get_first()
    if f == -1:
        return 0
    return get_last() - f + 1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([1, 1, 2, 2, 2, 2, 3], 2), 4),
        (([1, 1, 2, 2, 2, 2, 3], 4), 0)
    ]
    for idx, ((arr, x), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr, x) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "109_Search_in_rotated_sorted_array_I.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
Problem Name: Search in Rotated Sorted Array
Description: Search for target in rotated sorted array of unique elements.

Folder: Binary_Search
File: 109_Search_in_rotated_sorted_array_I.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Identify the sorted half. Check if target lies in that half; else search other half.
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        # Left half sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([4, 5, 6, 7, 0, 1, 2], 0), 4),
        (([4, 5, 6, 7, 0, 1, 2], 3), -1)
    ]
    for idx, ((nums, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, target) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "110_Search_in_rotated_sorted_array_II.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
Problem Name: Search in Rotated Sorted Array II (with duplicates)
Description: Search target in rotated sorted array when duplicates are present.

Folder: Binary_Search
File: 110_Search_in_rotated_sorted_array_II.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Handle the edge case when nums[low] == nums[mid] == nums[high] by shrinking pointers.
# Time Complexity: O(log N) average, O(N) worst-case
# Space Complexity: O(1)
def optimal_solution(nums: list[int], target: int) -> bool:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
            
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue
            
        # Left half sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([2, 5, 6, 0, 0, 1, 2], 0), True),
        (([2, 5, 6, 0, 0, 1, 2], 3), False)
    ]
    for idx, ((nums, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, target) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "111_Find_minimum_in_Rotated_Sorted_Array.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Problem Name: Find Minimum in Rotated Sorted Array
Description: Find the minimum element in a rotated sorted array.

Folder: Binary_Search
File: 111_Find_minimum_in_Rotated_Sorted_Array.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: If left half sorted, nums[low] is potential min. Move search space to right half.
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    low, high = 0, len(nums) - 1
    ans = float('inf')
    while low <= high:
        mid = (low + high) // 2
        # Optimization: Entire segment sorted
        if nums[low] <= nums[high]:
            ans = min(ans, nums[low])
            break
        # Left half sorted
        if nums[low] <= nums[mid]:
            ans = min(ans, nums[low])
            low = mid + 1
        # Right half sorted
        else:
            ans = min(ans, nums[mid])
            high = mid - 1
    return ans

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0)
    ]
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "112_Find_out_how_many_times_the_array_is_rotated.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/rotation4755/1
Problem Name: Rotation Count
Description: Find out how many times the array is rotated (equivalent to index of minimum element).

Folder: Binary_Search
File: 112_Find_out_how_many_times_the_array_is_rotated.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: The rotation count is equal to the index of the minimum element.
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int]) -> int:
    low, high = 0, len(arr) - 1
    min_val = float('inf')
    ans_idx = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[low] <= arr[high]:
            if arr[low] < min_val:
                min_val = arr[low]
                ans_idx = low
            break
        if arr[low] <= arr[mid]:
            if arr[low] < min_val:
                min_val = arr[low]
                ans_idx = low
            low = mid + 1
        else:
            if arr[mid] < min_val:
                min_val = arr[mid]
                ans_idx = mid
            high = mid - 1
    return ans_idx

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        ([5, 1, 2, 3, 4], 1),
        ([4, 5, 6, 7, 0, 1, 2], 4)
    ]
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "113_Single_element_in_a_Sorted_Array.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/single-element-in-a-sorted-array/
Problem Name: Single Element in a Sorted Array
Description: Find the element that appears only once in a sorted array of duplicates.

Folder: Binary_Search
File: 113_Single_element_in_a_Sorted_Array.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Pairs before the single element start at (even, odd) indices.
# Pairs after the single element start at (odd, even) indices.
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]
    if nums[0] != nums[1]:
        return nums[0]
    if nums[-1] != nums[-2]:
        return nums[-1]
        
    low, high = 1, n - 2
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]
            
        # (even, odd) check
        if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
        ([3, 3, 7, 7, 10, 11, 11], 10)
    ]
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "114_Find_peak_element.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/find-peak-element/
Problem Name: Find Peak Element
Description: Find any peak element in array (strictly greater than neighbors).

Folder: Binary_Search
File: 114_Find_peak_element.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: If arr[mid] < arr[mid+1], a peak must lie on right side. Else on left.
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[-1] > nums[-2]:
        return n - 1
        
    low, high = 1, n - 2
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        ([1, 2, 3, 1], 2),
        ([1, 2, 1, 3, 5, 6, 4], 5) # index 5 has value 6
    ]
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "115_Find_square_root_of_a_number.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/square-root/1
Problem Name: Square Root of an Integer
Description: Find floor of square root of integer N.

Folder: Binary_Search
File: 115_Find_square_root_of_a_number.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(n: int) -> int:
    low, high = 1, n
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
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
        (5, 2),
        (16, 4),
        (0, 0)
    ]
    for idx, (n, expected) in enumerate(test_cases, 1):
        if n == 0:
            assert n == 0
            continue
        assert optimal_solution(n) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "116_Find_Nth_root_of_a_number.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/find-nth-root-of-m5843/1
Problem Name: Find Nth Root of M
Description: Find integer Nth root of M (return -1 if it's not an integer).

Folder: Binary_Search
File: 116_Find_Nth_root_of_a_number.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(log M)
# Space Complexity: O(1)
def optimal_solution(n: int, m: int) -> int:
    low, high = 1, m
    while low <= high:
        mid = (low + high) // 2
        val = mid ** n
        if val == m:
            return mid
        elif val < m:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        ((2, 9), 3),
        ((3, 27), 3),
        ((2, 8), -1)
    ]
    for idx, ((n, m), expected) in enumerate(test_cases, 1):
        assert optimal_solution(n, m) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "117_Koko_eating_bananas.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/koko-eating-bananas/
Problem Name: Koko Eating Bananas
Description: Find minimum integer speed K to eat all bananas in H hours.

Folder: Binary_Search
File: 117_Koko_eating_bananas.py
\"\"\"

import math

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary Search on speed K. Search range is [1, max(piles)].
# Time Complexity: O(N * log(max(piles)))
# Space Complexity: O(1)
def optimal_solution(piles: list[int], h: int) -> int:
    def can_eat_all(speed):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / speed)
        return hours <= h

    low, high = 1, max(piles)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if can_eat_all(mid):
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
        (([3, 6, 7, 11], 8), 4),
        (([30, 11, 23, 4, 20], 5), 30)
    ]
    for idx, ((piles, h), expected) in enumerate(test_cases, 1):
        assert optimal_solution(piles, h) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "118_Minimum_days_to_make_M_bouquets.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
Problem Name: Minimum Days to Make M Bouquets
Description: Find minimum days to make m bouquets using k adjacent flowers.

Folder: Binary_Search
File: 118_Minimum_days_to_make_M_bouquets.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary Search on days. Range is [min(bloomDay), max(bloomDay)].
# Time Complexity: O(N * log(max(bloomDay)))
# Space Complexity: O(1)
def optimal_solution(bloomDay: list[int], m: int, k: int) -> int:
    if m * k > len(bloomDay):
        return -1
        
    def can_make(days):
        bouquets = 0
        flowers = 0
        for b in bloomDay:
            if b <= days:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        return bouquets >= m

    low, high = min(bloomDay), max(bloomDay)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if can_make(mid):
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
        (([1, 10, 2, 9, 3, 8, 4, 7], 3, 2), 9),
        (([1, 10, 3, 10, 2], 3, 2), -1)
    ]
    for idx, ((bloomDay, m, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(bloomDay, m, k) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "119_Find_the_smallest_divisor.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
Problem Name: Find the Smallest Divisor Given a Threshold
Description: Find smallest divisor such that sum of division results is <= threshold.

Folder: Binary_Search
File: 119_Find_the_smallest_divisor.py
\"\"\"

import math

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary Search on divisor from 1 to max(nums).
# Time Complexity: O(N * log(max(nums)))
# Space Complexity: O(1)
def optimal_solution(nums: list[int], threshold: int) -> int:
    def get_sum(div):
        total = 0
        for x in nums:
            total += math.ceil(x / div)
        return total

    low, high = 1, max(nums)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if get_sum(mid) <= threshold:
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
        (([1, 2, 5, 9], 6), 5),
        (([44, 22, 33, 11, 1], 5), 44)
    ]
    for idx, ((nums, threshold), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, threshold) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "120_Capacity_to_Ship_Packages_Within_D_Days.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
Problem Name: Capacity to Ship Packages Within D Days
Description: Find minimum weight capacity to ship all packages in D days.

Folder: Binary_Search
File: 120_Capacity_to_Ship_Packages_Within_D_Days.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary Search on capacity in range [max(weights), sum(weights)].
# Time Complexity: O(N * log(sum(weights) - max(weights)))
# Space Complexity: O(1)
def optimal_solution(weights: list[int], days: int) -> int:
    def can_ship(capacity):
        curr_weight = 0
        curr_days = 1
        for w in weights:
            if curr_weight + w > capacity:
                curr_days += 1
                curr_weight = w
            else:
                curr_weight += w
        return curr_days <= days

    low, high = max(weights), sum(weights)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if can_ship(mid):
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
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15),
        (([3, 2, 2, 4, 1, 4], 3), 6)
    ]
    for idx, ((weights, days), expected) in enumerate(test_cases, 1):
        assert optimal_solution(weights, days) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "121_Kth_Missing_Positive_Number.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/kth-missing-positive-number/
Problem Name: Kth Missing Positive Number
Description: Find the kth missing positive integer.

Folder: Binary_Search
File: 121_Kth_Missing_Positive_Number.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: At index `mid`, the number of missing positives is `arr[mid] - (mid + 1)`.
# Time Complexity: O(log N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int], k: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        missing = arr[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    # Result formula: low + k
    return low + k

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([2, 3, 4, 7, 11], 5), 9),
        (([1, 2, 3, 4], 2), 6)
    ]
    for idx, ((arr, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr, k) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "122_Aggressive_Cows.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/aggressive-cows-problem/
Problem Name: Aggressive Cows
Description: Place C cows in stalls such that the minimum distance between any two of them is maximized.

Folder: Binary_Search
File: 122_Aggressive_Cows.py
\"\"\"

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
""",

    "123_Book_Allocation_Problem.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/allocate-minimum-number-pages/
Problem Name: Allocate Books
Description: Allocate books to M students such that the maximum pages allocated to a student is minimized.

Folder: Binary_Search
File: 123_Book_Allocation_Problem.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary Search on the maximum pages in range [max(arr), sum(arr)].
# Time Complexity: O(N log(sum - max))
# Space Complexity: O(1)
def optimal_solution(arr: list[int], m: int) -> int:
    if m > len(arr):
        return -1
        
    def count_students(max_pages):
        students = 1
        pages = 0
        for x in arr:
            if pages + x <= max_pages:
                pages += x
            else:
                students += 1
                pages = x
        return students

    low, high = max(arr), sum(arr)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if count_students(mid) <= m:
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
        (([12, 34, 67, 90], 2), 113)
    ]
    for idx, ((arr, m), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr, m) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "124_Split_array_largest_sum.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/split-array-largest-sum/
Problem Name: Split Array Largest Sum
Description: Split array into k subarrays minimizing the maximum sum.

Folder: Binary_Search
File: 124_Split_array_largest_sum.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Equivalent to the Book Allocation Problem.
# Time Complexity: O(N log(sum - max))
# Space Complexity: O(1)
def optimal_solution(nums: list[int], k: int) -> int:
    if k > len(nums):
        return -1
        
    def count_splits(max_sum):
        splits = 1
        curr_sum = 0
        for x in nums:
            if curr_sum + x <= max_sum:
                curr_sum += x
            else:
                splits += 1
                curr_sum = x
        return splits

    low, high = max(nums), sum(nums)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if count_splits(mid) <= k:
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
        (([7, 2, 5, 10, 8], 2), 18)
    ]
    for idx, ((nums, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, k) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "125_Painters_Partition.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/the-painters-partition-problem1353/1
Problem Name: Painter's Partition
Description: Paint boards of varying lengths among K painters to minimize max time.

Folder: Binary_Search
File: 125_Painters_Partition.py
\"\"\"

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
""",

    "126_Minimize_Max_Distance_to_Gas_Station.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1
Problem Name: Minimize Max Distance to Gas Station
Description: Minimize maximum distance between adjacent gas stations after adding K new stations.

Folder: Binary_Search
File: 126_Minimize_Max_Distance_to_Gas_Station.py
\"\"\"

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
""",

    "127_Median_of_2_sorted_arrays.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
Problem Name: Median of Two Sorted Arrays
Description: Find the median of two sorted arrays in O(log(min(n, m))) time.

Folder: Binary_Search
File: 127_Median_of_2_sorted_arrays.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary search on partition of the smaller array.
# Time Complexity: O(log(min(N, M)))
# Space Complexity: O(1)
def optimal_solution(nums1: list[int], nums2: list[int]) -> float:
    if len(nums1) > len(nums2):
        return optimal_solution(nums2, nums1)
        
    n1, n2 = len(nums1), len(nums2)
    low, high = 0, n1
    half = (n1 + n2 + 1) // 2
    
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = half - cut1
        
        l1 = nums1[cut1-1] if cut1 > 0 else -float('inf')
        l2 = nums2[cut2-1] if cut2 > 0 else -float('inf')
        r1 = nums1[cut1] if cut1 < n1 else float('inf')
        r2 = nums2[cut2] if cut2 < n2 else float('inf')
        
        if l1 <= r2 and l2 <= r1:
            if (n1 + n2) % 2 == 1:
                return float(max(l1, l2))
            return (max(l1, l2) + min(r1, r2)) / 2.0
        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1
            
    return 0.0

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([1, 3], [2]), 2.0),
        (([1, 2], [3, 4]), 2.5)
    ]
    for idx, ((n1, n2), expected) in enumerate(test_cases, 1):
        assert optimal_solution(n1, n2) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "128_Kth_element_of_2_sorted_arrays.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1
Problem Name: K-th Element of Two Sorted Arrays
Description: Find the kth element in the final sorted array of two sorted arrays.

Folder: Binary_Search
File: 128_Kth_element_of_2_sorted_arrays.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Similar to Median of Two Sorted Arrays, binary search on partition cut.
# Time Complexity: O(log(min(N, M)))
# Space Complexity: O(1)
def optimal_solution(arr1: list[int], arr2: list[int], k: int) -> int:
    n1, n2 = len(arr1), len(arr2)
    if n1 > n2:
        return optimal_solution(arr2, arr1, k)
        
    low = max(0, k - n2)
    high = min(k, n1)
    
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = k - cut1
        
        l1 = arr1[cut1-1] if cut1 > 0 else -float('inf')
        l2 = arr2[cut2-1] if cut2 > 0 else -float('inf')
        r1 = arr1[cut1] if cut1 < n1 else float('inf')
        r2 = arr2[cut2] if cut2 < n2 else float('inf')
        
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1
            
    return -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([2, 3, 6, 7, 9], [1, 4, 8, 10], 5), 6)
    ]
    for idx, ((arr1, arr2, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr1, arr2, k) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "129_Find_row_with_maximum_1s.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1
Problem Name: Row with Max 1s
Description: Find row index with maximum number of 1s in a boolean 2D array.

Folder: Binary_Search
File: 129_Find_row_with_maximum_1s.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Start at top-right corner. Move left if cell is 1, move down if cell is 0.
# Time Complexity: O(N + M)
# Space Complexity: O(1)
def optimal_solution(matrix: list[list[int]]) -> int:
    if not matrix:
        return -1
    n = len(matrix)
    m = len(matrix[0])
    
    r = 0
    c = m - 1
    max_row = -1
    
    while r < n and c >= 0:
        if matrix[r][c] == 1:
            max_row = r
            c -= 1
        else:
            r += 1
            
    return max_row

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        ([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]], 2)
    ]
    for idx, (mat, expected) in enumerate(test_cases, 1):
        assert optimal_solution(mat) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "130_Search_in_a_2D_matrix.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/search-a-2d-matrix/
Problem Name: Search a 2D Matrix
Description: Search target in 2D matrix where rows are sorted and first integer of each row is greater than last.

Folder: Binary_Search
File: 130_Search_in_a_2D_matrix.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Treat the 2D matrix as a flattened 1D array of size N * M.
# Time Complexity: O(log(N * M))
# Space Complexity: O(1)
def optimal_solution(matrix: list[list[int]], target: int) -> bool:
    if not matrix:
        return False
    n, m = len(matrix), len(matrix[0])
    low, high = 0, n * m - 1
    
    while low <= high:
        mid = (low + high) // 2
        r = mid // m
        c = mid % m
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), True),
        (([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13), False)
    ]
    for idx, ((mat, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(mat, target) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "131_Search_in_2D_matrix_II.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/search-a-2d-matrix-ii/
Problem Name: Search a 2D Matrix II
Description: Search target in a 2D matrix where rows and columns are sorted.

Folder: Binary_Search
File: 131_Search_in_2D_matrix_II.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Start at top-right corner. Move left if target < cell, down if target > cell.
# Time Complexity: O(N + M)
# Space Complexity: O(1)
def optimal_solution(matrix: list[list[int]], target: int) -> bool:
    if not matrix:
        return False
    n, m = len(matrix), len(matrix[0])
    r, c = 0, m - 1
    
    while r < n and c >= 0:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            c -= 1
        else:
            r += 1
            
    return False

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        (([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22]], 5), True),
        (([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22]], 20), False)
    ]
    for idx, ((mat, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(mat, target) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "132_Find_Peak_Element_II.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/find-a-peak-element-ii/
Problem Name: Find a Peak Element II (2D Peak)
Description: Find a peak element in a 2D grid.

Folder: Binary_Search
File: 132_Find_Peak_Element_II.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary search on columns. Find row with max element in the column.
# Compare with neighbors on left and right columns.
# Time Complexity: O(M * log N) where M is row count and N is col count.
# Space Complexity: O(1)
def optimal_solution(mat: list[list[int]]) -> list[int]:
    n = len(mat)
    m = len(mat[0])
    low = 0
    high = m - 1
    
    while low <= high:
        mid_col = (low + high) // 2
        
        # Find row with max element in mid_col
        max_row = 0
        for r in range(n):
            if mat[r][mid_col] > mat[max_row][mid_col]:
                max_row = r
                
        left_val = mat[max_row][mid_col - 1] if mid_col > 0 else -1
        right_val = mat[max_row][mid_col + 1] if mid_col < m - 1 else -1
        
        if mat[max_row][mid_col] > left_val and mat[max_row][mid_col] > right_val:
            return [max_row, mid_col]
        elif mat[max_row][mid_col] < left_val:
            high = mid_col - 1
        else:
            low = mid_col + 1
            
    return [-1, -1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    test_cases = [
        ([[1, 4], [3, 2]], [0, 1]), # 4 is a peak
        ([[10, 20, 15], [21, 30, 14], [7, 16, 32]], [1, 1]) # 30 is a peak
    ]
    for idx, (mat, expected) in enumerate(test_cases, 1):
        assert optimal_solution(mat) == expected, f"Test case {idx} failed"
    print("Done.")
""",

    "133_Matrix_Median.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/matrix-median0728/1
Problem Name: Matrix Median
Description: Find the median of a row-wise sorted matrix of odd dimensions.

Folder: Binary_Search
File: 133_Matrix_Median.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Binary search on the answer value in range [1, 10^9].
# For a candidate value, count how many elements are <= mid using Upper Bound.
# Time Complexity: O(32 * N * log M)
# Space Complexity: O(1)
def optimal_solution(matrix: list[list[int]]) -> int:
    n = len(matrix)
    m = len(matrix[0])
    
    def count_less_equal(x):
        count = 0
        for r in range(n):
            # Binary search to count elements <= x in row r
            low, high = 0, m - 1
            ans = 0
            while low <= high:
                mid = (low + high) // 2
                if matrix[r][mid] <= x:
                    ans = mid + 1
                    low = mid + 1
                else:
                    high = mid - 1
            count += ans
        return count

    low = 1
    high = int(1e9)
    req = (n * m + 1) // 2
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        if count_less_equal(mid) >= req:
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
        ([[1, 3, 5], [2, 6, 9], [3, 6, 9]], 5)
    ]
    for idx, (mat, expected) in enumerate(test_cases, 1):
        assert optimal_solution(mat) == expected, f"Test case {idx} failed"
    print("Done.")
"""
}

def main():
    target_dir = os.path.join(".", "DSA-Knowledge", "Binary_Search", "Code")
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
        
    print("All Binary Search code solutions populated successfully!")

if __name__ == "__main__":
    main()
