import os

SOLUTIONS = {
    "062_Largest_Element.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/largest-element-in-array5009/1
Problem Name: Largest Element in Array
Description: Given an array A[], find the largest element in it.

Folder: Arrays
File: 062_Largest_Element.py
\"\"\"

# ============================================
# BRUTE FORCE APPROACH
# ============================================
# Idea: Sort the array in ascending order and return the last element.
# Time Complexity: O(N log N) due to sorting.
# Space Complexity: O(1) auxiliary space (or O(N) depending on sort implementation).
def brute_force_solution(arr: list[int]) -> int:
    if not arr:
        return -1
    arr_copy = sorted(arr)
    return arr_copy[-1]

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep track of the maximum element seen so far as we traverse the array.
# Time Complexity: O(N) single pass.
# Space Complexity: O(1) constant space.
def optimal_solution(arr: list[int]) -> int:
    if not arr:
        return -1
    max_val = arr[0]
    for val in arr:
        if val > max_val:
            max_val = val
    return max_val

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests for Largest Element...")
    
    test_cases = [
        ([1, 8, 7, 56, 90], 90),
        ([1, 2, 0, 3, 2, 4, 5], 5),
        ([-10, -2, -30, -4], -2)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "063_Second_Largest_Element.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/second-largest3735/1
Problem Name: Second Largest Element
Description: Find the second largest distinct element in an array without sorting.

Folder: Arrays
File: 063_Second_Largest_Element.py
\"\"\"

# ============================================
# BRUTE FORCE APPROACH
# ============================================
# Idea: Sort the array, find the maximum, and scan backwards to find the first different element.
# Time Complexity: O(N log N)
# Space Complexity: O(1)
def brute_force_solution(arr: list[int]) -> int:
    if len(arr) < 2:
        return -1
    sorted_arr = sorted(arr)
    largest = sorted_arr[-1]
    for i in range(len(sorted_arr) - 2, -1, -1):
        if sorted_arr[i] != largest:
            return sorted_arr[i]
    return -1

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Maintain 'largest' and 'second_largest' during a single pass.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int]) -> int:
    if len(arr) < 2:
        return -1
    largest = -float('inf')
    second_largest = -float('inf')
    
    for x in arr:
        if x > largest:
            second_largest = largest
            largest = x
        elif x > second_largest and x != largest:
            second_largest = x
            
    return second_largest if second_largest != -float('inf') else -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests for Second Largest...")
    
    test_cases = [
        ([12, 35, 1, 10, 34, 1], 34),
        ([10, 10, 10], -1),
        ([1, 2, 5, 4, 3, 5], 4)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "064_Check_if_the_Array_is_Sorted_II.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
Problem Name: Check if Array Is Sorted and Rotated
Description: Check if the array can be sorted by rotating it some number of positions.

Folder: Arrays
File: 064_Check_if_the_Array_is_Sorted_II.py
\"\"\"

# ============================================
# BRUTE FORCE APPROACH
# ============================================
# Idea: Check every possible rotation to see if it is sorted.
# Time Complexity: O(N^2)
# Space Complexity: O(N)
def brute_force_solution(nums: list[int]) -> bool:
    n = len(nums)
    for rot in range(n):
        rotated = nums[rot:] + nums[:rot]
        is_sorted = True
        for i in range(1, n):
            if rotated[i] < rotated[i-1]:
                is_sorted = False
                break
        if is_sorted:
            return True
    return False

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: If an array is sorted and rotated, there can be at most one element 
# that is strictly greater than its next element (wrapping around to index 0).
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> bool:
    n = len(nums)
    count = 0
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count += 1
    return count <= 1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([3, 4, 5, 1, 2], True),
        ([2, 1, 3, 4], False),
        ([1, 2, 3], True)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "065_Remove_duplicates_from_Sorted_array.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Problem Name: Remove Duplicates from Sorted Array
Description: Remove duplicates in-place from sorted array, returning new length.

Folder: Arrays
File: 065_Remove_duplicates_from_Sorted_array.py
\"\"\"

# ============================================
# BRUTE FORCE APPROACH
# ============================================
# Idea: Store elements in a Set, then copy back to array.
# Time Complexity: O(N)
# Space Complexity: O(N)
def brute_force_solution(nums: list[int]) -> int:
    unique_set = sorted(list(set(nums)))
    for i in range(len(unique_set)):
        nums[i] = unique_set[i]
    return len(unique_set)

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Use two pointers: one for tracking unique index, one for scanning.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        # We need to copy arr to check mutations
        arr_copy = arr[:]
        assert optimal_solution(arr_copy) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "066_Left_Rotate_Array_by_One.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/left-rotate-an-array-by-one/1
Problem Name: Left Rotate Array by One
Description: Shift all elements left by one index. First element goes to the end.

Folder: Arrays
File: 066_Left_Rotate_Array_by_One.py
\"\"\"

# ============================================
# BRUTE FORCE APPROACH / OPTIMAL APPROACH
# ============================================
# Idea: Save the first element, shift all elements left, then place saved element at end.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int]) -> list[int]:
    if not arr:
        return arr
    temp = arr[0]
    for i in range(len(arr) - 1):
        arr[i] = arr[i+1]
    arr[-1] = temp
    return arr

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([1, 2, 3, 4, 5], [2, 3, 4, 5, 1]),
        ([3], [3])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr[:]) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "067_Left_Rotate_Array_by_K_Places.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/rotate-array/
