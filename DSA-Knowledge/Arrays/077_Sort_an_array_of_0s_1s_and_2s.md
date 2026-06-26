# Sort an array of 0s 1s and 2s

## Difficulty
Medium

---

## Pattern
Dutch National Flag Algorithm / Three Pointers

---

## Recognition Clues
- Sort a sequence consisting of exactly three distinct keys (typically 0, 1, and 2).
- Require sorting in-place in a single pass with $O(1)$ auxiliary space.

---

## Core Insight
- Partition the array into four segments using three pointers: `low`, `mid`, and `high`.
  - `nums[0...low-1]` are all `0`.
  - `nums[low...mid-1]` are all `1`.
  - `nums[mid...high]` are unsorted.
  - `nums[high+1...N-1]` are all `2`.
- By inspecting `nums[mid]` and swapping it into the low or high segment, we shrink the unsorted middle segment until `mid > high`.

---

## Interview Explanation
1. **Brute Force Idea**: Sort the array using a standard sorting algorithm (e.g., Merge Sort) taking $O(N \log N)$ time, or perform a counting sort: count the occurrences of `0`, `1`, and `2`, and overwrite the array in-place.
2. **Why Inefficient**: Standard sorting takes $O(N \log N)$ time. Counting sort is $O(N)$ but requires two full passes (one to count, one to overwrite) and does not sort by swapping elements, which can be an issue if the keys are attached to satellite data.
3. **Key Observation**: We can sort the array in a single pass using three pointers to represent boundaries for each color.
4. **Optimal Solution Intuition (Dutch National Flag)**:
   - Place `low = 0`, `mid = 0`, and `high = N - 1`.
   - While `mid <= high`:
     - If `nums[mid] == 0`: Swap `nums[mid]` and `nums[low]`. Since the swapped element at `low` is guaranteed to be a 1 (or it is `mid` itself), we can safely increment both `low` and `mid`.
     - If `nums[mid] == 1`: Increment `mid`.
     - If `nums[mid] == 2`: Swap `nums[mid]` and `nums[high]`, then decrement `high`. Do *not* increment `mid` because the element swapped from `high` is uninspected.
5. **Time Complexity**: $O(N)$ since the `mid` pointer advances or `high` pointer recedes at each step, taking at most $N$ operations.
6. **Space Complexity**: $O(1)$ auxiliary space since we sort strictly in-place.

---

## Brute Force
- **Idea**: Count frequencies of 0, 1, and 2, and overwrite the array sequentially.
- **Code**:
```python
def sort_colors_brute(nums):
    cnt0 = nums.count(0)
    cnt1 = nums.count(1)
    cnt2 = nums.count(2)
    
    # Overwrite the array
    for i in range(cnt0):
        nums[i] = 0
    for i in range(cnt0, cnt0 + cnt1):
        nums[i] = 1
    for i in range(cnt0 + cnt1, len(nums)):
        nums[i] = 2
    return nums
```
- **TC**: $O(N)$ (requires two passes)
- **SC**: $O(1)$

---

## Optimal Approach
- **Algorithm**: Dutch National Flag (Three Pointers).
  1. Initialize `low = 0`, `mid = 0`, `high = len(nums) - 1`.
  2. While `mid <= high`:
     - If `nums[mid] == 0`, swap `nums[low]` and `nums[mid]`, increment `low` and `mid`.
     - If `nums[mid] == 1`, increment `mid`.
     - Else (`nums[mid] == 2`), swap `nums[mid]` and `nums[high]`, decrement `high`.
- **Why it works**: The algorithm maintains loop invariants: all elements to the left of `low` are 0, all elements between `low` and `mid-1` are 1, and all elements to the right of `high` are 2.
- **Complexity**: Time: $O(N)$ (single pass), Space: $O(1)$.

---

## Optimal Code
```python
def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            # Swap with low boundary and advance both pointers
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else: # nums[mid] == 2
            # Swap with high boundary, decrement high, but do not advance mid
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            
    return nums
```

---

## Test Cases
- **Normal Case**: 
  - Input: `nums = [2, 0, 2, 1, 1, 0]`
  - Output: `[0, 0, 1, 1, 2, 2]`
- **Hard Case**: 
  - Input: `nums = [2, 2, 1, 1, 0, 0]`
  - Output: `[0, 0, 1, 1, 2, 2]`
- **Edge Case**: 
  - Input: `nums = [1]`
  - Output: `[1]`

---

## Common Mistakes
- **Incrementing `mid` when swapping with `high`**: The element brought from `high` to `mid` is unsorted and must be evaluated in the next iteration.
- **Incorrect loop boundary**: Using `while mid < high` instead of `while mid <= high`. If the element at `high` is not checked, it could remain out of place.

---

## Killer Edge Cases
- Array contains only one of the three numbers (e.g., `[2, 2, 2]`).
- Array is already sorted.
- Array has length 1.

---

## Follow-Up Variants
- **Sort 3 Colors** $\rightarrow$ **Sort 4 Colors (0, 1, 2, 3)**:
  - *Delta*: Maintain four pointers (`low`, `mid1`, `mid2`, `high`) to define five boundaries.

---

## Similar Problems
- Sort Colors (LeetCode 75)
- 3-Way Partitioning (GFG)

---

## Theory Connections
- **Dijkstra's 3-Way Partitioning**: Dutch National Flag is Dijkstra's solution to partition elements around a pivot range. Modern implementations of QuickSort (such as dual-pivot QuickSort in Java) use 3-way partitioning to avoid $O(N^2)$ worst-case time complexity when sorting inputs with high duplicate counts.

---

## Personal Progress

**Confidence**
- [ ] 0
- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4
- [ ] 5

**Time Bucket**
- [ ] <10 min
- [ ] 10-20
- [ ] 20-40
- [ ] 40+

**Status**
- [ ] Not Attempted
- [ ] Hint Used
- [ ] Solved
- [ ] Mastered

**Revision Count**: 
**Last Revised**: 
**Next Review**: 

---

## Notes

