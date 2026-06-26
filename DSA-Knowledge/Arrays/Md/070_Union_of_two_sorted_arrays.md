# Union of two sorted arrays

## Difficulty
Easy

---

## Pattern
Two Pointers / Sorted Merge (similar to Merge Sort)

---

## Recognition Clues
- Two input arrays are sorted.
- Need a combined sorted representation containing all unique elements from both.

---

## Core Insight
- Leverage the sorted nature of both arrays by scanning them simultaneously with two pointers. 
- At each step, select the smaller of the two pointed elements and append it to the union array if it does not match the previously appended element.

---

## Interview Explanation
1. **Brute Force Idea**: Place all elements from both arrays into a hash set (to remove duplicates), convert the set back to a list, and sort it.
2. **Why Inefficient**: Sorting the merged set takes $O((N+M) \log (N+M))$ time. This wastes the sorted property of the input arrays.
3. **Key Observation**: By comparing elements at the front of both arrays using two pointers, we can build the sorted union in a single linear pass ($O(N+M)$).
4. **Optimal Solution Intuition**: Initialize pointers `i = 0` and `j = 0`. Create an empty list `union`. At each step:
   - Compare `arr1[i]` and `arr2[j]`.
   - Add the smaller value to `union` if `union` is empty or if the value is different from `union[-1]` (to avoid duplicates).
   - Increment the pointer that pointed to the smaller value (or both if they were equal).
   - Continue until one array is exhausted, then append the remaining elements of the other array in a similar duplicate-free fashion.
5. **Time Complexity**: $O(N+M)$ because we traverse both arrays once.
6. **Space Complexity**: $O(N+M)$ in the worst case to store the union list, but the auxiliary space used by the algorithm logic is $O(1)$.

---

## Brute Force
- **Idea**: Insert all elements into a Set, then sort and return.
- **Code**:
```python
def union_sorted_brute(arr1, arr2):
    s = set(arr1).union(set(arr2))
    return sorted(list(s))
```
- **TC**: $O((N+M)\log(N+M))$
- **SC**: $O(N+M)$

---

## Optimal Approach
- **Algorithm**:
  1. Initialize `i = 0`, `j = 0`, and `union = []`.
  2. Create a helper function `append_unique(val)` that appends `val` to `union` only if `union` is empty or `union[-1] != val`.
  3. While `i < len(arr1)` and `j < len(arr2)`:
     - If `arr1[i] < arr2[j]`, call `append_unique(arr1[i])` and increment `i`.
     - If `arr2[j] < arr1[i]`, call `append_unique(arr2[j])` and increment `j`.
     - Else, call `append_unique(arr1[i])` and increment both `i` and `j`.
  4. Append remaining elements of `arr1` and `arr2` using `append_unique`.
- **Why it works**: By processing elements in increasing order and checking the tail of `union`, we ensure that elements are added in sorted order and duplicates are filtered on-the-fly.
- **Complexity**: Time: $O(N+M)$, Space: $O(1)$ auxiliary space.

---

## Optimal Code
```python
def find_union(arr1, arr2):
    i, j = 0, 0
    union = []
    
    def append_unique(val):
        if not union or union[-1] != val:
            union.append(val)
            
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            append_unique(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            append_unique(arr2[j])
            j += 1
        else:
            append_unique(arr1[i])
            i += 1
            j += 1
            
    while i < len(arr1):
        append_unique(arr1[i])
        i += 1
        
    while j < len(arr2):
        append_unique(arr2[j])
        j += 1
        
    return union
```

---

## Test Cases
- **Normal Case**: 
  - Input: `arr1 = [1, 2, 3, 4, 5]`, `arr2 = [2, 3, 5, 6, 7]`
  - Output: `[1, 2, 3, 4, 5, 6, 7]`
- **Hard Case**: 
  - Input: `arr1 = [1, 1, 1]`, `arr2 = [2, 2, 2]`
  - Output: `[1, 2]`
- **Edge Case**: 
  - Input: `arr1 = []`, `arr2 = [1, 2, 3]`
  - Output: `[1, 2, 3]`

---

## Common Mistakes
- Index out of bounds when appending remaining elements of the unfinished array.
- Forgetting to check `not union` when appending, leading to list index out of range for the first element.
- Not handling duplicates that exist inside a single input array (e.g. `arr1 = [1, 1, 2]`).

---

## Killer Edge Cases
- One or both input arrays are empty.
- Arrays contain duplicate values internally.
- Arrays have no common elements.

---

## Follow-Up Variants
- **Union of Sorted Arrays** $\rightarrow$ **Intersection of Sorted Arrays**: Return only the common elements of both sorted arrays without duplicates.
  - *Delta*: Only append to the output when `arr1[i] == arr2[j]`.

---

## Similar Problems
- Intersection of Two Sorted Arrays
- Merge Two Sorted Arrays (LeetCode 88)

---

## Theory Connections
- **Merge Operation**: This is a direct implementation of the two-way merge algorithm. Merging forms the foundational combination step in Merge Sort, External Sorting (for large files), and merge-join operations in relational database engines.

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