Problem Name: Rotate Array by K Places (Left variant)
Description: Left rotate the array by k steps.

Folder: Arrays
File: 067_Left_Rotate_Array_by_K_Places.py
\"\"\"

# ============================================
# BRUTE FORCE APPROACH
# ============================================
# Idea: Store first k elements in a temp array, shift remaining elements left, copy temp back.
# Time Complexity: O(N)
# Space Complexity: O(k)
def brute_force_solution(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    k = k % n
    temp = arr[:k]
    for i in range(n - k):
        arr[i] = arr[i + k]
    for i in range(k):
        arr[n - k + i] = temp[i]
    return arr

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Reverse first k, reverse remaining, then reverse the entire array.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    if n == 0:
        return arr
    k = k % n
    
    def reverse(l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
            
    reverse(0, k - 1)
    reverse(k, n - 1)
    reverse(0, n - 1)
    return arr

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (([1, 2, 3, 4, 5, 6, 7], 3), [4, 5, 6, 7, 1, 2, 3]),
        (([1, 2], 3), [2, 1])
    ]
    
    for idx, ((arr, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr[:], k) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "068_Move_Zeros_to_End.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/move-zeroes/
Problem Name: Move Zeroes
Description: Move all 0s to the end of the array while maintaining relative order of non-zero elements.

Folder: Arrays
File: 068_Move_Zeros_to_End.py
\"\"\"

# ============================================
# BRUTE FORCE APPROACH
# ============================================
# Idea: Store non-zero elements in a temp list, then fill the rest of the array with zeroes.
# Time Complexity: O(N)
# Space Complexity: O(N)
def brute_force_solution(nums: list[int]) -> list[int]:
    temp = [x for x in nums if x != 0]
    for i in range(len(temp)):
        nums[i] = temp[i]
    for i in range(len(temp), len(nums)):
        nums[i] = 0
    return nums

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Use a pointer for the next position of non-zero element. Swap when non-zero found.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> list[int]:
    last_non_zero = 0
    for curr in range(len(nums)):
        if nums[curr] != 0:
            nums[last_non_zero], nums[curr] = nums[curr], nums[last_non_zero]
            last_non_zero += 1
    return nums

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr[:]) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "069_Linear_Search.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1
Problem Name: Linear Search
Description: Search for an element in an array. Return index if found, else -1.

Folder: Arrays
File: 069_Linear_Search.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int], target: int) -> int:
    for idx, val in enumerate(arr):
        if val == target:
            return idx
    return -1

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (([1, 2, 3, 4, 5], 3), 2),
        (([1, 2, 3, 4, 5], 6), -1)
    ]
    
    for idx, ((arr, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr, target) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "070_Union_of_two_sorted_arrays.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1
Problem Name: Union of Two Sorted Arrays
Description: Given two sorted arrays, find their union.

Folder: Arrays
File: 070_Union_of_two_sorted_arrays.py
\"\"\"

# ============================================
# BRUTE FORCE APPROACH
# ============================================
# Idea: Insert all elements of both arrays into a sorted Set.
# Time Complexity: O((N + M) log(N + M))
# Space Complexity: O(N + M)
def brute_force_solution(arr1: list[int], arr2: list[int]) -> list[int]:
    return sorted(list(set(arr1 + arr2)))

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Use two pointers to merge sorted arrays while skipping duplicates.
# Time Complexity: O(N + M)
# Space Complexity: O(1) auxiliary space (excluding result)
def optimal_solution(arr1: list[int], arr2: list[int]) -> list[int]:
    i, j = 0, 0
    union = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
            
    while i < len(arr1):
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1
        
    return union

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (([1, 2, 3, 4, 5], [2, 3, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7]),
        (([1, 1, 1], [2, 2]), [1, 2])
    ]
    
    for idx, ((arr1, arr2), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr1, arr2) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "071_Find_missing_number.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/missing-number/
Problem Name: Missing Number
Description: Find the single missing number in the range [0, N] from an array of size N.

Folder: Arrays
File: 071_Find_missing_number.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Calculate expected sum of [0, N] and subtract the array sum.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([3, 0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "072_Maximum_Consecutive_Ones.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/max-consecutive-ones/
Problem Name: Max Consecutive Ones
Description: Find the maximum number of consecutive 1s in a binary array.

Folder: Arrays
File: 072_Maximum_Consecutive_Ones.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Reset count to 0 when 0 is seen, update max_count at each step.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    max_count = 0
    curr_count = 0
    for num in nums:
        if num == 1:
            curr_count += 1
            max_count = max(max_count, curr_count)
        else:
            curr_count = 0
    return max_count

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([1, 1, 0, 1, 1, 1], 3),
        ([1, 0, 1, 1, 0, 1], 2)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "073_Find_the_number_that_appears_once_and_other_numbers_twice.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/single-number/
Problem Name: Single Number
Description: Given a non-empty array of integers where every element appears twice except for one, find that single one.

Folder: Arrays
File: 073_Find_the_number_that_appears_once_and_other_numbers_twice.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: XORing a number with itself cancels it out (x ^ x = 0). XORing with 0 preserves (x ^ 0 = x).
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    xor = 0
    for num in nums:
        xor ^= num
    return xor

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "074_Longest_subarray_with_given_sum_Kpositives.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k8645/1
Problem Name: Longest Subarray with Sum K (Positives)
Description: Find length of longest subarray with sum K in positive integer array.

Folder: Arrays
File: 074_Longest_subarray_with_given_sum_Kpositives.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Two pointer / sliding window. Expand right, shrink left when sum exceeds K.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int], k: int) -> int:
    l = 0
    curr_sum = 0
    max_len = 0
    
    for r in range(len(arr)):
        curr_sum += arr[r]
        while curr_sum > k and l <= r:
            curr_sum -= arr[l]
            l += 1
        if curr_sum == k:
            max_len = max(max_len, r - l + 1)
            
    return max_len

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (([1, 2, 3, 1, 1, 1, 1], 3), 4),
        (([1, 4, 3, 3, 5, 5], 16), 0)
    ]
    
    for idx, ((arr, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr, k) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "075_Longest_subarray_with_sum_K.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k8645/1
Problem Name: Longest Subarray with Sum K (Positives, Negatives, Zeros)
Description: Find length of longest subarray with sum K.

Folder: Arrays
File: 075_Longest_subarray_with_sum_K.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Map prefix_sum to its first occurrence index. If prefix_sum - K is in map, compute length.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(arr: list[int], k: int) -> int:
    prefix_map = {}
    curr_sum = 0
    max_len = 0
    
    for i in range(len(arr)):
        curr_sum += arr[i]
        
        if curr_sum == k:
            max_len = i + 1
            
        rem = curr_sum - k
        if rem in prefix_map:
            max_len = max(max_len, i - prefix_map[rem])
            
        # Store only the first occurrence to maximize the length
        if curr_sum not in prefix_map:
            prefix_map[curr_sum] = i
            
    return max_len

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (([10, 5, 2, 7, 1, 9], 15), 4),
        (([-1, 8, 5, -2, 2, -8, 1, 7], 0), 5)
    ]
    
    for idx, ((arr, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr, k) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "076_Two_Sum.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/two-sum/
Problem Name: Two Sum
Description: Find indices of two numbers that sum to K.

Folder: Arrays
File: 076_Two_Sum.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Use HashMap to store indices of visited elements. Look up target - num.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(nums: list[int], target: int) -> list[int]:
    visited = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in visited:
            return [visited[complement], i]
        visited[num] = i
    return []

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2])
    ]
    
    for idx, ((nums, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, target) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "077_Sort_an_array_of_0s_1s_and_2s.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/sort-colors/
Problem Name: Sort Colors (Sort array of 0s, 1s, and 2s)
Description: Sort an array with 0s, 1s, and 2s in-place.

Folder: Arrays
File: 077_Sort_an_array_of_0s_1s_and_2s.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Dutch National Flag Algorithm. Pointers low, mid, high.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> list[int]:
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr[:]) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "078_Majority_Element_I.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/majority-element/
Problem Name: Majority Element (> N/2)
Description: Find the element that appears more than N/2 times.

