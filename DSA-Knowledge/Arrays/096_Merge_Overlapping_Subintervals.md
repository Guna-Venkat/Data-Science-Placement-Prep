# Merge Overlapping Subintervals

## Difficulty
Medium

---

## Pattern
Sorting / Array Interval

---

## Recognition Clues
- Merge all overlapping intervals.\n- Return an array of the non-overlapping intervals that cover all input intervals.

---

## Core Insight
- If we sort the intervals by their start values, overlapping intervals will become adjacent.\n- We can iterate through the sorted list: if the current interval starts after the previously merged interval ends, we append it as a new interval.\n- Otherwise, they overlap; merge them by updating the end boundary of the previous interval to the maximum of both ends.

---

## Interview Explanation
1. **Brute Force Idea**: Compare every interval with every other interval. If they overlap, merge them and remove the duplicates. Repeat this process until no overlapping intervals remain.
2. **Why Inefficient**: Takes $O(N^2)$ or $O(N^3)$ time due to repeated comparisons and updates.
3. **Key Observation**: Sorting the intervals by their start times ensures that any potential merge partners are placed next to each other. We can then solve the problem in a single pass ($O(N)$ after sorting).
4. **Optimal Solution Intuition**:
   - Sort the intervals by `start` values.
   - Create a list `merged` and append the first interval to it.
   - For each subsequent interval:
     - If `current.start <= merged[-1].end`, they overlap. Set `merged[-1].end = max(merged[-1].end, current.end)`.
     - Else, they do not overlap. Append `current` to `merged`.
5. **Time Complexity**: $O(N \log N)$ (due to sorting).
6. **Space Complexity**: $O(N)$ (to store the merged intervals).

---

## Brute Force
- **Idea**: Compare all intervals iteratively and merge them.
- **Code**:
```python
def merge_brute(intervals):
    # Highly complex and nested updates; omitted for brevity.
    pass
```
- **TC**: $O(N^2)$
- **SC**: $O(N)$

---

## Optimal Approach
- **Algorithm**: Sort-and-sweep interval merging.
- **Why it works**: Sorting by start times orders the intervals chronologically, meaning we only need to compare the current interval with the last merged interval.
- **Complexity**: Time: $O(N \log N)$, Space: $O(N)$ (or $O(1)$ if sorting in-place and ignoring output space).

---

## Optimal Code
```python
def mergeIntervals(intervals):
    if not intervals:
        return []
        
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for i in range(1, len(intervals)):
        current = intervals[i]
        prev = merged[-1]
        
        # If current interval overlaps with prev, merge them
        if current[0] <= prev[1]:
            prev[1] = max(prev[1], current[1])
        else:
            # Otherwise, append as new interval
            merged.append(current)
            
    return merged
```

---

## Test Cases
- **Normal Case**: Input: `intervals = [[1,3],[2,6],[8,10],[15,18]]`\n- Output: `[[1,6],[8,10],[15,18]]`
- **Hard Case**: Input: `intervals = [[1,4],[4,5]]`\n- Output: `[[1,5]]`
- **Edge Case**: Input: `intervals = [[1,4]]`\n- Output: `[[1,4]]`

---

## Common Mistakes
- Forgetting to sort the intervals first.\n- Using `current.start < prev.end` instead of `<=`, which misses intervals that touch at boundaries (e.g. `[1, 4]` and `[4, 5]`).\n- Not updating `prev.end` to the *maximum* of both ends (e.g. if `[1, 5]` and `[2, 3]` are merged, the end remains 5, not 3).

---

## Killer Edge Cases
- Intervals are already sorted and disjoint.\n- All intervals overlap into a single large interval.\n- An interval is fully contained inside another interval (nested intervals).

---

## Follow-Up Variants
- Merge Intervals $\rightarrow$ Insert Interval (insert a new interval and merge).

---

## Similar Problems
- Insert Interval (LeetCode 57)\n- Non-overlapping Intervals (LeetCode 435)

---

## Theory Connections
- Interval Scheduling / Sweep-Line: Order points chronologically and process them using boundary status sweeps. This is a foundational technique in computer graphics, computational geometry (Bentley-Ottmann algorithm), and database range locks.

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
