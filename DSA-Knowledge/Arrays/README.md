# Arrays: Core Concepts, Patterns, and Revision Guide

An array is a contiguous memory structure representing a collection of elements of the same type. In interviews and computer science, arrays form the foundation for other data structures and are frequently paired with optimal time-space algorithms.

---

## Topic Overview & When to Use

Arrays are the starting point for modern DSA. They provide $O(1)$ random access, but inserting or deleting elements in the middle takes $O(N)$ time.

Use array techniques when:
- You need to search, filter, or partition contiguous sequences.
- Subarrays or subsequences are specified with target conditions (e.g., maximum sum, given sum $K$).
- You need to track frequencies or occurrences within a bounded range.
- Matrix problems (2D arrays) requiring coordinate-based navigation.

---

## Pattern Recognition Guide

| Pattern | Recognition Clue | Core Idea | Common Problems |
| :--- | :--- | :--- | :--- |
| **Two Pointers** | Sorted arrays, finding pairs/triplets, swapping in place | Maintain two indexes (left/right or slow/fast) to scan elements from different directions or speeds. | Two Sum, 3 Sum, Move Zeros |
| **Sliding Window** | Contiguous subarrays with size $K$ or sum $K$ properties | Expand a window using a right pointer and contract it from the left to maintain invariants. | Longest Subarray with Sum K |
| **Prefix Sum / XOR** | Subarray sum query, prefix/suffix relations | Precompute running sums or running XORs to answer range query questions in $O(1)$ time. | Count Subarrays with Sum K, Subarrays with XOR K |
| **Kadane's Algorithm** | Maximum subarray sum or product | Keep a running local optimum and update the global optimum at each index. | Max Subarray Sum, Max Product Subarray |
| **Dutch National Flag** | Sorting 3 distinct elements in-place | Maintain three boundaries (low, mid, high) and swap elements to their respective ends. | Sort 0s, 1s, and 2s |
| **Boyer-Moore Voting** | Find majority elements appearing $> N/2$ or $> N/3$ times | Maintain candidate counts that cancel each other out when different. | Majority Element I & II |
| **Matrix Layer Simulation** | Matrix rotations, spiral traversals | Track current boundaries (`top`, `bottom`, `left`, `right`) and adjust them as you traverse layers. | Spiral Matrix, Rotate Image |

---

## Common Interview Traps & Pitfalls

1. **Integer Overflow**: Calculating mid-points or running products that exceed $2^{31} - 1$.
2. **Off-by-One Errors**: Accessing indices out of bounds (e.g., accessing `arr[n]` instead of `arr[n-1]`).
3. **Array Mutation during Iteration**: Modifying array indices while iterating through it, causing index shifts.
4. **Duplicate Handling**: Forgetting to skip duplicate elements in sorted two-pointer traversals (e.g., in 3 Sum / 4 Sum).
5. **Static Size Limitations**: Inlanguages like C++, static arrays cannot be resized. Remember to use vectors or dynamic arrays.

---

## Learning & Revision Order

1. **Basics**: Largest, second largest, check sorted, remove duplicates, shift/rotate.
2. **Two Pointer / Sorting / Partitioning**: Move zeros, union, two sum, sort 0s 1s 2s.
3. **Subarray Accumulators**: Kadane's, maximum product, prefix sum, subarray sums.
4. **Frequency & Voting**: Majority elements, missing/repeating numbers.
5. **Advanced Sorting/Merging**: Merge intervals, merge sorted arrays, count inversions, reverse pairs.
6. **2D Arrays (Matrix)**: Set matrix zeroes, rotate image, spiral print.

---

## Important Templates

### 1. Two-Pointer (Opposite Ends)
```python
def two_pointer_template(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

### 2. Sliding Window (Variable Size)
```python
def sliding_window_template(arr, k):
    left = 0
    current_sum = 0
    max_len = 0
    for right in range(len(arr)):
        current_sum += arr[right]
        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1
        if current_sum == k:
            max_len = max(max_len, right - left + 1)
    return max_len
```

### 3. Prefix Sum with Hashing (Subarray Sum equals K)
```python
def prefix_sum_hash(arr, k):
    prefix_map = {0: 1} # sum -> count
    curr_sum = 0
    count = 0
    for num in arr:
        curr_sum += num
        if curr_sum - k in prefix_map:
            count += prefix_map[curr_sum - k]
        prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1
    return count