Folder: Arrays
File: 078_Majority_Element_I.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Boyer-Moore Voting Algorithm. Candidate selection with cancellation.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    return candidate

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "079_Kadanes_Algorithm.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/maximum-subarray/
Problem Name: Maximum Subarray Sum (Kadane's Algorithm)
Description: Find the contiguous subarray which has the largest sum.

Folder: Arrays
File: 079_Kadanes_Algorithm.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Accumulate running sum. Reset to 0 if sum drops below 0. Track max.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    max_sum = nums[0]
    curr_sum = 0
    for x in nums:
        curr_sum += x
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "080_Print_subarray_with_maximum_subarray_sum.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/maximum-sub-array5543/1
Problem Name: Print Subarray with Maximum Subarray Sum
Description: Find and return the actual subarray with the maximum sum.

Folder: Arrays
File: 080_Print_subarray_with_maximum_subarray_sum.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep track of start and end indices of the max subarray window.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> list[int]:
    max_sum = nums[0]
    curr_sum = 0
    start = 0
    temp_start = 0
    end = 0
    
    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i
            
        if curr_sum < 0:
            curr_sum = 0
            temp_start = i + 1
            
    return nums[start:end+1]

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], [4, -1, 2, 1]),
        ([1], [1])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "081_Stock_Buy_and_Sell.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Problem Name: Stock Buy and Sell
