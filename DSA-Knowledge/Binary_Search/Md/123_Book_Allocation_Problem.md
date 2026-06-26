# Book Allocation Problem

**Pattern:** Binary Search on Answer (Minimax Search Space)

**Recognition:**
- Allocate contiguous items (books/tasks) to a fixed number of workers (students) such that the maximum allocation to any worker is minimized.
- Array elements represent size/workload.
- The bounds of search space are `low = max(arr)` (min capacity required to assign the largest single book) and `high = sum(arr)` (max capacity when all books are assigned to one student).

**Optimal Code (Python):**
```python
def findPages(arr: list[int], n: int, m: int) -> int:
    # If there are fewer books than students, allocation is impossible
    if m > n:
        return -1
        
    def getRequiredStudents(max_allowed_pages: int) -> int:
        students = 1
        pages_allocated = 0
        
        for pages in arr:
            if pages_allocated + pages > max_allowed_pages:
                # Assign to the next student
                students += 1
                pages_allocated = pages
            else:
                pages_allocated += pages
                
        return students

    low = max(arr)
    high = sum(arr)
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        required_students = getRequiredStudents(mid)
        
        if required_students <= m:
            ans = mid
            high = mid - 1  # Attempt to find a smaller maximum workload
        else:
            low = mid + 1   # Increase page limit to reduce student count
            
    return ans
```

**Killer Edge:**
- Number of students `m` exceeds number of books `n` (edge check returns `-1`).
- All books have identical page counts.
- `m = 1` (returns the sum of all pages).

**Mistake:**
- Initializing `low = 0` or `low = 1` instead of `low = max(arr)`. Setting it too low allows the binary search to try values where a student cannot even be allocated the largest single book, breaking the logic.
- Miscalculating student count when transitioning: resetting `pages_allocated = 0` instead of `pages_allocated = pages` when moving to the next student.
