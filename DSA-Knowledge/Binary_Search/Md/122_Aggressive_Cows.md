# Aggressive Cows

**Pattern:** Binary Search on Answer (Monotonic Feasibility Function)

**Recognition:**
- Find the **maximum possible minimum distance** between items (minimax optimization).
- Feasibility check is monotonic: if a minimum distance of `d` is possible, any distance `< d` is also possible.
- The sorted position of stalls enables greedy placement check in $O(N)$ time.

**Optimal Code (Python):**
```python
def aggressiveCows(stalls: list[int], k: int) -> int:
    # Sort stalls to enable greedy coordinate placement
    stalls.sort()
    
    def canPlace(min_dist: int) -> bool:
        count = 1
        last_pos = stalls[0]
        
        for i in range(1, len(stalls)):
            if stalls[i] - last_pos >= min_dist:
                count += 1
                last_pos = stalls[i]
                if count >= k:
                    return True
        return False

    low = 1
    high = stalls[-1] - stalls[0]
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        if canPlace(mid):
            ans = mid
            low = mid + 1  # Try to maximize the minimum distance
        else:
            high = mid - 1 # Reduce search space
            
    return ans
```

**Killer Edge:**
- $k = 2$ cows (returns the distance between first and last stall).
- Coinciding stalls or very large coordinates.

**Mistake:**
- Forgetting to sort the `stalls` array before running binary search. The coordinate system must be sorted for the greedy check to work.
- Mismatching pointer updates: shifting `low` to `mid` instead of `mid + 1`, causing an infinite loop.