Description: Maximize single transaction profit.

Folder: Arrays
File: 081_Stock_Buy_and_Sell.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep minimum price seen, check profit on selling at current day.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(prices: list[int]) -> int:
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
        
    return max_profit

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "082_Rearrange_array_elements_by_sign.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/rearrange-array-elements-by-sign/
Problem Name: Rearrange Array Elements by Sign
Description: Rearrange array into alternating positive and negative values.

Folder: Arrays
File: 082_Rearrange_array_elements_by_sign.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Single pass with two pointer indices pointing to even/odd placements.
# Time Complexity: O(N)
# Space Complexity: O(N) for output array
def optimal_solution(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [0] * n
    pos_idx = 0
    neg_idx = 1
    
    for x in nums:
        if x > 0:
            res[pos_idx] = x
            pos_idx += 2
        else:
            res[neg_idx] = x
            neg_idx += 2
            
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([3, 1, -2, -5, 2, -4], [3, -2, 1, -5, 2, -4]),
        ([-1, 1], [1, -1])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "083_Next_Permutation.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/next-permutation/
Problem Name: Next Permutation
Description: Find the next lexicographical permutation of numbers.

Folder: Arrays
File: 083_Next_Permutation.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: 
# 1. Find pivot (first decreasing index from right).
# 2. Swap pivot with smallest larger element on its right.
# 3. Reverse elements after pivot.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> list[int]:
    n = len(nums)
    pivot = -1
    
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot = i
            break
            
    if pivot == -1:
        nums.reverse()
        return nums
        
    for i in range(n - 1, pivot, -1):
        if nums[i] > nums[pivot]:
            nums[pivot], nums[i] = nums[i], nums[pivot]
            break
            
    # Reverse subarray nums[pivot+1:]
    nums[pivot+1:] = reversed(nums[pivot+1:])
    return nums

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr[:]) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "084_Leaders_in_an_Array.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1
Problem Name: Leaders in an Array
Description: Find all elements that are greater than all elements to their right.