```

---

## Progress Tracker & Complexity Summary Table

| ID | Problem Name | Difficulty | Pattern | Brute Force | Optimal | Status |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: |
| 062 | [Largest Element](062_Largest_Element.md) | Easy | Iterative | $O(N \log N)$ / $O(1)$ | $O(N)$ / $O(1)$ | [ ] |
| 063 | [Second Largest Element](063_Second_Largest_Element.md) | Easy | Iterative | $O(N \log N)$ / $O(1)$ | $O(N)$ / $O(1)$ | [ ] |
| 064 | [Check if Array is Sorted](064_Check_if_the_Array_is_Sorted_II.md) | Easy | Iterative | $O(N^2)$ / $O(1)$ | $O(N)$ / $O(1)$ | [ ] |
| 065 | [Remove Duplicates](065_Remove_duplicates_from_Sorted_array.md) | Easy | Two Pointer | $O(N)$ / $O(N)$ | $O(N)$ / $O(1)$ | [ ] |
| 066 | [Left Rotate by One](066_Left_Rotate_Array_by_One.md) | Easy | Iterative | $O(N)$ / $O(N)$ | $O(N)$ / $O(1)$ | [ ] |
| 067 | [Left Rotate by K](067_Left_Rotate_Array_by_K_Places.md) | Easy | Array Reversal | $O(N \cdot K)$ / $O(1)$ | $O(N)$ / $O(1)$ | [ ] |
| 068 | [Move Zeros to End](068_Move_Zeros_to_End.md) | Easy | Two Pointer | $O(N)$ / $O(N)$ | $O(N)$ / $O(1)$ | [ ] |
| 069 | [Linear Search](069_Linear_Search.md) | Easy | Iterative | $O(N)$ / $O(1)$ | $O(N)$ / $O(1)$ | [ ] |
| 070 | [Union of Two Sorted Arrays](070_Union_of_two_sorted_arrays.md) | Easy | Two Pointer | $O((N+M)\log(N+M))$ | $O(N+M)$ / $O(N+M)$ | [ ] |
| 071 | [Find Missing Number](071_Find_missing_number.md) | Easy | Math / XOR | $O(N^2)$ / $O(1)$ | $O(N)$ / $O(1)$ | [ ] |
| 072 | [Max Consecutive Ones](072_Maximum_Consecutive_Ones.md) | Easy | Iterative | $O(N)$ / $O(1)$ | $O(N)$ / $O(1)$ | [ ] |
| 073 | [Single Number](073_Find_the_number_that_appears_once_and_other_numbers_twice.md) | Easy | Bitwise XOR | $O(N^2)$ / $O(1)$ | $O(N)$ / $O(1)$ | [ ] |
| 074 | [Longest Subarray with Sum K (+ve)](074_Longest_subarray_with_given_sum_Kpositives.md) | Easy/Med | Sliding Window | $O(N^2)$ / $O(1)$ | $O(N)$ / $O(1)$ | [ ] |
| 075 | [Longest Subarray with Sum K (+ve/-ve)](075_Longest_subarray_with_sum_K.md) | Medium | Hashing | $O(N^2)$ / $O(1)$ | $O(N)$ / $O(N)$ | [ ] |
| 076 | [Two Sum](076_Two_Sum.md) | Easy | Hashing | $O(N^2)$ / $O(1)$ | $O(N)$ / $O(N)$ | [ ] |
| 077 | [Sort 0s 1s 2s](077_Sort_an_array_of_0s_1s_and_2s.md) | Medium | Three Pointer | $O(N \log N)$ / $O(1)$ | $O(N)$ / $O(1)$ | [ ] |
| 078 | [Majority Element (>N/2)](078_Majority_Element_I.md) | Medium | Voting Algo | $O(N^2)$ / $O(1)$ | $O(N)$ / $O(1)$ | [ ] |
| 079 | [Kadane's Algorithm](079_Kadanes_Algorithm.md) | Medium | DP / Greedy | $O(N^2)$ / $O(1)$ | $O(N)$ / $O(1)$ | [ ] |
| 080 | [Print Max Subarray Sum](080_Print_subarray_with_maximum_subarray_sum.md) | Medium | DP / Greedy | $O(N^2)$ / $O(1)$ | $O(N)$ / $O(1)$ | [ ] |
| 081 | [Stock Buy and Sell](081_Stock_Buy_and_Sell.md) | Easy | Iterative | $O(N^2)$ / $O(1)$ | $O(N)$ / $O(1)$ | [ ] |
| 082 | [Rearrange Elements by Sign](082_Rearrange_array_elements_by_sign.md) | Medium | Two Pointer | $O(N)$ / $O(N)$ | $O(N)$ / $O(N)$ | [ ] |
| 083 | [Next Permutation](083_Next_Permutation.md) | Medium | Vector Logic | $O(N! \cdot N)$ | $O(N)$ / $O(1)$ | [ ] |
| 084 | [Leaders in Array](084_Leaders_in_an_Array.md) | Easy | Iterative | $O(N^2)$ / $O(1)$ | $O(N)$ / $O(N)$ | [ ] |
| 085 | [Longest Consecutive Sequence](085_Longest_Consecutive_Sequence_in_an_Array.md) | Medium | Hashing | $O(N \log N)$ / $O(1)$ | $O(N)$ / $O(N)$ | [ ] |
| 086 | [Set Matrix Zeroes](086_Set_Matrix_Zeroes.md) | Medium | Vector Tracking | $O(N \cdot M \cdot (N+M))$ | $O(N \cdot M)$ / $O(1)$ | [ ] |
| 087 | [Rotate Matrix by 90](087_Rotate_matrix_by_90_degrees.md) | Medium | Transpose+Rev | $O(N^2)$ / $O(N^2)$ | $O(N^2)$ / $O(1)$ | [ ] |
| 088 | [Spiral Matrix Traversal](088_Print_the_matrix_in_spiral_manner.md) | Medium | Boundaries | $O(N \cdot M)$ / $O(N \cdot M)$ | $O(N \cdot M)$ / $O(1)$ | [ ] |
| 089 | [Subarray Sum Equals K](089_Count_subarrays_with_given_sum.md) | Medium | Hashing | $O(N^2)$ / $O(1)$ | $O(N)$ / $O(N)$ | [ ] |
| 090 | [Pascal's Triangle](090_Pascals_Triangle_I.md) | Medium | Combinatorics | $O(R^3)$ / $O(1)$ | $O(R^2)$ / $O(R^2)$ | [ ] |
| 091 | [Majority Element (>N/3)](091_Majority_Element_II.md) | Medium | Voting Algo | $O(N^2)$ / $O(1)$ | $O(N)$ / $O(1)$ | [ ] |
| 092 | [3 Sum](092_3_Sum.md) | Medium | Two Pointer | $O(N^3)$ / $O(1)$ | $O(N^2)$ / $O(1)$ | [ ] |
| 093 | [4 Sum](093_4_Sum.md) | Medium | Two Pointer | $O(N^4)$ / $O(1)$ | $O(N^3)$ / $O(1)$ | [ ] |
| 094 | [Largest Subarray Sum 0](094_Largest_Subarray_with_Sum_0.md) | Medium | Hashing | $O(N^2)$ / $O(1)$ | $O(N)$ / $O(N)$ | [ ] |
| 095 | [Subarrays with XOR K](095_Count_subarrays_with_given_xor_K.md) | Medium | Hashing | $O(N^2)$ / $O(1)$ | $O(N)$ / $O(N)$ | [ ] |
| 096 | [Merge Overlapping Intervals](096_Merge_Overlapping_Subintervals.md) | Medium | Sorting | $O(N \log N + N^2)$ | $O(N \log N)$ / $O(N)$ | [ ] |
| 097 | [Merge Sorted Arrays (no space)](097_Merge_two_sorted_arrays_without_extra_space.md) | Hard | Gap Method | $O(N \cdot M)$ / $O(1)$ | $O((N+M) \log (N+M))$ | [ ] |
| 098 | [Find Repeating & Missing](098_Find_the_repeating_and_missing_number.md) | Medium | Math / XOR | $O(N)$ / $O(N)$ | $O(N)$ / $O(1)$ | [ ] |
| 099 | [Count Inversions](099_Count_Inversions.md) | Hard | Merge Sort | $O(N^2)$ / $O(1)$ | $O(N \log N)$ / $O(N)$ | [ ] |
| 100 | [Reverse Pairs](100_Reverse_Pairs.md) | Hard | Merge Sort | $O(N^2)$ / $O(1)$ | $O(N \log N)$ / $O(N)$ | [ ] |
| 101 | [Max Product Subarray](101_Maximum_Product_Subarray_in_an_Array.md) | Medium | Prefix/Suffix | $O(N^2)$ / $O(1)$ | $O(N)$ / $O(1)$ | [ ] |