Folder: Arrays
File: 084_Leaders_in_an_Array.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Scan from right to left, tracking maximum element seen so far.
# Time Complexity: O(N)
# Space Complexity: O(1) auxiliary (excluding result)
def optimal_solution(arr: list[int]) -> list[int]:
    n = len(arr)
    if n == 0:
        return []
    leaders = []
    max_val = arr[-1]
    leaders.append(max_val)
    
    for i in range(n - 2, -1, -1):
        if arr[i] >= max_val:
            max_val = arr[i]
            leaders.append(max_val)
            
    leaders.reverse()
    return leaders

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([16, 17, 4, 3, 5, 2], [17, 5, 2]),
        ([1, 2, 3, 4, 5], [5])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "085_Longest_Consecutive_Sequence_in_an_Array.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/longest-consecutive-sequence/
Problem Name: Longest Consecutive Sequence
Description: Find length of longest consecutive elements sequence.

Folder: Arrays
File: 085_Longest_Consecutive_Sequence_in_an_Array.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Put all numbers in Set. Traverse numbers, start count only if num-1 is not in Set.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(nums: list[int]) -> int:
    num_set = set(nums)
    max_streak = 0
    
    for num in num_set:
        # Check if it's the start of a sequence
        if num - 1 not in num_set:
            curr_num = num
            curr_streak = 1
            
            while curr_num + 1 in num_set:
                curr_num += 1
                curr_streak += 1
                
            max_streak = max(max_streak, curr_streak)
            
    return max_streak

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "086_Set_Matrix_Zeroes.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/set-matrix-zeroes/
Problem Name: Set Matrix Zeroes
Description: If an element is 0, set its entire row and column to 0.

Folder: Arrays
File: 086_Set_Matrix_Zeroes.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Use first row and first column of matrix as markers. 
# Track if first row/col themselves need to be zeroed using separate boolean flags.
# Time Complexity: O(N * M)
# Space Complexity: O(1)
def optimal_solution(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix:
        return matrix
    n, m = len(matrix), len(matrix[0])
    first_row_zero = False
    first_col_zero = False
    
    # Check if first row/col has zeros
    for j in range(m):
        if matrix[0][j] == 0:
            first_row_zero = True
    for i in range(n):
        if matrix[i][0] == 0:
            first_col_zero = True
            
    # Mark zeros in first row/col
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
                
    # Update cells using markers
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
                
    # Update first row/col if needed
    if first_row_zero:
        for j in range(m):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(n):
            matrix[i][0] = 0
            
    return matrix

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
    ]
    
    for idx, (mat, expected) in enumerate(test_cases, 1):
        # deep copy
        mat_copy = [row[:] for row in mat]
        assert optimal_solution(mat_copy) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "087_Rotate_matrix_by_90_degrees.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/rotate-image/
Problem Name: Rotate Image (Rotate matrix by 90 degrees)
Description: Rotate N x N matrix by 90 degrees clockwise in-place.

Folder: Arrays
File: 087_Rotate_matrix_by_90_degrees.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Transpose the matrix (swap matrix[i][j] with matrix[j][i]), then reverse each row.
# Time Complexity: O(N^2)
# Space Complexity: O(1)
def optimal_solution(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    
    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # Reverse rows
    for i in range(n):
        matrix[i].reverse()
        
    return matrix

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
    ]
    
    for idx, (mat, expected) in enumerate(test_cases, 1):
        mat_copy = [row[:] for row in mat]
        assert optimal_solution(mat_copy) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "088_Print_the_matrix_in_spiral_manner.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/spiral-matrix/
Problem Name: Spiral Matrix
Description: Return all elements of the matrix in spiral order.

Folder: Arrays
File: 088_Print_the_matrix_in_spiral_manner.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep track of boundaries: top, bottom, left, right. Traverse boundaries spirally.
# Time Complexity: O(N * M)
# Space Complexity: O(1)
def optimal_solution(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []
        
    n, m = len(matrix), len(matrix[0])
    top, bottom = 0, n - 1
    left, right = 0, m - 1
    result = []
    
    while top <= bottom and left <= right:
        # Traverse Left to Right on Top row
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        
        # Traverse Top to Bottom on Right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Check if rows are exhausted
        if top <= bottom:
            # Traverse Right to Left on Bottom row
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
            
        # Check if columns are exhausted
        if left <= right:
            # Traverse Bottom to Top on Left column
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            
    return result

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5])
    ]
    
    for idx, (mat, expected) in enumerate(test_cases, 1):
        assert optimal_solution(mat) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "089_Count_subarrays_with_given_sum.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/subarray-sum-equals-k/
Problem Name: Subarray Sum Equals K
Description: Find the total number of continuous subarrays whose sum equals to K.

Folder: Arrays
File: 089_Count_subarrays_with_given_sum.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep track of prefix sum count in a HashMap. Check if curr_sum - K exists in map.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(nums: list[int], k: int) -> int:
    prefix_counts = {0: 1}
    curr_sum = 0
    count = 0
    
    for x in nums:
        curr_sum += x
        rem = curr_sum - k
        if rem in prefix_counts:
            count += prefix_counts[rem]
        prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
        
    return count

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (([1, 1, 1], 2), 2),
        (([1, 2, 3], 3), 2)
    ]
    
    for idx, ((nums, k), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, k) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "090_Pascals_Triangle_I.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/pascals-triangle/
Problem Name: Pascal's Triangle
Description: Generate the first numRows of Pascal's triangle.

Folder: Arrays
File: 090_Pascals_Triangle_I.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Each element of a row is the sum of the two elements directly above it.
# Time Complexity: O(numRows^2)
# Space Complexity: O(numRows^2) for the output triangle structure
def optimal_solution(numRows: int) -> list[list[int]]:
    triangle = []
    for r in range(numRows):
        row = [1] * (r + 1)
        for j in range(1, r):
            row[j] = triangle[r - 1][j - 1] + triangle[r - 1][j]
        triangle.append(row)
    return triangle

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]])
    ]
    
    for idx, (numRows, expected) in enumerate(test_cases, 1):
        assert optimal_solution(numRows) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "091_Majority_Element_II.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/majority-element-ii/
Problem Name: Majority Element II (> N/3)
Description: Find all elements that appear more than N/3 times.

Folder: Arrays
File: 091_Majority_Element_II.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Extended Boyer-Moore Voting Algorithm. There can be at most 2 majority elements.
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> list[int]:
    if not nums:
        return []
        
    cand1, cand2 = None, None
    count1, count2 = 0, 0
    
    for x in nums:
        if x == cand1:
            count1 += 1
        elif x == cand2:
            count2 += 1
        elif count1 == 0:
            cand1 = x
            count1 = 1
        elif count2 == 0:
            cand2 = x
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
            
    # Verify candidates
    res = []
    n = len(nums)
    if nums.count(cand1) > n // 3:
        res.append(cand1)
    if cand2 != cand1 and nums.count(cand2) > n // 3:
        res.append(cand2)
        
    return sorted(res)

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([3, 2, 3], [3]),
        ([1, 2], [1, 2])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "092_3_Sum.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/3sum/
Problem Name: 3Sum
Description: Find all unique triplets in the array which gives the sum of zero.

Folder: Arrays
File: 092_3_Sum.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Sort the array, loop i, then use two pointers j and k for remaining search.
# Time Complexity: O(N^2)
# Space Complexity: O(1) auxiliary (excluding result)
def optimal_solution(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    res = []
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        l, r = i + 1, n - 1
        while l < r:
            curr_sum = nums[i] + nums[l] + nums[r]
            if curr_sum == 0:
                res.append([nums[i], nums[l], nums[r]])
                # Skip duplicates for l and r
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            elif curr_sum < 0:
                l += 1
            else:
                r -= 1
                
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "093_4_Sum.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/4sum/
Problem Name: 4Sum
Description: Find all unique quadruplets which sum to target.

Folder: Arrays
File: 093_4_Sum.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Sort the array, two nested loops i and j, then two pointer search. Skip duplicates.
# Time Complexity: O(N^3)
# Space Complexity: O(1) auxiliary
def optimal_solution(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    res = []
    
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
                
            l, r = j + 1, n - 1
            while l < r:
                curr_sum = nums[i] + nums[j] + nums[l] + nums[r]
                if curr_sum == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif curr_sum < target:
                    l += 1
                else:
                    r -= 1
                    
    return res

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        (([1, 0, -1, 0, -2, 2], 0), [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])
    ]
    
    for idx, ((nums, target), expected) in enumerate(test_cases, 1):
        assert optimal_solution(nums, target) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "094_Largest_Subarray_with_Sum_0.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
Problem Name: Largest Subarray with 0 Sum
Description: Find length of the largest subarray with sum 0.

Folder: Arrays
File: 094_Largest_Subarray_with_Sum_0.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep track of prefix sums and their index. If seen before, sum over interval is 0.
# Time Complexity: O(N)
# Space Complexity: O(N)
def optimal_solution(arr: list[int]) -> int:
    prefix_map = {}
    curr_sum = 0
    max_len = 0
    
    for i in range(len(arr)):
        curr_sum += arr[i]
        
        if curr_sum == 0:
            max_len = i + 1
            
        if curr_sum in prefix_map:
            max_len = max(max_len, i - prefix_map[curr_sum])
        else:
            prefix_map[curr_sum] = i
            
    return max_len

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([15, -2, 2, -8, 1, 7, 10, 23], 5),
        ([1, 2, 3], 0)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "095_Count_subarrays_with_given_xor_K.py": """\"\"\"
LeetCode Link: https://www.interviewbit.com/problems/subarray-with-given-xor/
Problem Name: Subarrays with Given XOR
Description: Find the number of subarrays having XOR sum equal to B (or K).

Folder: Arrays
File: 095_Count_subarrays_with_given_xor_K.py
\"\"\"

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
""",

    "096_Merge_Overlapping_Subintervals.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/merge-intervals/
Problem Name: Merge Intervals
Description: Merge overlapping intervals.

Folder: Arrays
File: 096_Merge_Overlapping_Subintervals.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Sort intervals by start value. Iterate and merge overlapping.
# Time Complexity: O(N log N)
# Space Complexity: O(N)
def optimal_solution(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        current = intervals[i]
        last_merged = merged[-1]
        
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)
            
    return merged

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]])
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "097_Merge_two_sorted_arrays_without_extra_space.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
Problem Name: Merge Two Sorted Arrays Without Extra Space
Description: Merge elements of two sorted arrays A and B into both A and B sorted in-place.

Folder: Arrays
File: 097_Merge_two_sorted_arrays_without_extra_space.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Use Gap Method (Shell Sort based) to compare and swap elements at distance 'gap'.
# Time Complexity: O((N + M) log(N + M))
# Space Complexity: O(1)
def optimal_solution(arr1: list[int], arr2: list[int]) -> tuple[list[int], list[int]]:
    n, m = len(arr1), len(arr2)
    length = n + m
    gap = (length // 2) + (length % 2)
    
    def get_val(idx):
        if idx < n:
            return arr1[idx]
        return arr2[idx - n]
        
    def set_val(idx, val):
        if idx < n:
            arr1[idx] = val
        else:
            arr2[idx - n] = val
            
    while gap > 0:
        l = 0
        r = gap
        while r < length:
            if get_val(l) > get_val(r):
                temp = get_val(l)
                set_val(l, get_val(r))
                set_val(r, temp)
            l += 1
            r += 1
        if gap == 1:
            break
        gap = (gap // 2) + (gap % 2)
        
    return arr1, arr2

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    arr1, arr2 = [1, 3, 5, 7], [0, 2, 6, 8, 9]
    res1, res2 = optimal_solution(arr1[:], arr2[:])
    assert res1 == [0, 1, 2, 3] and res2 == [5, 6, 7, 8, 9], "Test failed"
    
    print("Done.")
""",

    "098_Find_the_repeating_and_missing_number.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/find-missing-and-repeating2512/1
Problem Name: Find Missing and Repeating Number
Description: Find the repeating and missing elements in an array containing elements from 1 to N.

Folder: Arrays
File: 098_Find_the_repeating_and_missing_number.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Math equations using S (Sum of numbers) and S2 (Sum of squares of numbers).
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(arr: list[int]) -> tuple[int, int]:
    n = len(arr)
    # Sn = Sum of 1 to N, S2n = Sum of squares of 1 to N
    Sn = n * (n + 1) // 2
    S2n = n * (n + 1) * (2 * n + 1) // 6
    
    S = sum(arr)
    S2 = sum(x*x for x in arr)
    
    # x = repeating, y = missing
    # S - Sn = x - y
    # S2 - S2n = x^2 - y^2 = (x - y)(x + y)
    val1 = S - Sn  # x - y
    val2 = S2 - S2n  # x^2 - y^2
    
    val3 = val2 // val1  # x + y
    
    x = (val1 + val3) // 2
    y = val3 - x
    
    return x, y

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([3, 1, 2, 5, 3], (3, 4)),
        ([4, 3, 6, 2, 1, 1], (1, 5))
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
""",

    "099_Count_Inversions.py": """\"\"\"
LeetCode Link: https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
Problem Name: Inversion Count
Description: Count number of inversion pairs (i < j and arr[i] > arr[j]).

Folder: Arrays
File: 099_Count_Inversions.py
\"\"\"

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
""",

    "100_Reverse_Pairs.py": "\"\"\"\nLeetCode Link: https://leetcode.com/problems/reverse-pairs/\nProblem Name: Reverse Pairs\nDescription: Given an integer array nums, return the number of reverse pairs (i < j and nums[i] > 2 * nums[j]).\n\nFolder: Arrays\nFile: 100_Reverse_Pairs.py\n\"\"\"\n\n# ============================================\n# OPTIMAL APPROACH\n# ============================================\n# Key Insight: Modify Merge Sort to count reverse pairs. \n# Time Complexity: O(N log N)\n# Space Complexity: O(N)\ndef optimal_solution(nums: list[int]) -> int:\n    def merge_sort(low, high):\n        if low >= high:\n            return 0\n        mid = (low + high) // 2\n        count = merge_sort(low, mid) + merge_sort(mid + 1, high)\n        count += count_pairs(low, mid, high)\n        merge(low, mid, high)\n        return count\n\n    def count_pairs(low, mid, high):\n        count = 0\n        right = mid + 1\n        for i in range(low, mid + 1):\n            while right <= high and nums[i] > 2 * nums[right]:\n                right += 1\n            count += (right - (mid + 1))\n        return count\n\n    def merge(low, mid, high):\n        temp = []\n        left = low\n        right = mid + 1\n        while left <= mid and right <= high:\n            if nums[left] <= nums[right]:\n                temp.append(nums[left])\n                left += 1\n            else:\n                temp.append(nums[right])\n                right += 1\n        while left <= mid:\n            temp.append(nums[left])\n            left += 1\n        while right <= high:\n            temp.append(nums[right])\n            right += 1\n        for i in range(low, high + 1):\n            nums[i] = temp[i - low]\n\n    return merge_sort(0, len(nums) - 1)\n\n# ============================================\n# TEST CASES\n# ============================================\nif __name__ == \"__main__\":\n    print(\"Running tests...\")\n    \n    test_cases = [\n        ([1, 3, 2, 3, 1], 2),\n        ([2, 4, 3, 5, 1], 3)\n    ]\n    \n    for idx, (arr, expected) in enumerate(test_cases, 1):\n        assert optimal_solution(arr[:]) == expected, f\"Test case {idx} failed\"\n        \n    print(\"Done.\")\n",

    "101_Maximum_Product_Subarray_in_an_Array.py": """\"\"\"
LeetCode Link: https://leetcode.com/problems/maximum-product-subarray/
Problem Name: Maximum Product Subarray
Description: Find contiguous subarray within an array which has the largest product.

Folder: Arrays
File: 101_Maximum_Product_Subarray_in_an_Array.py
\"\"\"

# ============================================
# OPTIMAL APPROACH
# ============================================
# Key Insight: Keep track of prefix product and suffix product. Max product is the max seen.
# If product becomes 0, reset to 1 (conceptually starting a new subarray).
# Time Complexity: O(N)
# Space Complexity: O(1)
def optimal_solution(nums: list[int]) -> int:
    n = len(nums)
    prefix = 1
    suffix = 1
    max_prod = -float('inf')
    
    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
            
        prefix *= nums[i]
        suffix *= nums[n - 1 - i]
        
        max_prod = max(max_prod, prefix, suffix)
        
    return max_prod

# ============================================
# TEST CASES
# ============================================
if __name__ == "__main__":
    print("Running tests...")
    
    test_cases = [
        ([2, 3, -2, 4], 6),
        ([-2, 0, -1], 0)
    ]
    
    for idx, (arr, expected) in enumerate(test_cases, 1):
        assert optimal_solution(arr) == expected, f"Test case {idx} failed"
        
    print("Done.")
"""
}

def main():
    target_dir = os.path.join(".", "DSA-Knowledge", "Arrays", "Code")
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
        
    print("All Arrays code solutions populated successfully!")

if __name__ == "__main__":
    main()
